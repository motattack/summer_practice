setting_black = \
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
    
    QCheckBox{
      color: white;
    }
    
    QCheckBox::indicator {
      background: white;
      border: 1px solid #cfd6d9;
      border-radius: 2px;
      height: 18px;
      width: 18px;
    }
    
    QCheckBox::indicator:hover {
      background: #e2eaee;
    }
    
    QCheckBox::indicator:indeterminate {
        background: white;
      color: white;
    }
    
    QCheckBox:checked {
      color: green;
    }
    
    QCheckBox::indicator:checked{
      background: #036ee9;
      border-color: #2094e5;
      image: url(engine/assets/tick.png);
    }
    
    QCheckBox::indicator:checked > img {
      background: red;
    }
    
    QPushButton {
        color: white;
        border-radius: 5px;
        font-size: 10pt;
        background:  grey;
    }"""

setting_white = \
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

    QCheckBox{
      color: black;
    }

    QCheckBox::indicator {
      background: white;
      border: 1px solid #cfd6d9;
      border-radius: 2px;
      height: 18px;
      width: 18px;
    }

    QCheckBox::indicator:hover {
      background: #e2eaee;
    }

    QCheckBox::indicator:indeterminate {
        background: white;
      color: white;
    }

    QCheckBox:checked {
      color: green;
    }

    QCheckBox::indicator:checked{
      background: #036ee9;
      border-color: #2094e5;
      image: url(engine/assets/tick.png);
    }

    QCheckBox::indicator:checked > img {
      background: red;
    }

    QPushButton {
        color: white;
        border-radius: 5px;
        font-size: 10pt;
        background:  grey;
    }"""
