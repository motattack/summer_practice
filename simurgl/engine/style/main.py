main_black = \
    """QWidget {
        font-family: Montserrat;
        font-style: normal;
        font-weight: 600;
        font-size: 14pt;
    
        background: black;
    }
    
    #centralwidget {
    border: 0.5px solid #e3e3f3;
    }
    
    #btn_exit {
        background: #4a4a4a;
    }
    
    #btn_exit:hover {
        background: #df4646;
    }
    
    QPushButton {
        color: white;
        border-radius: 5px;
        font-size: 10pt;
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(14, 157, 255), stop:1 rgb(0, 112, 235));
    }
    
    QPushButton:hover {
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(65, 178, 255), stop:1 rgb(31, 138, 255));
    }
    
    #logs, #settings, #theme {
        color: #c5c5c5;
        background: none;
    }
    
    QLineEdit {
        color: #fff;
        border: 2px solid #c5c5c5;
        border-radius: 5px;
    }
"""
main_white = \
    """QWidget {
        font-family: Montserrat;
        font-style: normal;
        font-weight: 600;
        font-size: 14pt;

        background: white;
    }

    #centralwidget {
    border: 0.5px solid #e3e3f3;
    }

    #btn_exit {
        background: #4a4a4a;
    }

    #btn_exit:hover {
        background: #df4646;
    }

    QPushButton {
        color: white;
        border-radius: 5px;
        font-size: 10pt;
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(14, 157, 255), stop:1 rgb(0, 112, 235));
    }

    QPushButton:hover {
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(65, 178, 255), stop:1 rgb(31, 138, 255));
    }

    #logs, #settings, #theme {
        color: #c5c5c5;
        background: none;
    }

    QLineEdit {
        color: black;
        border: 2px solid black;
        border-radius: 5px;
    }
"""