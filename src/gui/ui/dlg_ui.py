# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dlg.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dlg(object):
    def setupUi(self, Dlg):
        if not Dlg.objectName():
            Dlg.setObjectName(u"Dlg")
        Dlg.resize(1039, 657)
        self.glay_main = QGridLayout(Dlg)
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(Dlg)
        self.fr_main.setObjectName(u"fr_main")
        self.fr_main.setFrameShape(QFrame.StyledPanel)
        self.fr_main.setFrameShadow(QFrame.Raised)
        self.vlay_fr_main = QVBoxLayout(self.fr_main)
        self.vlay_fr_main.setSpacing(0)
        self.vlay_fr_main.setObjectName(u"vlay_fr_main")
        self.vlay_fr_main.setContentsMargins(0, 0, 0, 0)
        self.fr_menu_top = QFrame(self.fr_main)
        self.fr_menu_top.setObjectName(u"fr_menu_top")
        self.hlay_menu_top = QHBoxLayout(self.fr_menu_top)
        self.hlay_menu_top.setSpacing(0)
        self.hlay_menu_top.setObjectName(u"hlay_menu_top")
        self.hlay_menu_top.setContentsMargins(0, 0, 0, 0)
        self.lb_mt_ico = QLabel(self.fr_menu_top)
        self.lb_mt_ico.setObjectName(u"lb_mt_ico")

        self.hlay_menu_top.addWidget(self.lb_mt_ico)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.vlay_msg_body = QVBoxLayout(self.fr_body)
        self.vlay_msg_body.setSpacing(0)
        self.vlay_msg_body.setObjectName(u"vlay_msg_body")
        self.vlay_msg_body.setContentsMargins(10, 10, 10, 10)
        self.fr_dlg_body = QFrame(self.fr_body)
        self.fr_dlg_body.setObjectName(u"fr_dlg_body")
        self.fr_dlg_body.setFrameShape(QFrame.StyledPanel)
        self.fr_dlg_body.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.fr_dlg_body)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 233, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_12 = QPushButton(self.fr_dlg_body)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_2.addWidget(self.pushButton_12, 7, 1, 1, 1)

        self.pushButton_5 = QPushButton(self.fr_dlg_body)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 2, 0, 1, 2)

        self.pushButton_11 = QPushButton(self.fr_dlg_body)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_2.addWidget(self.pushButton_11, 7, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.fr_dlg_body)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 1, 0, 1, 2)

        self.pushButton_6 = QPushButton(self.fr_dlg_body)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 4, 0, 1, 2)

        self.pushButton_10 = QPushButton(self.fr_dlg_body)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_2.addWidget(self.pushButton_10, 8, 0, 1, 2)

        self.pushButton_8 = QPushButton(self.fr_dlg_body)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_2.addWidget(self.pushButton_8, 6, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.fr_dlg_body)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_2.addWidget(self.pushButton_9, 6, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.fr_dlg_body)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 2)

        self.pushButton_4 = QPushButton(self.fr_dlg_body)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 3, 0, 1, 2)

        self.pushButton_7 = QPushButton(self.fr_dlg_body)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 5, 0, 1, 2)

        self.pushButton_13 = QPushButton(self.fr_dlg_body)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_2.addWidget(self.pushButton_13, 9, 0, 1, 2)

        self.pushButton_14 = QPushButton(self.fr_dlg_body)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_2.addWidget(self.pushButton_14, 10, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pb_dlg = QPushButton(self.fr_dlg_body)
        self.pb_dlg.setObjectName(u"pb_dlg")

        self.verticalLayout.addWidget(self.pb_dlg)

        self.lw_dlg = QListWidget(self.fr_dlg_body)
        self.lw_dlg.setObjectName(u"lw_dlg")

        self.verticalLayout.addWidget(self.lw_dlg)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 2, 1)


        self.vlay_msg_body.addWidget(self.fr_dlg_body)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_dlg_bottom = QFrame(self.fr_main)
        self.fr_dlg_bottom.setObjectName(u"fr_dlg_bottom")
        self.hlay_msg_bottom = QHBoxLayout(self.fr_dlg_bottom)
        self.hlay_msg_bottom.setSpacing(2)
        self.hlay_msg_bottom.setObjectName(u"hlay_msg_bottom")
        self.hlay_msg_bottom.setContentsMargins(0, 2, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_msg_bottom.addItem(self.horizontalSpacer)

        self.pb_ok = QPushButton(self.fr_dlg_bottom)
        self.pb_ok.setObjectName(u"pb_ok")

        self.hlay_msg_bottom.addWidget(self.pb_ok)


        self.vlay_fr_main.addWidget(self.fr_dlg_bottom)


        self.glay_main.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(Dlg)

        QMetaObject.connectSlotsByName(Dlg)
    # setupUi

    def retranslateUi(self, Dlg):
        self.pushButton_12.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_13.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pushButton_14.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        self.pb_dlg.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        pass
    # retranslateUi

