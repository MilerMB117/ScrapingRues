# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v2cuZeIm.ui'
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
from PySide2.QtWidgets import *

import BdB_rc
import logo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(677, 446)
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
        self.cedulaText.setGeometry(QRect(130, 100, 181, 20))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        self.cedulaText.setFont(font1)
        self.cedulaText.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(196, 196, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius: 5px")
        self.cedulaText.setAlignment(Qt.AlignCenter)
        self.consultarButton = QPushButton(self.widget)
        self.consultarButton.setObjectName(u"consultarButton")
        self.consultarButton.setGeometry(QRect(340, 100, 91, 23))
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
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(110, 150, 361, 161))
        self.textEdit.setFrameShape(QFrame.WinPanel)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(530, 60, 101, 101))
        self.label_6.setStyleSheet(u"")
        self.label_6.setPixmap(QPixmap(u":/prefijoNuevo/BdB.png"))
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.cedulaText.raise_()
        self.consultarButton.raise_()
        self.label_5.raise_()
        self.textEdit.raise_()
        self.label_6.raise_()
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(280, 370, 351, 61))
        self.label_4.setStyleSheet(u"")
        self.label_4.setPixmap(QPixmap(u":/prefijoNuevo/aval.png"))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Banco de  Bogot\u00e1 - RUES Scraping", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Consulta de RUES</span></p></body></html>", None))
        self.cedulaText.setText(QCoreApplication.translate("Form", u"Ingrese el n\u00famero de NIT", None))
        self.consultarButton.setText(QCoreApplication.translate("Form", u"Consultar", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Aplicativo para la </p><p align=\"center\">extracci\u00f3n de datos</p><p align=\"center\">de RUES. </p><p align=\"center\">Desarrollada en</p><p align=\"center\"><span style=\" font-weight:600;\">Python.</span></p></body></html>", None))
        self.label_6.setText("")
        self.label_4.setText("")
    # retranslateUi

