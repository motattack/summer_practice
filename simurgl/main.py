import sqlite3
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QTableWidgetItem
from PyQt5.QtCore import Qt

from engine.widget.ui.logs import *
from engine.widget.ui.main import *
from engine.widget.ui.settings import *
from engine.widget.ui.move import MoveWindow
from engine.widget.ui.error import *

from engine.style.main import main_black, main_white
from engine.style.settings import setting_black, setting_white
from engine.style.logs import logs_black, logs_white
from engine.style.error import error_black, error_white
from engine.tool.config import theme_style, update_theme, update_autorun, update_hide_mode, update_protect, \
    autorun_status, hide_mod_status, protect_status, api, username, update_api, update_username, get_hide_mode

import engine.bot.main as bot
from engine.bot.checkAPI import check

from engine.tool.autorun import ar_add, ar_remove

db = sqlite3.connect("engine/bot/Logs.db", check_same_thread=False)
c = db.cursor()


class Bot(QtCore.QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        bot.app()


class Calc(MoveWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.bot = Bot()

        self.old_pos = None

        self.ui.api.setText(api)
        self.ui.username.setText(username)

        self.ui.btn_exit.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ui.settings.clicked.connect(self.setting)
        self.ui.btn_confirm.clicked.connect(self.confirm)
        self.ui.logs.clicked.connect(self.get_logs)
        self.ui.theme.clicked.connect(self.change_themes)
        self.theme_style = theme_style
        self.change_themes()

        self.error = None
        self.error_message = None
        self.not_run = True
        self.hide_mod_status = hide_mod_status

        if check(api):
            self.bot.start()

        if self.hide_mod_status:
            self.hide()
        else:
            self.show()

    def change_themes(self):
        if self.theme_style:
            self.ui.theme.setText("⬛️")
            self.setStyleSheet(main_white)
        else:
            self.ui.theme.setText("⬜️")
            self.setStyleSheet(main_black)
        update_theme(self.theme_style)
        self.theme_style = not self.theme_style

    def confirm(self):
        global api, username
        if self.ui.api.text() != api:
            self.update_api()
            api = self.ui.api.text()
        if self.ui.username.text() != username:
            self.update_username()
            username = self.ui.username.text()
        if check(api) and self.not_run:
            self.not_run = False
            self.bot.start()
        elif self.not_run:
            self.error_message = "Проверьте правильность токена"
            self.error = Error("Проверьте правильность токена", self)
            self.error.show()
        else:
            self.error_message = "Вы уже вошли!"
            self.error = Error("Вы уже вошли!", self)
            self.error.show()

    def update_api(self):
        global api
        api = self.ui.api.text()
        update_api(api)

    def update_username(self):
        global username
        username = self.ui.username.text()
        update_username(username)

    def setting(self):
        win_setting = Setting(self)
        win_setting.setGeometry(
            QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, win_setting.size(), self.geometry()))
        win_setting.show()

    def get_logs(self):
        win_logs = Logs(self)
        win_logs.setGeometry(
            QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, win_logs.size(), self.geometry()))
        win_logs.show()

    def hide_on(self):
        self.resize(1, 1)
        self.move(9999, 9999)


class Setting(MoveWindow, QMainWindow):
    def __init__(self, parent=Calc):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui = Ui_Settings()
        self.ui.setupUi(self)

        self.old_pos = None

        self.ui.back.clicked.connect(self.back_to_main)

        self.ui.autorun.setChecked(autorun_status)
        self.ui.autorun.stateChanged.connect(self.autorun)

        self.ui.hide_mod.setChecked(hide_mod_status)
        self.ui.hide_mod.stateChanged.connect(self.hide_mod)

        self.ui.protect.setChecked(protect_status)
        self.ui.protect.stateChanged.connect(self.protect)

        self.parent = parent

        self.change_themes()

    def autorun(self):
        global autorun_status
        autorun_status = self.ui.autorun.isChecked()
        update_autorun(autorun_status)
        if autorun_status:
            ar_add(str(os.path.dirname(os.path.realpath(__name__))))
        else:
            ar_remove(str(os.path.dirname(os.path.realpath(__name__))))

    def hide_mod(self):
        global hide_mod_status
        hide_mod_status = self.ui.hide_mod.isChecked()
        update_hide_mode(hide_mod_status)
        self.parent.hide() if hide_mod_status else self.parent.show()

    def protect(self):
        global protect_status
        protect_status = self.ui.protect.isChecked()
        update_protect(protect_status)

    def back_to_main(self):
        self.hide()
        if self.parent.hide_mod_status:
            self.parent.hide_on()

    def change_themes(self):
        if self.parent.theme_style:
            self.setStyleSheet(setting_black)
        else:
            self.setStyleSheet(setting_white)


class Logs(MoveWindow, QMainWindow):
    def __init__(self, parent=Calc):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui = Ui_Logs()
        self.ui.setupUi(self)

        self.old_pos = None

        self.ui.back.clicked.connect(self.back_to_main)
        self.parent = parent

        self.change_themes()

        self.db_logs = c.execute("""SELECT * FROM Logs""").fetchall()
        self.write(self.db_logs)

    def change_themes(self):
        if self.parent.theme_style:
            self.setStyleSheet(logs_black)
        else:
            self.setStyleSheet(logs_white)

    def write(self, db_logs):
        for i, film in enumerate(db_logs):
            self.ui.tableWidget.insertRow(self.ui.tableWidget.rowCount())
            for j, data in enumerate(film):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(data)))

    def back_to_main(self):
        self.hide()
        self.parent.show()


class Error(MoveWindow, QMainWindow):
    def __init__(self, text, parent=Calc):
        super().__init__(parent)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui = Ui_Error()
        self.ui.setupUi(self)

        self.ui.error.setText(text)

        self.ui.ok.clicked.connect(self.ok)
        self.parent = parent

        self.change_themes()

    def ok(self):
        self.close()

    def change_themes(self):
        if self.parent.theme_style:
            self.setStyleSheet(error_black)
        else:
            self.setStyleSheet(error_white)


def main():
    app = QApplication(sys.argv)
    window = Calc()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

db.close()
