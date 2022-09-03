from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class BackGround(object):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(16777215, 16777215)
        MainWindow.setMinimumSize(QtCore.QSize(133, 133))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("/*\n"
                                 " * The MIT License (MIT)\n"
                                 " *\n"
                                 " * Copyright (c) <2013-2014> <Colin Duquesnoy>\n"
                                 " *\n"
                                 " * Permission is hereby granted, free of charge, to any person obtaining a copy\n"
                                 " * of this software and associated documentation files (the \"Software\"), to deal\n"
                                 " * in the Software without restriction, including without limitation the rights\n"
                                 " * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
                                 " * copies of the Software, and to permit persons to whom the Software is\n"
                                 " * furnished to do so, subject to the following conditions:\n"
                                 "\n"
                                 " * The above copyright notice and this permission notice shall be included in\n"
                                 " * all copies or substantial portions of the Software.\n"
                                 "\n"
                                 " * THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
                                 " * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
                                 " * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
                                 " * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
                                 " * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
                                 " * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n"
                                 " * THE SOFTWARE.\n"
                                 " */\n"
                                 "\n"
                                 "QProgressBar:horizontal {\n"
                                 "    border: 1px solid qlineargradient(x1: 0, x2: 1,"
                                 " stop: 0  #f3f4f8, stop: 1 #5b5d6d);\n"
                                 "    text-align: center;\n"
                                 "    padding: 1px;\n"
                                 "    background: #201F1F;\n"
                                 "}\n"
                                 "QProgressBar::chunk:horizontal {\n"
                                 "    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0,"
                                 " stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));\n"
                                 "}\n"
                                 "\n"
                                 "QToolTip\n"
                                 "{\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    background-color: rgb(90, 102, 117);;\n"
                                 "    color: white;\n"
                                 "    padding: 1px;\n"
                                 "    opacity: 200;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget\n"
                                 "{\n"
                                 "    color: silver;\n"
                                 "    background-color: #302F2F;\n"
                                 "    selection-background-color:#3d8ec9;\n"
                                 "    selection-color: black;\n"
                                 "    background-clip: border;\n"
                                 "    border-image: none;\n"
                                 "    outline: 0;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:hover\n"
                                 "{\n"
                                 "    background-color: #78879b;\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:selected\n"
                                 "{\n"
                                 "    background-color: #3d8ec9;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox\n"
                                 "{\n"
                                 "    spacing: 5px;\n"
                                 "    outline: none;\n"
                                 "    color: #bbb;\n"
                                 "    margin-bottom: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:disabled\n"
                                 "{\n"
                                 "    color: #777777;\n"
                                 "}\n"
                                 "QCheckBox::indicator,\n"
                                 "QGroupBox::indicator\n"
                                 "{\n"
                                 "    width: 18px;\n"
                                 "    height: 18px;\n"
                                 "}\n"
                                 "QGroupBox::indicator\n"
                                 "{\n"
                                 "    margin-left: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked,\n"
                                 "QCheckBox::indicator:unchecked:hover,\n"
                                 "QGroupBox::indicator:unchecked,\n"
                                 "QGroupBox::indicator:unchecked:hover\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked:focus,\n"
                                 "QCheckBox::indicator:unchecked:pressed,\n"
                                 "QGroupBox::indicator:unchecked:focus,\n"
                                 "QGroupBox::indicator:unchecked:pressed\n"
                                 "{\n"
                                 "  border: none;\n"
                                 "    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked,\n"
                                 "QCheckBox::indicator:checked:hover,\n"
                                 "QGroupBox::indicator:checked,\n"
                                 "QGroupBox::indicator:checked:hover\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/checkbox_checked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked:focus,\n"
                                 "QCheckBox::indicator:checked:pressed,\n"
                                 "QGroupBox::indicator:checked:focus,\n"
                                 "QGroupBox::indicator:checked:pressed\n"
                                 "{\n"
                                 "  border: none;\n"
                                 "    image: url(:/dark_blue/img/checkbox_checked_focus.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:indeterminate,\n"
                                 "QCheckBox::indicator:indeterminate:hover,\n"
                                 "QCheckBox::indicator:indeterminate:pressed\n"
                                 "QGroupBox::indicator:indeterminate,\n"
                                 "QGroupBox::indicator:indeterminate:hover,\n"
                                 "QGroupBox::indicator:indeterminate:pressed\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/checkbox_indeterminate.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:indeterminate:focus,\n"
                                 "QGroupBox::indicator:indeterminate:focus\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/checkbox_indeterminate_focus.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked:disabled,\n"
                                 "QGroupBox::indicator:checked:disabled\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:unchecked:disabled,\n"
                                 "QGroupBox::indicator:unchecked:disabled\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton\n"
                                 "{\n"
                                 "    spacing: 5px;\n"
                                 "    outline: none;\n"
                                 "    color: #bbb;\n"
                                 "    margin-bottom: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton:disabled\n"
                                 "{\n"
                                 "    color: #777777;\n"
                                 "}\n"
                                 "QRadioButton::indicator\n"
                                 "{\n"
                                 "    width: 21px;\n"
                                 "    height: 21px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:unchecked,\n"
                                 "QRadioButton::indicator:unchecked:hover\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/radio_unchecked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:unchecked:focus,\n"
                                 "QRadioButton::indicator:unchecked:pressed\n"
                                 "{\n"
                                 "  border: none;\n"
                                 "  outline: none;\n"
                                 "    image: url(:/dark_blue/img/radio_unchecked_focus.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked,\n"
                                 "QRadioButton::indicator:checked:hover\n"
                                 "{\n"
                                 "  border: none;\n"
                                 "  outline: none;\n"
                                 "    image: url(:/dark_blue/img/radio_checked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked:focus,\n"
                                 "QRadioButton::indicato::menu-arrowr:checked:pressed\n"
                                 "{\n"
                                 "  border: none;\n"
                                 "  outline: none;\n"
                                 "    image: url(:/dark_blue/img/radio_checked_focus.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:indeterminate,\n"
                                 "QRadioButton::indicator:indeterminate:hover,\n"
                                 "QRadioButton::indicator:indeterminate:pressed\n"
                                 "{\n"
                                 "        image: url(:/dark_blue/img/radio_indeterminate.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked:disabled\n"
                                 "{\n"
                                 "  outline: none;\n"
                                 "  image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:unchecked:disabled\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QMenuBar\n"
                                 "{\n"
                                 "    background-color: #302F2F;\n"
                                 "    color: silver;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:selected\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:pressed\n"
                                 "{\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    background-color: #3d8ec9;\n"
                                 "    color: black;\n"
                                 "    margin-bottom:-1px;\n"
                                 "    padding-bottom:1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu\n"
                                 "{\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    color: silver;\n"
                                 "    margin: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::icon\n"
                                 "{\n"
                                 "    margin: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item\n"
                                 "{\n"
                                 "    padding: 2px 2px 2px 25px;\n"
                                 "    margin-left: 5px;\n"
                                 "    border: 1px solid transparent; /* reserve space for selection border */\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item:selected\n"
                                 "{\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::separator {\n"
                                 "    height: 2px;\n"
                                 "    background: lightblue;\n"
                                 "    margin-left: 10px;\n"
                                 "    margin-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator {\n"
                                 "    width: 16px;\n"
                                 "    height: 16px;\n"
                                 "}\n"
                                 "\n"
                                 "/* non-exclusive indicator = check box style indicator\n"
                                 "   (see QActionGroup::setExclusive) */\n"
                                 "QMenu::indicator:non-exclusive:unchecked {\n"
                                 "    image: url(:/dark_blue/img/checkbox_unchecked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:non-exclusive:unchecked:selected {\n"
                                 "    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:non-exclusive:checked {\n"
                                 "    image: url(:/dark_blue/img/checkbox_checked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:non-exclusive:checked:selected {\n"
                                 "    image: url(:/dark_blue/img/checkbox_checked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "/* exclusive indicator ="
                                 " radio button style indicator (see QActionGroup::setExclusive) */\n"
                                 "QMenu::indicator:exclusive:unchecked {\n"
                                 "    image: url(:/dark_blue/img/radio_unchecked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:exclusive:unchecked:selected {\n"
                                 "    image: url(:/dark_blue/img/radio_unchecked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:exclusive:checked {\n"
                                 "    image: url(:/dark_blue/img/radio_checked.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::indicator:exclusive:checked:selected {\n"
                                 "    image: url(:/dark_blue/img/radio_checked_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::right-arrow {\n"
                                 "    margin: 5px;\n"
                                 "    image: url(:/dark_blue/img/right_arrow.png)\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QWidget:disabled\n"
                                 "{\n"
                                 "    color: #808080;\n"
                                 "    background-color: #302F2F;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractItemView\n"
                                 "{\n"
                                 "    alternate-background-color: #3A3939;\n"
                                 "    color: silver;\n"
                                 "    border: 1px solid 3A3939;\n"
                                 "    border-radius: 2px;\n"
                                 "    padding: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:focus, QMenuBar:focus\n"
                                 "{\n"
                                 "    border: 1px solid #78879b;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus\n"
                                 "{\n"
                                 "    border: none;\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "    background-color: #201F1F;\n"
                                 "    padding: 2px;\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid qlineargradient(x1: 0,"
                                 " x2: 1, stop: 0  #f3f4f8, stop: 1 #5b5d6d);\n"
                                 "    border-radius: 2px;\n"
                                 "    color: silver;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox {\n"
                                 "    border:1px solid #3A3939;\n"
                                 "    border-radius: 2px;\n"
                                 "    margin-top: 20px;\n"
                                 "    background-color: #302F2F;\n"
                                 "    color: silver;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox::title {\n"
                                 "    subcontrol-origin: margin;\n"
                                 "    subcontrol-position: top center;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    padding-top: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractScrollArea\n"
                                 "{\n"
                                 "    border-radius: 2px;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    background-color: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal\n"
                                 "{\n"
                                 "    height: 15px;\n"
                                 "    margin: 3px 15px 3px 15px;\n"
                                 "    border: 1px transparent #2A2929;\n"
                                 "    border-radius: 4px;\n"
                                 "    background-color: #2A2929;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal\n"
                                 "{\n"
                                 "    background-color: #605F5F;\n"
                                 "    min-width: 5px;\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal\n"
                                 "{\n"
                                 "    margin: 0px 3px 0px 3px;\n"
                                 "    border-image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
                                 "    width: 10px;\n"
                                 "    height: 10px;\n"
                                 "    subcontrol-position: right;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal\n"
                                 "{\n"
                                 "    margin: 0px 3px 0px 3px;\n"
                                 "    border-image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: left;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on\n"
                                 "{\n"
                                 "    border-image: url(:/dark_blue/img/right_arrow.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: right;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on\n"
                                 "{\n"
                                 "    border-image: url(:/dark_blue/img/left_arrow.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: left;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
                                 "{\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                 "{\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical\n"
                                 "{\n"
                                 "    background-color: #2A2929;\n"
                                 "    width: 15px;\n"
                                 "    margin: 15px 3px 15px 3px;\n"
                                 "    border: 1px transparent #2A2929;\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical\n"
                                 "{\n"
                                 "    background-color: #605F5F;\n"
                                 "    min-height: 5px;\n"
                                 "    border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical\n"
                                 "{\n"
                                 "    margin: 3px 0px 3px 0px;\n"
                                 "    border-image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical\n"
                                 "{\n"
                                 "    margin: 3px 0px 3px 0px;\n"
                                 "    border-image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: bottom;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on\n"
                                 "{\n"
                                 "\n"
                                 "    border-image: url(:/dark_blue/img/up_arrow.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
                                 "{\n"
                                 "    border-image: url(:/dark_blue/img/down_arrow.png);\n"
                                 "    height: 10px;\n"
                                 "    width: 10px;\n"
                                 "    subcontrol-position: bottom;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                 "{\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                 "{\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit\n"
                                 "{\n"
                                 "    background-color: #201F1F;\n"
                                 "    color: silver;\n"
                                 "    border: 1px solid white;\n"
                                 "}\n"
                                 "\n"
                                 "QPlainTextEdit\n"
                                 "{\n"
                                 "    background-color: #201F1F;;\n"
                                 "    color: silver;\n"
                                 "    border-radius: 2px;\n"
                                 "    border: 1px solid white;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section\n"
                                 "{\n"
                                 "    background-color: #3A3939;\n"
                                 "    color: silver;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "}\n"
                                 "\n"
                                 "QSizeGrip {\n"
                                 "    image: url(:/dark_blue/img/sizegrip.png);\n"
                                 "    width: 12px;\n"
                                 "    height: 12px;\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow\n"
                                 "{\n"
                                 "    background-color: #302F2F;\n"
                                 "\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator\n"
                                 "{\n"
                                 "    background-color: #302F2F;\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    spacing: 2px;\n"
                                 "    border: 1px dashed #3A3939;\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator:hover\n"
                                 "{\n"
                                 "\n"
                                 "    background-color: #787876;\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    spacing: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QMenu::separator\n"
                                 "{\n"
                                 "    height: 1px;\n"
                                 "    background-color: #3A3939;\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    margin-left: 10px;\n"
                                 "    margin-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QFrame\n"
                                 "{\n"
                                 "    border-radius: 2px;\n"
                                 "    border: 1px solid #444;\n"
                                 "}\n"
                                 "\n"
                                 "QFrame[frameShape=\"0\"]\n"
                                 "{\n"
                                 "    border-radius: 2px;\n"
                                 "    border: 1px transparent #444;\n"
                                 "}\n"
                                 "\n"
                                 "QStackedWidget\n"
                                 "{\n"
                                 "    background-color: #302F2F;\n"
                                 "    border: 1px transparent black;\n"
                                 "}\n"
                                 "\n"
                                 "QToolBar {\n"
                                 "    border: 1px transparent #393838;\n"
                                 "    background: 1px solid #302F2F;\n"
                                 "    font-weight: bold;\n"
                                 "}\n"
                                 "\n"
                                 "QToolBar::handle:horizontal {\n"
                                 "    image: url(:/dark_blue/img/Hmovetoolbar.png);\n"
                                 "}\n"
                                 "QToolBar::handle:vertical {\n"
                                 "    image: url(:/dark_blue/img/Vmovetoolbar.png);\n"
                                 "}\n"
                                 "QToolBar::separator:horizontal {\n"
                                 "    image: url(:/dark_blue/img/Hsepartoolbar.png);\n"
                                 "}\n"
                                 "QToolBar::separator:vertical {\n"
                                 "    image: url(:/dark_blue/img/Vsepartoolbars.png);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton\n"
                                 "{\n"
                                 "    color: white;\n"
                                 "    background-color: white;\n"
                                 "    border-width: 1px;\n"
                                 "    border-color: qlineargradient(x1: 0, x2: 1, stop: 0  #f3f4f8, stop: 1 #5b5d6d);\n"
                                 "    border-style: solid;\n"
                                 "    padding-top: 2px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    border-radius: 1px;\n"
                                 "    /* outline: none; */\n"
                                 "    /* min-width: 40px; */\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:disabled\n"
                                 "{\n"
                                 "    background-color: black;\n"
                                 "    border-width: 2px;\n"
                                 "    border-color: #3A3939;\n"
                                 "    border-style: solid;\n"
                                 "    padding-top: 2px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    /*border-radius: 2px;*/\n"
                                 "    color: #808080;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:focus {\n"
                                 "    background-color: #3d8ec9;\n"
                                 "    color: white;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox\n"
                                 "{\n"
                                 "    selection-background-color: #3d8ec9;\n"
                                 "    background-color: #201F1F;\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    border-radius: 2px;\n"
                                 "    padding: 2px;\n"
                                 "    min-width: 75px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:checked{\n"
                                 "    background-color: #4A4949;\n"
                                 "    border-color: #6A6969;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    border: 2px solid #78879b;\n"
                                 "    color: silver;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:hover, QAbstractSpinBox:hover,"
                                 "QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,"
                                 "QAbstractView:hover,QTreeView:hover\n"
                                 "{\n"
                                 "    border: 1px solid #78879b;\n"
                                 "    color: silver;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:on\n"
                                 "{\n"
                                 "    background-color: #626873;\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-left: 4px;\n"
                                 "    selection-background-color: #4a4a4a;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView\n"
                                 "{\n"
                                 "    background-color: #201F1F;\n"
                                 "    border-radius: 2px;\n"
                                 "    border: 1px solid #444;\n"
                                 "    selection-background-color: #3d8ec9;\n"
                                 "    color: silver;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down\n"
                                 "{\n"
                                 "    subcontrol-origin: padding;\n"
                                 "    subcontrol-position: top right;\n"
                                 "    width: 15px;\n"
                                 "\n"
                                 "    border-left-width: 0px;\n"
                                 "    border-left-color: darkgray;\n"
                                 "    border-left-style: solid;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    border-bottom-right-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::down-arrow\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
                                 "QComboBox::down-arrow:focus\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed\n"
                                 "{\n"
                                 "    background-color: #484846;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox {\n"
                                 "    padding-top: 2px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    background-color: #201F1F;\n"
                                 "    color: silver;\n"
                                 "    border-radius: 2px;\n"
                                 "    min-width: 75px;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox:up-button\n"
                                 "{\n"
                                 "    background-color: transparent;\n"
                                 "    subcontrol-origin: border;\n"
                                 "    subcontrol-position: top right;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox:down-button\n"
                                 "{\n"
                                 "    background-color: transparent;\n"
                                 "    subcontrol-origin: border;\n"
                                 "    subcontrol-position: bottom right;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox::up-arrow,"
                                 "QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {\n"
                                 "    image: url(:/dark_blue/img/up_arrow_disabled.png);\n"
                                 "    width: 10px;\n"
                                 "    height: 10px;\n"
                                 "}\n"
                                 "QAbstractSpinBox::up-arrow:hover\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/up_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QAbstractSpinBox::down-arrow,"
                                 "QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/down_arrow_disabled.png);\n"
                                 "    width: 10px;\n"
                                 "    height: 10px;\n"
                                 "}\n"
                                 "QAbstractSpinBox::down-arrow:hover\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QLabel\n"
                                 "{\n"
                                 "    border: 0px solid black;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget{\n"
                                 "    border: 1px transparent black;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::pane {\n"
                                 "    border: 1px solid #444;\n"
                                 "    border-radius: 3px;\n"
                                 "    padding: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar\n"
                                 "{\n"
                                 "    qproperty-drawBase: 0;\n"
                                 "    left: 5px; /* move to the right by 5px */\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar:focus\n"
                                 "{\n"
                                 "    border: 0px transparent black;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::close-button  {\n"
                                 "    image: url(:/dark_blue/img/close.png);\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::close-button:hover\n"
                                 "{\n"
                                 "    image: url(:/dark_blue/img/close-hover.png);\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::close-button:pressed {\n"
                                 "    image: url(:/dark_blue/img/close-pressed.png);\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "/* TOP TABS */\n"
                                 "QTabBar::tab:top {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #4A4949;\n"
                                 "    border-bottom: 1px transparent black;\n"
                                 "    background-color: #302F2F;\n"
                                 "    padding: 5px;\n"
                                 "    border-top-left-radius: 2px;\n"
                                 "    border-top-right-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:top:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #201F1F;\n"
                                 "    border: 1px transparent #4A4949;\n"
                                 "    border-bottom: 1px transparent #4A4949;\n"
                                 "    border-top-left-radius: 0px;\n"
                                 "    border-top-right-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:top:!selected:hover {\n"
                                 "    background-color: #48576b;\n"
                                 "}\n"
                                 "\n"
                                 "/* BOTTOM TABS */\n"
                                 "QTabBar::tab:bottom {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #4A4949;\n"
                                 "    border-top: 1px transparent black;\n"
                                 "    background-color: #302F2F;\n"
                                 "    padding: 5px;\n"
                                 "    border-bottom-left-radius: 2px;\n"
                                 "    border-bottom-right-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:bottom:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #201F1F;\n"
                                 "    border: 1px transparent #4A4949;\n"
                                 "    border-top: 1px transparent #4A4949;\n"
                                 "    border-bottom-left-radius: 0px;\n"
                                 "    border-bottom-right-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:bottom:!selected:hover {\n"
                                 "    background-color: #78879b;\n"
                                 "}\n"
                                 "\n"
                                 "/* LEFT TABS */\n"
                                 "QTabBar::tab:left {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #4A4949;\n"
                                 "    border-left: 1px transparent black;\n"
                                 "    background-color: #302F2F;\n"
                                 "    padding: 5px;\n"
                                 "    border-top-right-radius: 2px;\n"
                                 "    border-bottom-right-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:left:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #201F1F;\n"
                                 "    border: 1px transparent #4A4949;\n"
                                 "    border-right: 1px transparent #4A4949;\n"
                                 "    border-top-right-radius: 0px;\n"
                                 "    border-bottom-right-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:left:!selected:hover {\n"
                                 "    background-color: #48576b;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "/* RIGHT TABS */\n"
                                 "QTabBar::tab:right {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #4A4949;\n"
                                 "    border-right: 1px transparent black;\n"
                                 "    background-color: #302F2F;\n"
                                 "    padding: 5px;\n"
                                 "    border-top-left-radius: 2px;\n"
                                 "    border-bottom-left-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:right:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #201F1F;\n"
                                 "    border: 1px transparent #4A4949;\n"
                                 "    border-right: 1px transparent #4A4949;\n"
                                 "    border-top-left-radius: 0px;\n"
                                 "    border-bottom-left-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:right:!selected:hover {\n"
                                 "    background-color: #48576b;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar QToolButton::right-arrow:enabled {\n"
                                 "     image: url(:/dark_blue/img/right_arrow.png);\n"
                                 " }\n"
                                 "\n"
                                 " QTabBar QToolButton::left-arrow:enabled {\n"
                                 "     image: url(:/dark_blue/img/left_arrow.png);\n"
                                 " }\n"
                                 "\n"
                                 "QTabBar QToolButton::right-arrow:disabled {\n"
                                 "     image: url(:/dark_blue/img/right_arrow_disabled.png);\n"
                                 " }\n"
                                 "\n"
                                 " QTabBar QToolButton::left-arrow:disabled {\n"
                                 "     image: url(:/dark_blue/img/left_arrow_disabled.png);\n"
                                 " }\n"
                                 "\n"
                                 "\n"
                                 "QDockWidget {\n"
                                 "    border: 1px solid #403F3F;\n"
                                 "    titlebar-close-icon: url(:/dark_blue/img/close.png);\n"
                                 "    titlebar-normal-icon: url(:/dark_blue/img/undock.png);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button, QDockWidget::float-button {\n"
                                 "    border: 1px solid transparent;\n"
                                 "    border-radius: 2px;\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:hover, QDockWidget::float-button:hover {\n"
                                 "    background: rgba(255, 255, 255, 10);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {\n"
                                 "    padding: 1px -1px -1px 1px;\n"
                                 "    background: rgba(255, 255, 255, 10);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {\n"
                                 "    border: 1px solid #444;\n"
                                 "    background-color: silver;\n"
                                 "    border-radius: 3px;\n"
                                 "    margin-left: 3px;\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView:branch:selected, QTreeView:branch:hover {\n"
                                 "    background: url(:/dark_blue/img/transparent.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:has-siblings:!adjoins-item {\n"
                                 "    border-image: url(:/dark_blue/img/transparent.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:has-siblings:adjoins-item {\n"
                                 "    border-image: url(:/dark_blue/img/transparent.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:!has-children:!has-siblings:adjoins-item {\n"
                                 "    border-image: url(:/dark_blue/img/transparent.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:has-children:!has-siblings:closed,\n"
                                 "QTreeView::branch:closed:has-children:has-siblings {\n"
                                 "    image: url(:/dark_blue/img/branch_closed.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:open:has-children:!has-siblings,\n"
                                 "QTreeView::branch:open:has-children:has-siblings  {\n"
                                 "    image: url(:/dark_blue/img/branch_open.png);\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView::branch:has-children:!has-siblings:closed:hover,\n"
                                 "QTreeView::branch:closed:has-children:has-siblings:hover {\n"
                                 "    image: url(:/dark_blue/img/branch_closed-on.png);\n"
                                 "    }\n"
                                 "\n"
                                 "QTreeView::branch:open:has-children:!has-siblings:hover,\n"
                                 "QTreeView::branch:open:has-children:has-siblings:hover  {\n"
                                 "    image: url(:/dark_blue/img/branch_open-on.png);\n"
                                 "    }\n"
                                 "\n"
                                 "QListView::item:!selected:hover,"
                                 " QListView::item:!selected:hover, QTreeView::item:!selected:hover  {\n"
                                 "    background: rgba(0, 0, 0, 0);\n"
                                 "    outline: 0;\n"
                                 "    color: #FFFFFF\n"
                                 "}\n"
                                 "\n"
                                 "QListView::item:selected:hover,"
                                 " QListView::item:selected:hover, QTreeView::item:selected:hover  {\n"
                                 "    background: #3d8ec9;\n"
                                 "    color: #FFFFFF;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:horizontal {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    height: 8px;\n"
                                 "    background: #201F1F;\n"
                                 "    margin: 2px 0;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal {\n"
                                 "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 14px;\n"
                                 "    height: 14px;\n"
                                 "    margin: -4px 0;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:vertical {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 8px;\n"
                                 "    background: #201F1F;\n"
                                 "    margin: 0 0px;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:vertical {\n"
                                 "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
                                 "    stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 14px;\n"
                                 "    height: 14px;\n"
                                 "    margin: 0 -4px;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton {\n"
                                 "    /*  background-color: transparent; */\n"
                                 "    border: 2px transparent #4A4949;\n"
                                 "    border-radius: 4px;\n"
                                 "    background-color: dimgray;\n"
                                 "    margin: 2px;\n"
                                 "    padding: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton[popupMode=\"1\"] { /* only for MenuButtonPopup */\n"
                                 " padding-right: 20px; /* make way for the popup button */\n"
                                 " border: 2px transparent #4A4949;\n"
                                 " border-radius: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton[popupMode=\"2\"] { /* only for InstantPopup */\n"
                                 " padding-right: 10px; /* make way for the popup button */\n"
                                 " border: 2px transparent #4A4949;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QToolButton:hover, QToolButton::menu-button:hover {\n"
                                 "    border: 2px solid #78879b;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton:checked, QToolButton:pressed,\n"
                                 "    QToolButton::menu-button:pressed {\n"
                                 "    background-color: #4A4949;\n"
                                 "    border: 2px solid #78879b;\n"
                                 "}\n"
                                 "\n"
                                 "/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */\n"
                                 "QToolButton::menu-indicator {\n"
                                 "    image: url(:/dark_blue/img/down_arrow.png);\n"
                                 "    top: -7px; left: -2px; /* shift it a bit */\n"
                                 "}\n"
                                 "\n"
                                 "/* the subcontrols below are used only in the MenuButtonPopup mode */\n"
                                 "QToolButton::menu-button {\n"
                                 "    border: 1px transparent #4A4949;\n"
                                 "    border-top-right-radius: 6px;\n"
                                 "    border-bottom-right-radius: 6px;\n"
                                 "    /* 16px width + 4px for border = 20px allocated above */\n"
                                 "    width: 16px;\n"
                                 "    outline: none;\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton::menu-arrow {\n"
                                 "    image: url(:/dark_blue/img/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QToolButton::menu-arrow:open {\n"
                                 "    top: 1px; left: 1px; /* shift it a bit */\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton::menu-indicator  {\n"
                                 "    subcontrol-origin: padding;\n"
                                 "    subcontrol-position: bottom right;\n"
                                 "    left: 4px;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView\n"
                                 "{\n"
                                 "    border: 1px solid #444;\n"
                                 "    gridline-color: #6c6c6c;\n"
                                 "    background-color: #201F1F;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableView, QHeaderView\n"
                                 "{\n"
                                 "    border-radius: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {\n"
                                 "    background: #78879b;\n"
                                 "    color: #FFFFFF;\n"
                                 "}\n"
                                 "\n"
                                 "QTableView::item:selected:active,"
                                 " QTreeView::item:selected:active, QListView::item:selected:active  {\n"
                                 "    background: #3d8ec9;\n"
                                 "    color: #FFFFFF;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView\n"
                                 "{\n"
                                 "    border: 1px transparent;\n"
                                 "    border-radius: 2px;\n"
                                 "    margin: 0px;\n"
                                 "    padding: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section  {\n"
                                 "    background-color: #3A3939;\n"
                                 "    color: silver;\n"
                                 "    padding: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "    border-radius: 0px;\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one\n"
                                 "{\n"
                                 "    border-top: 1px solid #6c6c6c;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section::vertical\n"
                                 "{\n"
                                 "    border-top: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one\n"
                                 "{\n"
                                 "    border-left: 1px solid #6c6c6c;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section::horizontal\n"
                                 "{\n"
                                 "    border-left: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QHeaderView::section:checked\n"
                                 " {\n"
                                 "    color: white;\n"
                                 "    background-color: #5A5959;\n"
                                 " }\n"
                                 "\n"
                                 " /* style the sort indicator */\n"
                                 "QHeaderView::down-arrow {\n"
                                 "    image: url(:/dark_blue/img/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::up-arrow {\n"
                                 "    image: url(:/dark_blue/img/up_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QTableCornerButton::section {\n"
                                 "    background-color: #3A3939;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QToolBox  {\n"
                                 "    padding: 3px;\n"
                                 "    border: 1px transparent black;\n"
                                 "}\n"
                                 "\n"
                                 "QToolBox::tab {\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #302F2F;\n"
                                 "    border: 1px solid #4A4949;\n"
                                 "    border-bottom: 1px transparent #302F2F;\n"
                                 "    border-top-left-radius: 5px;\n"
                                 "    border-top-right-radius: 5px;\n"
                                 "}\n"
                                 "\n"
                                 " QToolBox::tab:selected { /* italicize selected tabs */\n"
                                 "    font: italic;\n"
                                 "    background-color: #302F2F;\n"
                                 "    border-color: #3d8ec9;\n"
                                 " }\n"
                                 "\n"
                                 "QStatusBar::item {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    border-radius: 2px;\n"
                                 " }\n"
                                 "\n"
                                 "\n"
                                 "QFrame[height=\"3\"], QFrame[width=\"3\"] {\n"
                                 "    background-color: #AAA;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QSplitter::handle {\n"
                                 "    border: 1px dashed #3A3939;\n"
                                 "}\n"
                                 "\n"
                                 "QSplitter::handle:hover {\n"
                                 "    background-color: #787876;\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "}\n"
                                 "\n"
                                 "QSplitter::handle:horizontal {\n"
                                 "    width: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QSplitter::handle:vertical {\n"
                                 "    height: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QListWidget {\n"
                                 "    background-color: silver;\n"
                                 "    border-radius: 5px;\n"
                                 "    margin-left: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QListWidget::item {\n"
                                 "    color: black;\n"
                                 "}\n"
                                 "\n"
                                 "QMessageBox {\n"
                                 "    messagebox-critical-icon    : url(:/dark_blue/img/critical.png);\n"
                                 "    messagebox-information-icon    : url(:/dark_blue/img/information.png);\n"
                                 "    messagebox-question-icon    : url(:/dark_blue/img/question.png);\n"
                                 "    messagebox-warning-icon:    : url(:/dark_blue/img/warning.png);\n"
                                 "}\n"
                                 "\n"
                                 "ColorButton::enabled {\n"
                                 "    border-radius: 0px;\n"
                                 "    border: 1px solid #444444;\n"
                                 "}\n"
                                 "\n"
                                 "ColorButton::disabled {\n"
                                 "    border-radius: 0px;\n"
                                 "    border: 1px solid #AAAAAA;\n"
                                 "}")
        MainWindow.setIconSize(QtCore.QSize(330, 303))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setMaximumSize(QtCore.QSize(1920, 1080))
        self.centralwidget.setStyleSheet("background-color: #404252;")
        self.centralwidget.setMouseTracking(True)
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(1)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(1)

        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        # self.stackedWidget.setGeometry(QtCore.QRect(240, 0, 1731, 1081))
        self.stackedWidget.setGeometry(QtCore.QRect(266, 5, 1631, 950))
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet("background-color:  #282a3a ;border-radius : 1px;")
        self.stackedWidget.setGraphicsEffect(shadow)
        # background - color: qlineargradient(x1: 0, x2: 1, stop: 0  # 455A64, stop: 1 #F78361);

        self.home_widget = QtWidgets.QWidget()
        self.home_widget.setObjectName("home_widget")

        self.Home_Project_Name_Line = QtWidgets.QLineEdit(self.home_widget)
        self.Home_Project_Name_Line.setGeometry(QtCore.QRect(625, 550, 300, 22))
        self.Home_Project_Name_Line.setObjectName("Home_Project_Name_Line")

        self.logo2 = QPixmap('icons/logo3.png')
        self.label_center4 = QtWidgets.QLabel(self.home_widget)
        self.label_center4.setGeometry(QtCore.QRect(650, 100, 250, 250))
        self.label_center4.setObjectName("label_2")
        self.label_center4.setStyleSheet("background:transparent;")
        self.label_center4.setPixmap(self.logo2)
        self.label_center4.setScaledContents(True)

        self.label_center5 = QtWidgets.QLabel("     Please enter the project name \n"
                                              "to create a project file on the desktop", self.home_widget)
        self.label_center5.setGeometry(QtCore.QRect(670, 490, 300, 35))
        self.label_center5.setStyleSheet("background:transparent;")

        self.pushButton_3 = QtWidgets.QPushButton(self.home_widget)
        self.pushButton_3.setGeometry(QtCore.QRect(725, 600, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget.addWidget(self.home_widget)
        self.resize_widget = QtWidgets.QWidget()
        self.resize_widget.setObjectName("resize_widget")

        self.open_button_resize = QtWidgets.QPushButton(self.resize_widget)
        self.open_button_resize.setGeometry(QtCore.QRect(140, 40, 93, 28))
        self.open_button_resize.setObjectName("open_button_resize")

        self.save_button_resize = QtWidgets.QPushButton("Save Path", self.resize_widget)
        self.save_button_resize.setGeometry(QtCore.QRect(570, 40, 93, 28))
        self.save_button_resize.setObjectName("open_button_resize")

        self.width_resize_text = QtWidgets.QLineEdit(self.resize_widget)
        self.width_resize_text.setGeometry(QtCore.QRect(260, 40, 71, 31))
        self.width_resize_text.setObjectName("width_resize_text")

        self.width_resize_label = QtWidgets.QLabel(self.resize_widget)
        self.width_resize_label.setGeometry(QtCore.QRect(280, 20, 41, 16))
        self.width_resize_label.setObjectName("width_resize_label")

        self.height_resize_text = QtWidgets.QLineEdit(self.resize_widget)
        self.height_resize_text.setGeometry(QtCore.QRect(350, 40, 71, 31))
        self.height_resize_text.setObjectName("height_resize_text")

        self.height_resize_label = QtWidgets.QLabel(self.resize_widget)
        self.height_resize_label.setGeometry(QtCore.QRect(370, 20, 41, 16))
        self.height_resize_label.setObjectName("height_resize_label")

        self.preview_button_resize = QtWidgets.QPushButton(self.resize_widget)
        self.preview_button_resize.setGeometry(QtCore.QRect(480, 40, 31, 28))
        self.preview_button_resize.setText("")
        self.preview_button_resize.setObjectName("preview_button_resize")
        self.preview_resize_label = QtWidgets.QLabel(self.resize_widget)
        self.preview_resize_label.setGeometry(QtCore.QRect(470, 20, 51, 16))
        self.preview_resize_label.setObjectName("preview_resize_label")
        self.run_button_resize = QtWidgets.QPushButton(self.resize_widget)
        self.run_button_resize.setGeometry(QtCore.QRect(690, 40, 93, 28))
        self.run_button_resize.setObjectName("run_button_resize")
        self.progressBar_resize = QtWidgets.QProgressBar(self.resize_widget)
        self.progressBar_resize.setGeometry(QtCore.QRect(820, 40, 118, 23))
        self.progressBar_resize.setProperty("value", 24)
        self.progressBar_resize.setObjectName("progressBar_resize")
        self.info_resize_box = QtWidgets.QLabel(self.resize_widget)
        self.info_resize_box.setGeometry(QtCore.QRect(1180, 10, 291, 61))
        self.info_resize_box.setObjectName("info_resize_box")
        self.info_resize_box.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_resize_label = QtWidgets.QLabel(self.resize_widget)
        self.info_resize_label.setGeometry(QtCore.QRect(1150, 30, 31, 16))
        self.info_resize_label.setObjectName("info_resize_label")

        self.layout_resize = QtWidgets.QLabel(self.resize_widget)
        self.layout_resize.setGeometry(QtCore.QRect(10, 80, 1600, 800))
        self.layout_resize.setObjectName("layout_resize")
        self.layout_resize.setStyleSheet(" border: 1px solid black;border-radius : 1px; ")

        self.stackedWidget.addWidget(self.resize_widget)
        self.crop_widget = QtWidgets.QWidget()
        self.crop_widget.setObjectName("crop_widget")
        self.info_crop_label_2 = QtWidgets.QLabel(self.crop_widget)
        self.info_crop_label_2.setGeometry(QtCore.QRect(1150, 30, 31, 16))
        self.info_crop_label_2.setObjectName("info_crop_label_2")
        self.xmin_crop_text_2 = QtWidgets.QLineEdit(self.crop_widget)
        self.xmin_crop_text_2.setGeometry(QtCore.QRect(200, 40, 41, 31))
        self.xmin_crop_text_2.setObjectName("xmin_crop_text_2")
        self.run_button_crop_2 = QtWidgets.QPushButton(self.crop_widget)
        self.run_button_crop_2.setGeometry(QtCore.QRect(690, 40, 93, 28))
        self.run_button_crop_2.setObjectName("run_button_crop_2")
        self.save_button_crop = QtWidgets.QPushButton("Save Path", self.crop_widget)
        self.save_button_crop.setGeometry(QtCore.QRect(570, 40, 93, 28))
        self.save_button_crop.setObjectName("open_button_resize")
        self.open_button_crop_2 = QtWidgets.QPushButton(self.crop_widget)
        self.open_button_crop_2.setGeometry(QtCore.QRect(70, 40, 93, 28))
        self.open_button_crop_2.setObjectName("open_button_crop_2")
        self.ymin_crop_label_2 = QtWidgets.QLabel(self.crop_widget)
        self.ymin_crop_label_2.setGeometry(QtCore.QRect(260, 20, 41, 16))
        self.ymin_crop_label_2.setObjectName("ymin_crop_label_2")
        self.preview_button_crop_2 = QtWidgets.QPushButton(self.crop_widget)
        self.preview_button_crop_2.setGeometry(QtCore.QRect(480, 40, 31, 28))
        self.preview_button_crop_2.setText("")
        self.preview_button_crop_2.setObjectName("preview_button_crop_2")

        self.info_crop_box_2 = QtWidgets.QLabel(self.crop_widget)
        self.info_crop_box_2.setGeometry(QtCore.QRect(1180, 10, 291, 61))
        self.info_crop_box_2.setObjectName("info_crop_box_2")
        self.info_crop_box_2.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.preview_crop_label_2 = QtWidgets.QLabel(self.crop_widget)
        self.preview_crop_label_2.setGeometry(QtCore.QRect(470, 20, 51, 16))
        self.preview_crop_label_2.setObjectName("preview_crop_label_2")
        self.progressBar_crop_2 = QtWidgets.QProgressBar(self.crop_widget)
        self.progressBar_crop_2.setGeometry(QtCore.QRect(820, 40, 118, 23))
        self.progressBar_crop_2.setProperty("value", 24)
        self.progressBar_crop_2.setObjectName("progressBar_crop_2")
        self.xmin_crop_label_2 = QtWidgets.QLabel(self.crop_widget)
        self.xmin_crop_label_2.setGeometry(QtCore.QRect(200, 20, 41, 16))
        self.xmin_crop_label_2.setObjectName("xmin_crop_label_2")

        self.layout_crop = QtWidgets.QLabel(self.crop_widget)
        self.layout_crop.setGeometry(QtCore.QRect(10, 80, 1600, 800))
        self.layout_crop.setObjectName("layout_resize")
        self.layout_crop.setStyleSheet(" border: 1px solid black;border-radius : 1px; ")

        self.ymin_crop_text_2 = QtWidgets.QLineEdit(self.crop_widget)
        self.ymin_crop_text_2.setGeometry(QtCore.QRect(260, 40, 41, 31))
        self.ymin_crop_text_2.setObjectName("ymin_crop_text_2")

        self.ymax_crop_text_3 = QtWidgets.QLineEdit(self.crop_widget)
        self.ymax_crop_text_3.setGeometry(QtCore.QRect(390, 40, 41, 31))
        self.ymax_crop_text_3.setObjectName("ymax_crop_text_3")

        self.xmax_crop_label_3 = QtWidgets.QLabel(self.crop_widget)
        self.xmax_crop_label_3.setGeometry(QtCore.QRect(330, 20, 41, 16))
        self.xmax_crop_label_3.setObjectName("xmax_crop_label_3")

        self.ymax_crop_label_3 = QtWidgets.QLabel(self.crop_widget)
        self.ymax_crop_label_3.setGeometry(QtCore.QRect(390, 20, 41, 16))
        self.ymax_crop_label_3.setObjectName("ymax_crop_label_3")

        self.xmax_crop_text_3 = QtWidgets.QLineEdit(self.crop_widget)
        self.xmax_crop_text_3.setGeometry(QtCore.QRect(330, 40, 41, 31))
        self.xmax_crop_text_3.setObjectName("xmax_crop_text_3")

        self.stackedWidget.addWidget(self.crop_widget)
        self.rotate_widget = QtWidgets.QWidget()
        self.rotate_widget.setObjectName("rotate_widget")
        self.info_rotate_label_3 = QtWidgets.QLabel(self.rotate_widget)
        self.info_rotate_label_3.setGeometry(QtCore.QRect(1150, 30, 31, 16))
        self.info_rotate_label_3.setObjectName("info_rotate_label_3")

        self.open_button_rotate_3 = QtWidgets.QPushButton(self.rotate_widget)
        self.open_button_rotate_3.setGeometry(QtCore.QRect(70, 40, 93, 28))
        self.open_button_rotate_3.setObjectName("open_button_rotate_3")

        self.save_button_rotate = QtWidgets.QPushButton("Save Path", self.rotate_widget)
        self.save_button_rotate.setGeometry(QtCore.QRect(570, 40, 93, 28))
        self.save_button_rotate.setObjectName("open_button_resize")

        self.info_rotate_box_3 = QtWidgets.QLabel(self.rotate_widget)
        self.info_rotate_box_3.setGeometry(QtCore.QRect(1180, 10, 291, 61))
        self.info_rotate_box_3.setObjectName("info_rotate_box_3")
        self.info_rotate_box_3.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.angle_rotate_label_3 = QtWidgets.QLabel(self.rotate_widget)
        self.angle_rotate_label_3.setGeometry(QtCore.QRect(200, 20, 41, 16))
        self.angle_rotate_label_3.setObjectName("angle_rotate_label_3")
        self.progressBar_rotate_3 = QtWidgets.QProgressBar(self.rotate_widget)
        self.progressBar_rotate_3.setGeometry(QtCore.QRect(820, 40, 118, 23))
        self.progressBar_rotate_3.setProperty("value", 24)
        self.progressBar_rotate_3.setObjectName("progressBar_rotate_3")

        self.angle_rotate_text_3 = QtWidgets.QLineEdit(self.rotate_widget)
        self.angle_rotate_text_3.setGeometry(QtCore.QRect(200, 40, 41, 31))
        self.angle_rotate_text_3.setObjectName("angle_rotate_text_3")

        self.layout_rotate = QtWidgets.QLabel(self.rotate_widget)
        self.layout_rotate.setGeometry(QtCore.QRect(10, 80, 1600, 800))
        self.layout_rotate.setObjectName("layout_rotate")
        self.layout_rotate.setStyleSheet(" border: 1px solid black; border-radius : 1px; ")

        self.preview_button_rotate_3 = QtWidgets.QPushButton(self.rotate_widget)
        self.preview_button_rotate_3.setGeometry(QtCore.QRect(480, 40, 31, 28))
        self.preview_button_rotate_3.setText("")
        self.preview_button_rotate_3.setObjectName("preview_button_rotate_3")

        self.run_button_rotate_3 = QtWidgets.QPushButton(self.rotate_widget)
        self.run_button_rotate_3.setGeometry(QtCore.QRect(690, 40, 93, 28))
        self.run_button_rotate_3.setObjectName("run_button_rotate_3")

        self.preview_rotate_label_4 = QtWidgets.QLabel(self.rotate_widget)
        self.preview_rotate_label_4.setGeometry(QtCore.QRect(470, 20, 51, 16))
        self.preview_rotate_label_4.setObjectName("preview_rotate_label_4")

        self.preview_rotate_label_5 = QtWidgets.QLabel(self.rotate_widget)
        self.preview_rotate_label_5.setGeometry(QtCore.QRect(1630, 1030, 51, 16))
        self.preview_rotate_label_5.setObjectName("preview_rotate_label_5")

        self.stackedWidget.addWidget(self.rotate_widget)
        self.brig_widget = QtWidgets.QWidget()
        self.brig_widget.setObjectName("brig_widget")

        self.run_button_brig_4 = QtWidgets.QPushButton(self.brig_widget)
        self.run_button_brig_4.setGeometry(QtCore.QRect(690, 40, 93, 28))
        self.run_button_brig_4.setObjectName("run_button_brig_4")

        self.save_button_brig = QtWidgets.QPushButton("Save Path", self.brig_widget)
        self.save_button_brig.setGeometry(QtCore.QRect(570, 40, 93, 28))
        self.save_button_brig.setObjectName("open_button_resize")

        self.open_button_brig_4 = QtWidgets.QPushButton(self.brig_widget)
        self.open_button_brig_4.setGeometry(QtCore.QRect(70, 40, 93, 28))
        self.open_button_brig_4.setObjectName("open_button_brig_4")

        self.preview_button_brig_4 = QtWidgets.QPushButton(self.brig_widget)
        self.preview_button_brig_4.setGeometry(QtCore.QRect(480, 40, 31, 28))
        self.preview_button_brig_4.setText("")
        self.preview_button_brig_4.setObjectName("preview_button_brig_4")

        self.info_brig_box_4 = QtWidgets.QLabel(self.brig_widget)
        self.info_brig_box_4.setGeometry(QtCore.QRect(1180, 10, 291, 61))
        self.info_brig_box_4.setObjectName("info_brig_box_4")
        self.info_brig_box_4.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.progressBar_brig_4 = QtWidgets.QProgressBar(self.brig_widget)
        self.progressBar_brig_4.setGeometry(QtCore.QRect(820, 40, 118, 23))
        self.progressBar_brig_4.setProperty("value", 24)
        self.progressBar_brig_4.setObjectName("progressBar_brig_4")

        self.layout_brig = QtWidgets.QLabel(self.brig_widget)
        self.layout_brig.setGeometry(QtCore.QRect(10, 80, 1600, 800))
        self.layout_brig.setObjectName("layout_rotate")
        self.layout_brig.setStyleSheet(" border: 1px solid black; border-radius : 1px;")

        self.preview_brig_label_6 = QtWidgets.QLabel(self.brig_widget)
        self.preview_brig_label_6.setGeometry(QtCore.QRect(470, 20, 51, 16))
        self.preview_brig_label_6.setObjectName("preview_brig_label_6")

        self.info_brig_label_4 = QtWidgets.QLabel(self.brig_widget)
        self.info_brig_label_4.setGeometry(QtCore.QRect(1150, 30, 31, 16))
        self.info_brig_label_4.setObjectName("info_brig_label_4")

        self.brig_brig_label_4 = QtWidgets.QLabel(self.brig_widget)
        self.brig_brig_label_4.setGeometry(QtCore.QRect(190, 20, 81, 20))
        self.brig_brig_label_4.setObjectName("brig_brig_label_4")

        self.preview_brig_label_7 = QtWidgets.QLabel(self.brig_widget)
        self.preview_brig_label_7.setGeometry(QtCore.QRect(1630, 1030, 51, 16))
        self.preview_brig_label_7.setObjectName("preview_brig_label_7")

        self.brig_brig_text_4 = QtWidgets.QLineEdit(self.brig_widget)
        self.brig_brig_text_4.setGeometry(QtCore.QRect(200, 40, 41, 31))
        self.brig_brig_text_4.setObjectName("brig_brig_text_4")
        self.stackedWidget.addWidget(self.brig_widget)
        self.label_widget = QtWidgets.QWidget()
        self.label_widget.setObjectName("label_widget")

        self.open_button_ann_5 = QtWidgets.QPushButton(self.label_widget)
        self.open_button_ann_5.setGeometry(QtCore.QRect(70, 40, 93, 28))
        self.open_button_ann_5.setObjectName("open_button_ann_5")

        self.preview_button_ann_5 = QtWidgets.QPushButton(self.label_widget)
        self.preview_button_ann_5.setGeometry(QtCore.QRect(350, 40, 31, 28))
        self.preview_button_ann_5.setText("")
        self.preview_button_ann_5.setObjectName("preview_button_ann_5")

        self.run_button_ann_5 = QtWidgets.QPushButton(self.label_widget)
        self.run_button_ann_5.setGeometry(QtCore.QRect(690, 40, 93, 28))
        self.run_button_ann_5.setObjectName("run_button_ann_5")

        self.info_ann_box_12 = QtWidgets.QLabel(self.label_widget)
        self.info_ann_box_12.setGeometry(QtCore.QRect(1180, 10, 291, 61))
        self.info_ann_box_12.setObjectName("info_ann_box_5")
        self.info_ann_box_12.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_box_13 = QtWidgets.QLabel(self.label_widget)
        self.info_ann_box_13.setGeometry(QtCore.QRect(1180, 40, 97, 31))
        self.info_ann_box_13.setObjectName("info_ann_box_5")
        self.info_ann_box_13.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_box_14 = QtWidgets.QLabel(self.label_widget)
        self.info_ann_box_14.setGeometry(QtCore.QRect(1277, 40, 137, 31))
        self.info_ann_box_14.setObjectName("info_ann_box_5")
        self.info_ann_box_14.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_box_15 = QtWidgets.QLabel(self.label_widget)
        self.info_ann_box_15.setGeometry(QtCore.QRect(1414, 40, 57, 31))
        self.info_ann_box_15.setObjectName("info_ann_box_5")
        self.info_ann_box_15.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_box_16 = QtWidgets.QLabel("    Name", self.label_widget)
        self.info_ann_box_16.setGeometry(QtCore.QRect(1180, 10, 97, 31))
        self.info_ann_box_16.setObjectName("info_ann_box_5")
        self.info_ann_box_16.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_box_17 = QtWidgets.QLabel("        Cordinates", self.label_widget)
        self.info_ann_box_17.setGeometry(QtCore.QRect(1277, 10, 137, 31))
        self.info_ann_box_17.setObjectName("info_ann_box_5")
        self.info_ann_box_17.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_box_18 = QtWidgets.QLabel("  Total", self.label_widget)
        self.info_ann_box_18.setGeometry(QtCore.QRect(1414, 10, 57, 31))
        self.info_ann_box_18.setObjectName("info_ann_box_5")
        self.info_ann_box_18.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.label_widget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 80, 12, 12))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")

        self.layout_ann_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.layout_ann_5.setContentsMargins(0, 0, 0, 0)

        self.preview_ann_label_8 = QtWidgets.QLabel(self.label_widget)
        self.preview_ann_label_8.setGeometry(QtCore.QRect(350, 20, 41, 16))
        self.preview_ann_label_8.setObjectName("preview_ann_label_8")

        self.info_ann_label_5 = QtWidgets.QLabel(self.label_widget)
        self.info_ann_label_5.setGeometry(QtCore.QRect(1150, 30, 31, 16))
        self.info_ann_label_5.setObjectName("info_ann_label_5")

        self.ann_ann_label_5 = QtWidgets.QLabel(self.label_widget)
        self.ann_ann_label_5.setGeometry(QtCore.QRect(200, 20, 81, 20))
        self.ann_ann_label_5.setObjectName("ann_ann_label_5")

        self.ann_ann_text_5 = QtWidgets.QLineEdit(self.label_widget)
        self.ann_ann_text_5.setGeometry(QtCore.QRect(200, 40, 81, 31))
        self.ann_ann_text_5.setObjectName("ann_ann_text_5")

        self.preview_ann_label_10 = QtWidgets.QLabel(self.label_widget)
        self.preview_ann_label_10.setGeometry(QtCore.QRect(440, 20, 61, 16))
        self.preview_ann_label_10.setObjectName("preview_ann_label_10")

        self.preview_button_ann_6 = QtWidgets.QPushButton(self.label_widget)
        self.preview_button_ann_6.setGeometry(QtCore.QRect(450, 40, 31, 28))
        self.preview_button_ann_6.setText("")
        self.preview_button_ann_6.setObjectName("preview_button_ann_6")

        self.label = QtWidgets.QLabel(self.label_widget)
        self.label.setGeometry(QtCore.QRect(650, 20, 201, 20))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.label_widget)

        self.seperate_widget = QtWidgets.QWidget()
        self.seperate_widget.setObjectName("seperate_widget")

        self.horizontalSlider = QtWidgets.QSlider(self.seperate_widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(290, 50, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")

        self.label_2 = QtWidgets.QLabel(self.seperate_widget)
        self.label_2.setGeometry(QtCore.QRect(290, 30, 55, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.seperate_widget)
        self.label_3.setGeometry(QtCore.QRect(430, 30, 55, 16))
        self.label_3.setObjectName("label_3")

        self.save_button_split = QtWidgets.QPushButton("Save Path", self.seperate_widget)
        self.save_button_split.setGeometry(QtCore.QRect(510, 40, 93, 28))
        self.save_button_split.setObjectName("open_button_resize")

        self.label_21 = QtWidgets.QLabel(self.seperate_widget)
        self.label_21.setGeometry(QtCore.QRect(310, 15, 55, 16))
        self.label_21.setObjectName("label_2")
        self.label_31 = QtWidgets.QLabel(self.seperate_widget)
        self.label_31.setGeometry(QtCore.QRect(470, 15, 55, 16))
        self.label_31.setObjectName("label_3")

        self.pushButton = QtWidgets.QPushButton(self.seperate_widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.seperate_widget)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 40, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.progressBar = QtWidgets.QProgressBar(self.seperate_widget)
        self.progressBar.setGeometry(QtCore.QRect(750, 40, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.info_ann_box_6 = QtWidgets.QLabel(self.seperate_widget)
        self.info_ann_box_6.setGeometry(QtCore.QRect(1200, 10, 291, 61))
        self.info_ann_box_6.setObjectName("info_ann_box_6")
        self.info_ann_box_6.setStyleSheet("background-color: #a0b1b9; border: 1px solid black; color: black; ")

        self.info_ann_label_6 = QtWidgets.QLabel(self.seperate_widget)
        self.info_ann_label_6.setGeometry(QtCore.QRect(1170, 30, 31, 16))
        self.info_ann_label_6.setObjectName("info_ann_label_6")
        self.stackedWidget.addWidget(self.seperate_widget)

        self.label_center = QtWidgets.QLabel(self.centralwidget)
        self.label_center.setGeometry(QtCore.QRect(5, 5, 249, 950))
        self.label_center.setObjectName("label_2")
        self.label_center.setStyleSheet("background-color: qlineargradient(x1: 0, x2: 1, stop: 0"
                                        " #222016 , stop: 1 #282a3a ); border-radius : 1px;")
        self.label_center.setGraphicsEffect(shadow2)

        self.home_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.home_central_button.setGeometry(QtCore.QRect(20, 150, 211, 41))
        self.home_central_button.setObjectName("home_central_button")
        self.home_central_button.setIcon(QIcon("icons/home.png"))

        self.resize_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.resize_central_button.setGeometry(QtCore.QRect(27, 260, 191, 41))
        self.resize_central_button.setObjectName("resize_central_button")
        self.resize_central_button.setIcon(QIcon("icons/increase.png"))

        self.crop_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.crop_central_button.setGeometry(QtCore.QRect(27, 360, 191, 41))
        self.crop_central_button.setObjectName("crop_central_button")
        self.crop_central_button.setIcon(QIcon("icons/crop.png"))

        self.seperate_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.seperate_central_button.setGeometry(QtCore.QRect(27, 760, 191, 41))
        self.seperate_central_button.setObjectName("seperate_central_button")
        self.seperate_central_button.setIcon(QIcon("icons/split (1).png"))

        self.label_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.label_central_button.setGeometry(QtCore.QRect(27, 660, 191, 41))
        self.label_central_button.setObjectName("label_central_button")
        self.label_central_button.setIcon(QIcon("icons/tag.png"))

        self.brig_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.brig_central_button.setGeometry(QtCore.QRect(27, 560, 191, 41))
        self.brig_central_button.setObjectName("brig_central_button")
        self.brig_central_button.setIcon(QIcon("icons/brightness.png"))

        self.rotate_central_button = QtWidgets.QPushButton(self.centralwidget)
        self.rotate_central_button.setGeometry(QtCore.QRect(27, 460, 191, 41))
        self.rotate_central_button.setObjectName("rotate_central_button")
        self.rotate_central_button.setIcon(QIcon("icons/loading.png"))

        self.dest = QPixmap('icons/arr.png')
        self.label_center2 = QtWidgets.QLabel(self.centralwidget)
        self.label_center2.setGeometry(QtCore.QRect(222, 157, 30, 30))
        self.label_center2.setObjectName("label_2")
        self.label_center2.setStyleSheet("background:transparent;")
        self.label_center2.setPixmap(self.dest)
        self.label_center2.setScaledContents(True)

        self.logo = QPixmap('icons/logo3.png')
        self.label_center3 = QtWidgets.QLabel(self.centralwidget)
        self.label_center3.setGeometry(QtCore.QRect(103, 43, 70, 70))
        self.label_center3.setObjectName("label_2")
        self.label_center3.setStyleSheet("background:transparent;")
        self.label_center3.setPixmap(self.logo)
        self.label_center3.setScaledContents(True)
        self.label_center8 = QtWidgets.QLabel("Created by Hakan Aktaş", self.centralwidget)
        self.label_center8.setGeometry(QtCore.QRect(10, 910, 320, 120))
        self.label_center8.setStyleSheet("background:transparent;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Preparation ToolKit"))
        self.pushButton_3.setText(_translate("MainWindow", "Create"))
        self.open_button_resize.setText(_translate("MainWindow", "Open File"))
        self.width_resize_label.setText(_translate("MainWindow", "Width"))
        self.height_resize_label.setText(_translate("MainWindow", "Height"))
        self.preview_resize_label.setText(_translate("MainWindow", "Preview"))
        self.run_button_resize.setText(_translate("MainWindow", "Run"))
        self.info_resize_label.setText(_translate("MainWindow", "Info:"))
        self.info_crop_label_2.setText(_translate("MainWindow", "Info:"))
        self.run_button_crop_2.setText(_translate("MainWindow", "Run"))
        self.open_button_crop_2.setText(_translate("MainWindow", "Open File"))
        self.ymin_crop_label_2.setText(_translate("MainWindow", "y min"))
        self.preview_crop_label_2.setText(_translate("MainWindow", "Preview"))
        self.xmin_crop_label_2.setText(_translate("MainWindow", "x min"))
        self.xmax_crop_label_3.setText(_translate("MainWindow", "x max"))
        self.ymax_crop_label_3.setText(_translate("MainWindow", "y max"))
        self.info_rotate_label_3.setText(_translate("MainWindow", "Info:"))
        self.open_button_rotate_3.setText(_translate("MainWindow", "Open File"))
        self.angle_rotate_label_3.setText(_translate("MainWindow", "Angle"))
        self.run_button_rotate_3.setText(_translate("MainWindow", "Run"))
        self.preview_rotate_label_4.setText(_translate("MainWindow", "Preview"))
        self.preview_rotate_label_5.setText(_translate("MainWindow", "Preview"))
        self.run_button_brig_4.setText(_translate("MainWindow", "Run"))
        self.open_button_brig_4.setText(_translate("MainWindow", "Open File"))
        self.preview_brig_label_6.setText(_translate("MainWindow", "Preview"))
        self.info_brig_label_4.setText(_translate("MainWindow", "Info:"))
        self.brig_brig_label_4.setText(_translate("MainWindow", "Brigness +/-"))
        self.preview_brig_label_7.setText(_translate("MainWindow", "Preview"))
        self.open_button_ann_5.setText(_translate("MainWindow", "Open File"))
        self.run_button_ann_5.setText(_translate("MainWindow", "Save"))
        self.preview_ann_label_8.setText(_translate("MainWindow", "Label"))
        self.info_ann_label_5.setText(_translate("MainWindow", "Info:"))
        self.ann_ann_label_5.setText(_translate("MainWindow", "Label Name"))
        self.preview_ann_label_10.setText(_translate("MainWindow", "Clear All"))
        self.label.setText(_translate("MainWindow", "To save and open the other image"))
        self.label_2.setText(_translate("MainWindow", "Train"))
        self.label_3.setText(_translate("MainWindow", "Test"))
        self.pushButton.setText(_translate("MainWindow", "Open File"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.info_ann_label_6.setText(_translate("MainWindow", "Info:"))
        self.home_central_button.setText(_translate("MainWindow", "   Home "))
        self.resize_central_button.setText(_translate("MainWindow", "   Resize"))
        self.crop_central_button.setText(_translate("MainWindow", "   Crop "))
        self.seperate_central_button.setText(_translate("MainWindow", "   Seperate "))
        self.label_central_button.setText(_translate("MainWindow", "   Label"))
        self.brig_central_button.setText(_translate("MainWindow", "   Brigtness"))
        self.rotate_central_button.setText(_translate("MainWindow", "   Rotate"))
