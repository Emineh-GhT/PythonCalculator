# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(421, 486)
        Dialog.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);\n"
"")
        self.b_sum = QPushButton(Dialog)
        self.b_sum.setObjectName(u"b_sum")
        self.b_sum.setGeometry(QRect(250, 280, 61, 51))
        self.b_sum.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.text_box = QLineEdit(Dialog)
        self.text_box.setObjectName(u"text_box")
        self.text_box.setGeometry(QRect(40, 40, 341, 51))
        self.text_box.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x20:0, y20:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(200, 200, 200, 200));\n"
"color: rgb(255, 255, 255);")
        self.b_sub = QPushButton(Dialog)
        self.b_sub.setObjectName(u"b_sub")
        self.b_sub.setGeometry(QRect(250, 220, 61, 51))
        self.b_sub.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_equal = QPushButton(Dialog)
        self.b_equal.setObjectName(u"b_equal")
        self.b_equal.setGeometry(QRect(40, 400, 341, 51))
        self.b_equal.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b0 = QPushButton(Dialog)
        self.b0.setObjectName(u"b0")
        self.b0.setGeometry(QRect(40, 340, 131, 51))
        self.b0.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b_ac = QPushButton(Dialog)
        self.b_ac.setObjectName(u"b_ac")
        self.b_ac.setGeometry(QRect(40, 100, 61, 51))
        self.b_ac.setStyleSheet(u"background-color: rgb(200,200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.b7 = QPushButton(Dialog)
        self.b7.setObjectName(u"b7")
        self.b7.setGeometry(QRect(40, 160, 61, 51))
        self.b7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b8 = QPushButton(Dialog)
        self.b8.setObjectName(u"b8")
        self.b8.setGeometry(QRect(110, 160, 61, 51))
        self.b8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b5 = QPushButton(Dialog)
        self.b5.setObjectName(u"b5")
        self.b5.setGeometry(QRect(110, 220, 61, 51))
        self.b5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b3 = QPushButton(Dialog)
        self.b3.setObjectName(u"b3")
        self.b3.setGeometry(QRect(180, 280, 61, 51))
        self.b3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b4 = QPushButton(Dialog)
        self.b4.setObjectName(u"b4")
        self.b4.setGeometry(QRect(40, 220, 61, 51))
        self.b4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b9 = QPushButton(Dialog)
        self.b9.setObjectName(u"b9")
        self.b9.setGeometry(QRect(180, 160, 61, 51))
        self.b9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b6 = QPushButton(Dialog)
        self.b6.setObjectName(u"b6")
        self.b6.setGeometry(QRect(180, 220, 61, 51))
        self.b6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b1 = QPushButton(Dialog)
        self.b1.setObjectName(u"b1")
        self.b1.setGeometry(QRect(40, 280, 61, 51))
        self.b1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b2 = QPushButton(Dialog)
        self.b2.setObjectName(u"b2")
        self.b2.setGeometry(QRect(110, 280, 61, 51))
        self.b2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b_dot = QPushButton(Dialog)
        self.b_dot.setObjectName(u"b_dot")
        self.b_dot.setGeometry(QRect(180, 340, 61, 51))
        self.b_dot.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(79, 79, 79);")
        self.b_pm = QPushButton(Dialog)
        self.b_pm.setObjectName(u"b_pm")
        self.b_pm.setGeometry(QRect(110, 100, 61, 51))
        self.b_pm.setStyleSheet(u"background-color: rgb(200,200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.b_p = QPushButton(Dialog)
        self.b_p.setObjectName(u"b_p")
        self.b_p.setGeometry(QRect(180, 100, 61, 51))
        self.b_p.setStyleSheet(u"background-color: rgb(200,200, 200);\n"
"color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.b_d = QPushButton(Dialog)
        self.b_d.setObjectName(u"b_d")
        self.b_d.setGeometry(QRect(250, 100, 61, 51))
        self.b_d.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.b_m = QPushButton(Dialog)
        self.b_m.setObjectName(u"b_m")
        self.b_m.setGeometry(QRect(250, 160, 61, 51))
        self.b_m.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_sqrt = QPushButton(Dialog)
        self.b_sqrt.setObjectName(u"b_sqrt")
        self.b_sqrt.setGeometry(QRect(250, 340, 61, 51))
        self.b_sqrt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_tan = QPushButton(Dialog)
        self.b_tan.setObjectName(u"b_tan")
        self.b_tan.setGeometry(QRect(320, 220, 61, 51))
        self.b_tan.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_sin = QPushButton(Dialog)
        self.b_sin.setObjectName(u"b_sin")
        self.b_sin.setGeometry(QRect(320, 100, 61, 51))
        self.b_sin.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_cos = QPushButton(Dialog)
        self.b_cos.setObjectName(u"b_cos")
        self.b_cos.setGeometry(QRect(320, 160, 61, 51))
        self.b_cos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_log = QPushButton(Dialog)
        self.b_log.setObjectName(u"b_log")
        self.b_log.setGeometry(QRect(320, 340, 61, 51))
        self.b_log.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.b_cot = QPushButton(Dialog)
        self.b_cot.setObjectName(u"b_cot")
        self.b_cot.setGeometry(QRect(320, 280, 61, 51))
        self.b_cot.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 150, 0);\n"
"border-color: rgb(0, 0, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.b_sum.setText(QCoreApplication.translate("Dialog", u"+", None))
        self.b_sub.setText(QCoreApplication.translate("Dialog", u"-", None))
        self.b_equal.setText(QCoreApplication.translate("Dialog", u"=", None))
        self.b0.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.b_ac.setText(QCoreApplication.translate("Dialog", u"AC", None))
        self.b7.setText(QCoreApplication.translate("Dialog", u"7", None))
        self.b8.setText(QCoreApplication.translate("Dialog", u"8", None))
        self.b5.setText(QCoreApplication.translate("Dialog", u"5", None))
        self.b3.setText(QCoreApplication.translate("Dialog", u"3", None))
        self.b4.setText(QCoreApplication.translate("Dialog", u"4", None))
        self.b9.setText(QCoreApplication.translate("Dialog", u"9", None))
        self.b6.setText(QCoreApplication.translate("Dialog", u"6", None))
        self.b1.setText(QCoreApplication.translate("Dialog", u"1", None))
        self.b2.setText(QCoreApplication.translate("Dialog", u"2", None))
        self.b_dot.setText(QCoreApplication.translate("Dialog", u".", None))
        self.b_pm.setText(QCoreApplication.translate("Dialog", u"+ / -", None))
        self.b_p.setText(QCoreApplication.translate("Dialog", u"%", None))
        self.b_d.setText(QCoreApplication.translate("Dialog", u"\u00f7", None))
        self.b_m.setText(QCoreApplication.translate("Dialog", u"x", None))
        self.b_sqrt.setText(QCoreApplication.translate("Dialog", u"sqrt", None))
        self.b_tan.setText(QCoreApplication.translate("Dialog", u"tan", None))
        self.b_sin.setText(QCoreApplication.translate("Dialog", u"sin", None))
        self.b_cos.setText(QCoreApplication.translate("Dialog", u"cos", None))
        self.b_log.setText(QCoreApplication.translate("Dialog", u"log", None))
        self.b_cot.setText(QCoreApplication.translate("Dialog", u"cot", None))
    # retranslateUi

