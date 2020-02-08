# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtWidgets import QFileDialog
import modules


class Ui_AraProje(object):
    def setupUi(self, AraProje):
        AraProje.setObjectName("AraProje")
        AraProje.resize(1200, 719)
        AraProje.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(AraProje)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 330, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                    "                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                    "                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                    "border: 2px solid darkgray;\n"
                                    "selection-background-color: lightgray;\n"
                                    "subcontrol-origin: padding;\n"
                                    "subcontrol-position: top right;\n"
                                    "width: 15px;\n"
                                    "border-left-width: 1px;\n"
                                    "border-left-color: darkgray;\n"
                                    "border-left-style: solid; /* just a single line */\n"
                                    "border-radius: 3px; /* same radius as the QComboBox */")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 230, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet(" background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                      "                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
                                      "                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
                                      "border: 2px solid darkgray;\n"
                                      "selection-background-color: lightgray;\n"
                                      "subcontrol-origin: padding;\n"
                                      "subcontrol-position: top right;\n"
                                      "width: 15px;\n"
                                      "border-left-width: 1px;\n"
                                      "border-left-color: darkgray;\n"
                                      "border-left-style: solid; /* just a single line */\n"
                                      "border-radius: 3px; /* same radius as the QComboBox */")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 280, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label_3.setStyleSheet("    background-color: red;\n"
                                   "    border-style: outset;\n"
                                   "    border-width: 2px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: beige;\n"
                                   "    font: bold 14px;\n"
                                   "    min-width: 10em;\n"
                                   "    padding: 6px;\n"
                                   "\n"
                                   "QPushButton#BlueButton:hover {\n"
                                   "    background-color: #64b5f6;\n"
                                   "    color: #fff;\n"
                                   "}")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("backround.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 220, 231, 21))
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 20, 900, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setAcceptDrops(False)
        self.label_2.setStyleSheet("background-color: #eeccff;\n"
                                   "    border-radius: 10px;")
        self.label_2.setLineWidth(2)
        self.label_2.setText(
            "Sperm Hücre Morfolojilerinin Deep Learning ile Sınıflandırılması")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 200, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #ffffff")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 300, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        font.setStrikeOut(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ffffff")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(520, 360, 171, 171))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("img/Future.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 80, 51, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(185, 100, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(True)
        self.label_8.setAcceptDrops(False)
        self.label_8.setStyleSheet("background-color: #eeccff;\n"
                                   "    border-radius: 10px;")
        self.label_8.setLineWidth(2)
        self.label_8.setText("1")
        self.label_8.setTextFormat(QtCore.Qt.PlainText)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(585, 100, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(True)
        self.label_9.setAcceptDrops(False)
        self.label_9.setStyleSheet("background-color: #eeccff;\n"
                                   "    border-radius: 10px;")
        self.label_9.setLineWidth(2)
        self.label_9.setText("2")
        self.label_9.setTextFormat(QtCore.Qt.PlainText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(985, 100, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(True)
        self.label_10.setAcceptDrops(False)
        self.label_10.setStyleSheet("background-color: #eeccff;\n"
                                    "    border-radius: 10px;")
        self.label_10.setLineWidth(2)
        self.label_10.setText("3")
        self.label_10.setTextFormat(QtCore.Qt.PlainText)
        self.label_10.setScaledContents(False)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(960, 210, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(920, 480, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("background-color: #aaccff ;\n"
                                    "    border-radius: 10px;")
        self.label_11.setTextFormat(QtCore.Qt.PlainText)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(400, 100, 3, 570))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(
            "background-color: #ffffff;border-radius: 2px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(800, 100, 3, 570))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(
            "background-color: #ffffff;border-radius: 2px;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(100, 400, 200, 200))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("img/HuSHeMMobileNet.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 220, 80, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(850, 290, 301, 161))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textBrowser.setFont(font)
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 81))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/ytu1.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1080, 20, 81, 81))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("img/ytu1.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.label_3.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.pushButton_2.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.pushButton_3.raise_()
        self.textBrowser.raise_()
        self.label.raise_()
        self.label_15.raise_()
        AraProje.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AraProje)
        self.statusbar.setObjectName("statusbar")
        AraProje.setStatusBar(self.statusbar)
        self.retranslateUi(AraProje)
        QtCore.QMetaObject.connectSlotsByName(AraProje)
        ####################################################
        self.comboBox.activated[str].connect(self.on_choice)
        self.comboBox_2.activated[str].connect(self.on_choice)
        self.pushButton_3.clicked.connect(self.getFileName)
        self.pushButton.clicked.connect(self.load_image)
        self.pushButton_2.clicked.connect(self.test_image)

    def retranslateUi(self, AraProje):
        _translate = QtCore.QCoreApplication.translate
        AraProje.setWindowTitle(_translate("AraProje", "MainWindow"))
        self.comboBox.setItemText(0, _translate("AraProje", "MobileNet"))
        self.comboBox.setItemText(1, _translate("AraProje", "Xception"))
        self.comboBox.setItemText(2, _translate("AraProje", "GoogleNet"))
        self.comboBox_2.setItemText(0, _translate("AraProje", "HuSHeM"))
        self.comboBox_2.setItemText(1, _translate("AraProje", "SMIDS"))
        self.pushButton.setText(_translate("AraProje", "Load Test Image"))
        self.lineEdit.setPlaceholderText(_translate("AraProje", "Path:"))
        self.label_4.setText(_translate("AraProje", "Dataset"))
        self.label_5.setText(_translate("AraProje", "Network"))
        self.label_7.setText(_translate("AraProje", "TextLabel"))
        self.pushButton_2.setText(_translate("AraProje", "Test->"))
        self.label_11.setText(_translate("AraProje", "?"))
        self.pushButton_3.setText(_translate("AraProje", "Browse"))
        self.textBrowser.setPlaceholderText(_translate("AraProje", "Results"))

    def on_choice(self):
        _translate = QtCore.QCoreApplication.translate
        model = self.comboBox.currentText()
        dataset = self.comboBox_2.currentText()
        self.label_14.setPixmap(QtGui.QPixmap("img/"+dataset+model+".png"))

    def getFileName(self):
        fname, _ = QFileDialog.getOpenFileName()
        path = str(fname)
        self.lineEdit.setText(path)

    def load_image(self):
        path = self.lineEdit.text()
        self.label_6.setPixmap(QtGui.QPixmap(path))

    def test_image(self):
        directory = self.lineEdit.text()
        model = self.comboBox.currentText()
        dataset = self.comboBox_2.currentText()
        x, y = modules.test_model(dataset, model, directory)
        self.textBrowser.setText(x)
        self.label_11.setText(y)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AraProje = QtWidgets.QMainWindow()
    ui = Ui_AraProje()
    ui.setupUi(AraProje)
    AraProje.show()
    sys.exit(app.exec_())
