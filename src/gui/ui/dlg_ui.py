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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalSpacer = QSpacerItem(20, 193, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_edit_pno = QPushButton(self.fr_dlg_body)
        self.pb_edit_pno.setObjectName(u"pb_edit_pno")

        self.gridLayout_2.addWidget(self.pb_edit_pno, 7, 1, 1, 1)

        self.pb_edit_cma = QPushButton(self.fr_dlg_body)
        self.pb_edit_cma.setObjectName(u"pb_edit_cma")

        self.gridLayout_2.addWidget(self.pb_edit_cma, 2, 0, 1, 2)

        self.pb_edit_pok = QPushButton(self.fr_dlg_body)
        self.pb_edit_pok.setObjectName(u"pb_edit_pok")

        self.gridLayout_2.addWidget(self.pb_edit_pok, 7, 0, 1, 1)

        self.pb_edit_gex = QPushButton(self.fr_dlg_body)
        self.pb_edit_gex.setObjectName(u"pb_edit_gex")

        self.gridLayout_2.addWidget(self.pb_edit_gex, 1, 0, 1, 2)

        self.pb_edit_edl = QPushButton(self.fr_dlg_body)
        self.pb_edit_edl.setObjectName(u"pb_edit_edl")

        self.gridLayout_2.addWidget(self.pb_edit_edl, 4, 0, 1, 2)

        self.pb_edit_lcl = QPushButton(self.fr_dlg_body)
        self.pb_edit_lcl.setObjectName(u"pb_edit_lcl")

        self.gridLayout_2.addWidget(self.pb_edit_lcl, 8, 0, 1, 2)

        self.pb_edit_dok = QPushButton(self.fr_dlg_body)
        self.pb_edit_dok.setObjectName(u"pb_edit_dok")

        self.gridLayout_2.addWidget(self.pb_edit_dok, 6, 0, 1, 1)

        self.pb_edit_dno = QPushButton(self.fr_dlg_body)
        self.pb_edit_dno.setObjectName(u"pb_edit_dno")

        self.gridLayout_2.addWidget(self.pb_edit_dno, 6, 1, 1, 1)

        self.pb_edit_afa = QPushButton(self.fr_dlg_body)
        self.pb_edit_afa.setObjectName(u"pb_edit_afa")

        self.gridLayout_2.addWidget(self.pb_edit_afa, 0, 0, 1, 2)

        self.pb_edit_cch = QPushButton(self.fr_dlg_body)
        self.pb_edit_cch.setObjectName(u"pb_edit_cch")

        self.gridLayout_2.addWidget(self.pb_edit_cch, 3, 0, 1, 2)

        self.pb_edit_eok = QPushButton(self.fr_dlg_body)
        self.pb_edit_eok.setObjectName(u"pb_edit_eok")

        self.gridLayout_2.addWidget(self.pb_edit_eok, 5, 0, 1, 2)

        self.pb_edit_pau = QPushButton(self.fr_dlg_body)
        self.pb_edit_pau.setObjectName(u"pb_edit_pau")

        self.gridLayout_2.addWidget(self.pb_edit_pau, 9, 0, 1, 2)

        self.pb_edit_ann = QPushButton(self.fr_dlg_body)
        self.pb_edit_ann.setObjectName(u"pb_edit_ann")

        self.gridLayout_2.addWidget(self.pb_edit_ann, 10, 0, 1, 2)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
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
        self.pb_edit_pno.setText(QCoreApplication.translate("Dlg", u"PDB NOK", None))
        self.pb_edit_cma.setText(QCoreApplication.translate("Dlg", u"CRASH MAJEURE", None))
        self.pb_edit_pok.setText(QCoreApplication.translate("Dlg", u"PDB OK", None))
        self.pb_edit_gex.setText(QCoreApplication.translate("Dlg", u"GO EXPORT", None))
        self.pb_edit_edl.setText(QCoreApplication.translate("Dlg", u"ERREURS DLG", None))
        self.pb_edit_lcl.setText(QCoreApplication.translate("Dlg", u"LIVRAISON CLIENT", None))
        self.pb_edit_dok.setText(QCoreApplication.translate("Dlg", u"DJANGO OK", None))
        self.pb_edit_dno.setText(QCoreApplication.translate("Dlg", u"DJANGO NOK", None))
        self.pb_edit_afa.setText(QCoreApplication.translate("Dlg", u"A FAIRE", None))
        self.pb_edit_cch.setText(QCoreApplication.translate("Dlg", u"CRASH CHECK", None))
        self.pb_edit_eok.setText(QCoreApplication.translate("Dlg", u"EXPORT OK", None))
        self.pb_edit_pau.setText(QCoreApplication.translate("Dlg", u"PAUSE", None))
        self.pb_edit_ann.setText(QCoreApplication.translate("Dlg", u"ANNULE", None))
        self.pb_dlg.setText(QCoreApplication.translate("Dlg", u"PushButton", None))
        pass
    # retranslateUi

