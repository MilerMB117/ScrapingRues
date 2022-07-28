# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v2wGzvLT.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5 import QtWidgets
from PySide2.QtWidgets import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(677, 409)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-50, 0, 671, 401))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 401, 371))
        self.label.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(46, 60, 115, 255), stop:1 rgba(85, 170, 255, 255));\n"
"border-radius: 10px;\n"
"border-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 50, 331, 31))
        font = QFont()
        font.setFamily(u"Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(Qt.RichText)
        self.cedulaText = QLineEdit(self.widget)
        self.cedulaText.setObjectName(u"cedulaText")
        self.cedulaText.setGeometry(QRect(110, 100, 211, 20))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        self.cedulaText.setFont(font1)
        self.cedulaText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 196, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 5px")
        self.cedulaText.setAlignment(Qt.AlignCenter)
        self.loadCSVButton = QPushButton(self.widget)
        self.loadCSVButton.setObjectName(u"loadCSVButton")
        self.loadCSVButton.setGeometry(QRect(340, 100, 91, 23))
        self.loadCSVButton.setFont(font)
        self.loadCSVButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 212, 68, 255), stop:1 rgba(212, 255, 156, 255));\n"
"border-radius: 10px\n"
"")
        self.consultarButton = QPushButton(self.widget)
        self.consultarButton.setObjectName(u"consultarButton")
        self.consultarButton.setGeometry(QRect(150, 150, 91, 23))
        self.consultarButton.setFont(font)
        self.consultarButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 227, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 10px\n"
"")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 30, 221, 331))
        self.label_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.346591, y1:0.363636, x2:1, y2:1, stop:0 rgba(252, 255, 1, 255), stop:1 rgba(232, 164, 0, 255));\n"
"border-radius: 10px;")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(510, 180, 131, 151))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setTextFormat(Qt.AutoText)
        self.finishButton = QPushButton(self.widget)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(260, 150, 91, 23))
        self.finishButton.setFont(font)
        self.finishButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 162, 255, 255), stop:1 rgba(122, 198, 255, 255));\n"
"border-radius: 10px\n"
"")
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.cedulaText.raise_()
        self.loadCSVButton.raise_()
        self.consultarButton.raise_()
        self.label_5.raise_()
        self.finishButton.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Banco de  Bogot\u00e1 - RNEC Scraping", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Consulta de defunci\u00f3n Registraduria</span></p></body></html>", None))
        self.cedulaText.setText(QCoreApplication.translate("Form", u"Ingrese el n\u00famero de cedula...", None))
        self.loadCSVButton.setText(QCoreApplication.translate("Form", u"Abrir CSV", None))
        self.consultarButton.setText(QCoreApplication.translate("Form", u"Consultar", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Aplicativo para la </span></p><p align=\"center\"><span style=\" font-size:10pt;\">extracci\u00f3n de datos</span></p><p align=\"center\"><span style=\" font-size:10pt;\">de RNEC. </span></p><p align=\"center\"><span style=\" font-size:10pt;\">Desarrollada en</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Python.</span></p></body></html>", None))
        self.finishButton.setText(QCoreApplication.translate("Form", u"Ver resultados", None))
    # retranslateUi

if __name__ == "__main__":
        app=QtWidgets.QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        sys.exit(app.exec_())
        