# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'engine/ui/error.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(411, 211)
        Error.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(Error)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 391, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title.setMaximumSize(QtCore.QSize(500, 40))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.error = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.error.setMinimumSize(QtCore.QSize(0, 0))
        self.error.setText("")
        self.error.setScaledContents(True)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setWordWrap(True)
        self.error.setObjectName("error")
        self.verticalLayout.addWidget(self.error)
        self.ok = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ok.setObjectName("ok")
        self.verticalLayout.addWidget(self.ok)
        Error.setCentralWidget(self.centralwidget)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "MainWindow"))
        self.title.setText(_translate("Error", "Упс! Что-то пошло не так"))
        self.ok.setText(_translate("Error", "ОК"))