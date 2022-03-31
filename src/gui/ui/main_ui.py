# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1057, 775)
        self.vlay_main = QVBoxLayout(main)
        self.vlay_main.setSpacing(0)
        self.vlay_main.setObjectName(u"vlay_main")
        self.vlay_main.setContentsMargins(0, 0, 0, 0)
        self.fr_main = QFrame(main)
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

        self.wg_mt_blank = QWidget(self.fr_menu_top)
        self.wg_mt_blank.setObjectName(u"wg_mt_blank")

        self.hlay_menu_top.addWidget(self.wg_mt_blank)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_2)

        self.lb_mt_nom = QLabel(self.fr_menu_top)
        self.lb_mt_nom.setObjectName(u"lb_mt_nom")

        self.hlay_menu_top.addWidget(self.lb_mt_nom)

        self.horizontalSpacer_1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_top.addItem(self.horizontalSpacer_1)

        self.pb_mt_option = QPushButton(self.fr_menu_top)
        self.pb_mt_option.setObjectName(u"pb_mt_option")

        self.hlay_menu_top.addWidget(self.pb_mt_option)

        self.pb_mt_reduire = QPushButton(self.fr_menu_top)
        self.pb_mt_reduire.setObjectName(u"pb_mt_reduire")

        self.hlay_menu_top.addWidget(self.pb_mt_reduire)

        self.pb_mt_agrandir = QPushButton(self.fr_menu_top)
        self.pb_mt_agrandir.setObjectName(u"pb_mt_agrandir")

        self.hlay_menu_top.addWidget(self.pb_mt_agrandir)

        self.pb_mt_quitter = QPushButton(self.fr_menu_top)
        self.pb_mt_quitter.setObjectName(u"pb_mt_quitter")

        self.hlay_menu_top.addWidget(self.pb_mt_quitter)


        self.vlay_fr_main.addWidget(self.fr_menu_top)

        self.fr_body = QFrame(self.fr_main)
        self.fr_body.setObjectName(u"fr_body")
        self.fr_body.setFrameShape(QFrame.StyledPanel)
        self.fr_body.setFrameShadow(QFrame.Raised)
        self.hlay_body = QVBoxLayout(self.fr_body)
        self.hlay_body.setSpacing(0)
        self.hlay_body.setObjectName(u"hlay_body")
        self.hlay_body.setContentsMargins(0, 0, 0, 0)
        self.stk_main = QStackedWidget(self.fr_body)
        self.stk_main.setObjectName(u"stk_main")
        self.pg_menu = QWidget()
        self.pg_menu.setObjectName(u"pg_menu")
        self.gridLayout = QGridLayout(self.pg_menu)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.pb_menu_exportdlg = QPushButton(self.pg_menu)
        self.pb_menu_exportdlg.setObjectName(u"pb_menu_exportdlg")

        self.gridLayout.addWidget(self.pb_menu_exportdlg, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_menu_rip24 = QPushButton(self.pg_menu)
        self.pb_menu_rip24.setObjectName(u"pb_menu_rip24")

        self.horizontalLayout_3.addWidget(self.pb_menu_rip24)

        self.pb_menu_rip40 = QPushButton(self.pg_menu)
        self.pb_menu_rip40.setObjectName(u"pb_menu_rip40")

        self.horizontalLayout_3.addWidget(self.pb_menu_rip40)

        self.pb_menu_rip47 = QPushButton(self.pg_menu)
        self.pb_menu_rip47.setObjectName(u"pb_menu_rip47")

        self.horizontalLayout_3.addWidget(self.pb_menu_rip47)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)

        self.stk_main.addWidget(self.pg_menu)
        self.pg_dlg = QWidget()
        self.pg_dlg.setObjectName(u"pg_dlg")
        self.gridLayout_2 = QGridLayout(self.pg_dlg)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.fr_dlg_top = QFrame(self.pg_dlg)
        self.fr_dlg_top.setObjectName(u"fr_dlg_top")
        self.horizontalLayout_2 = QHBoxLayout(self.fr_dlg_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pb_retour_menu = QPushButton(self.fr_dlg_top)
        self.pb_retour_menu.setObjectName(u"pb_retour_menu")

        self.horizontalLayout_2.addWidget(self.pb_retour_menu)

        self.cb_marche = QComboBox(self.fr_dlg_top)
        self.cb_marche.setObjectName(u"cb_marche")

        self.horizontalLayout_2.addWidget(self.cb_marche)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_filtre_atraiter = QPushButton(self.fr_dlg_top)
        self.pb_filtre_atraiter.setObjectName(u"pb_filtre_atraiter")

        self.horizontalLayout.addWidget(self.pb_filtre_atraiter)

        self.pb_filtre_tout = QPushButton(self.fr_dlg_top)
        self.pb_filtre_tout.setObjectName(u"pb_filtre_tout")

        self.horizontalLayout.addWidget(self.pb_filtre_tout)

        self.pb_filtre_fait = QPushButton(self.fr_dlg_top)
        self.pb_filtre_fait.setObjectName(u"pb_filtre_fait")

        self.horizontalLayout.addWidget(self.pb_filtre_fait)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout_2.addWidget(self.fr_dlg_top, 0, 0, 1, 2)

        self.fr_dlg_body = QFrame(self.pg_dlg)
        self.fr_dlg_body.setObjectName(u"fr_dlg_body")
        self.fr_dlg_body.setFrameShape(QFrame.StyledPanel)
        self.fr_dlg_body.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.fr_dlg_body, 1, 0, 1, 1)

        self.fr_dlg_tools = QFrame(self.pg_dlg)
        self.fr_dlg_tools.setObjectName(u"fr_dlg_tools")
        self.fr_dlg_tools.setFrameShape(QFrame.StyledPanel)
        self.fr_dlg_tools.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_dlg_tools)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 0)
        self.pb_tools_add_dlg = QPushButton(self.fr_dlg_tools)
        self.pb_tools_add_dlg.setObjectName(u"pb_tools_add_dlg")

        self.verticalLayout.addWidget(self.pb_tools_add_dlg)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.gridLayout_2.addWidget(self.fr_dlg_tools, 1, 1, 1, 1)

        self.stk_main.addWidget(self.pg_dlg)

        self.hlay_body.addWidget(self.stk_main)


        self.vlay_fr_main.addWidget(self.fr_body)

        self.fr_menu_bottom = QFrame(self.fr_main)
        self.fr_menu_bottom.setObjectName(u"fr_menu_bottom")
        self.hlay_menu_bottom = QHBoxLayout(self.fr_menu_bottom)
        self.hlay_menu_bottom.setSpacing(0)
        self.hlay_menu_bottom.setObjectName(u"hlay_menu_bottom")
        self.hlay_menu_bottom.setContentsMargins(0, 0, 0, 0)
        self.lb_mb_version = QLabel(self.fr_menu_bottom)
        self.lb_mb_version.setObjectName(u"lb_mb_version")

        self.hlay_menu_bottom.addWidget(self.lb_mb_version)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hlay_menu_bottom.addItem(self.horizontalSpacer_4)


        self.vlay_fr_main.addWidget(self.fr_menu_bottom)


        self.vlay_main.addWidget(self.fr_main)


        self.retranslateUi(main)

        self.stk_main.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        self.pb_menu_exportdlg.setText(QCoreApplication.translate("main", u"EXPORTS\n"
"DLG", None))
        self.pb_menu_rip24.setText(QCoreApplication.translate("main", u"RIP24", None))
        self.pb_menu_rip40.setText(QCoreApplication.translate("main", u"RIP40", None))
        self.pb_menu_rip47.setText(QCoreApplication.translate("main", u"RIP47", None))
        self.pb_filtre_atraiter.setText(QCoreApplication.translate("main", u"A TRAITER", None))
        self.pb_filtre_tout.setText(QCoreApplication.translate("main", u"TOUT", None))
        self.pb_filtre_fait.setText(QCoreApplication.translate("main", u"FAIT", None))
        pass
    # retranslateUi

