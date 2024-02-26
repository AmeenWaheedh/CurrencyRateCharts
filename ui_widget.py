# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QRadioButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(645, 456)
        self.cmb_currency = QComboBox(Widget)
        self.cmb_currency.setObjectName(u"cmb_currency")
        self.cmb_currency.setGeometry(QRect(120, 20, 121, 22))
        font = QFont()
        font.setPointSize(12)
        self.cmb_currency.setFont(font)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 71, 21))
        self.label.setFont(font)
        self.frame_chart = QFrame(Widget)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setGeometry(QRect(20, 60, 611, 381))
        self.frame_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.frame_BuySell = QFrame(Widget)
        self.frame_BuySell.setObjectName(u"frame_BuySell")
        self.frame_BuySell.setGeometry(QRect(260, 10, 221, 40))
        self.frame_BuySell.setFrameShape(QFrame.StyledPanel)
        self.frame_BuySell.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_BuySell)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.radio_Buy = QRadioButton(self.frame_BuySell)
        self.radio_Buy.setObjectName(u"radio_Buy")
        self.radio_Buy.setFont(font)

        self.horizontalLayout.addWidget(self.radio_Buy)

        self.radio_Sell = QRadioButton(self.frame_BuySell)
        self.radio_Sell.setObjectName(u"radio_Sell")
        self.radio_Sell.setFont(font)

        self.horizontalLayout.addWidget(self.radio_Sell)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Currency:", None))
        self.radio_Buy.setText(QCoreApplication.translate("Widget", u"Buy Rate", None))
        self.radio_Sell.setText(QCoreApplication.translate("Widget", u"Sell Rate", None))
    # retranslateUi

