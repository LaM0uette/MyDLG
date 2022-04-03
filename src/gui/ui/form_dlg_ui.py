# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form_dlg.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_FormDlg(object):
    def setupUi(self, FormDlg):
        if not FormDlg.objectName():
            FormDlg.setObjectName(u"FormDlg")
        FormDlg.resize(648, 783)
        self.glay_main = QGridLayout(FormDlg)
        self.glay_main.setSpacing(0)
        self.glay_main.setObjectName(u"glay_main")
        self.glay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(FormDlg)
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
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_msg_body.addItem(self.verticalSpacer_2)

        self.lb_phase = QLabel(self.fr_body)
        self.lb_phase.setObjectName(u"lb_phase")

        self.vlay_msg_body.addWidget(self.lb_phase)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cb_phase = QComboBox(self.fr_body)
        self.cb_phase.setObjectName(u"cb_phase")

        self.horizontalLayout.addWidget(self.cb_phase)

        self.sb_phase = QSpinBox(self.fr_body)
        self.sb_phase.setObjectName(u"sb_phase")

        self.horizontalLayout.addWidget(self.sb_phase)


        self.vlay_msg_body.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_msg_body.addItem(self.verticalSpacer_3)

        self.lb_td = QLabel(self.fr_body)
        self.lb_td.setObjectName(u"lb_td")

        self.vlay_msg_body.addWidget(self.lb_td)

        self.cb_td = QComboBox(self.fr_body)
        self.cb_td.setObjectName(u"cb_td")

        self.vlay_msg_body.addWidget(self.cb_td)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_msg_body.addItem(self.verticalSpacer_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_nro = QLabel(self.fr_body)
        self.lb_nro.setObjectName(u"lb_nro")

        self.gridLayout.addWidget(self.lb_nro, 1, 0, 1, 1)

        self.cb_nro = QComboBox(self.fr_body)
        self.cb_nro.setObjectName(u"cb_nro")

        self.gridLayout.addWidget(self.cb_nro, 2, 0, 1, 1)

        self.lb_pm = QLabel(self.fr_body)
        self.lb_pm.setObjectName(u"lb_pm")

        self.gridLayout.addWidget(self.lb_pm, 1, 1, 1, 1)

        self.cb_pm = QComboBox(self.fr_body)
        self.cb_pm.setObjectName(u"cb_pm")

        self.gridLayout.addWidget(self.cb_pm, 2, 1, 1, 1)


        self.vlay_msg_body.addLayout(self.gridLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.vlay_msg_body.addItem(self.verticalSpacer_5)

        self.lb_refcode3 = QLabel(self.fr_body)
        self.lb_refcode3.setObjectName(u"lb_refcode3")

        self.vlay_msg_body.addWidget(self.lb_refcode3)

        self.cb_refcode3 = QComboBox(self.fr_body)
        self.cb_refcode3.setObjectName(u"cb_refcode3")

        self.vlay_msg_body.addWidget(self.cb_refcode3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vlay_msg_body.addItem(self.verticalSpacer)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_msg_bottom = QFrame(self.fr_main)
        self.fr_msg_bottom.setObjectName(u"fr_msg_bottom")
        self.hlay_msg_bottom = QHBoxLayout(self.fr_msg_bottom)
        self.hlay_msg_bottom.setSpacing(2)
        self.hlay_msg_bottom.setObjectName(u"hlay_msg_bottom")
        self.hlay_msg_bottom.setContentsMargins(0, 2, 1, 1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_msg_bottom.addItem(self.horizontalSpacer)

        self.pb_ok = QPushButton(self.fr_msg_bottom)
        self.pb_ok.setObjectName(u"pb_ok")

        self.hlay_msg_bottom.addWidget(self.pb_ok)


        self.vlay_fr_main.addWidget(self.fr_msg_bottom)


        self.glay_main.addWidget(self.fr_main, 1, 0, 1, 1)


        self.retranslateUi(FormDlg)

        QMetaObject.connectSlotsByName(FormDlg)
    # setupUi

    def retranslateUi(self, FormDlg):
        self.lb_phase.setText(QCoreApplication.translate("FormDlg", u"Phase :", None))
        self.lb_td.setText(QCoreApplication.translate("FormDlg", u"Transport / Distribution :", None))
        self.lb_nro.setText(QCoreApplication.translate("FormDlg", u"NRO :", None))
        self.lb_pm.setText(QCoreApplication.translate("FormDlg", u"PM :", None))
        self.lb_refcode3.setText(QCoreApplication.translate("FormDlg", u"REFCODE3 :", None))
        pass
    # retranslateUi

