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
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.pb_menu_exportdlg = QPushButton(self.pg_menu)
        self.pb_menu_exportdlg.setObjectName(u"pb_menu_exportdlg")

        self.gridLayout.addWidget(self.pb_menu_exportdlg, 0, 0, 1, 1)

        self.cb_menu_exportdlg = QComboBox(self.pg_menu)
        self.cb_menu_exportdlg.setObjectName(u"cb_menu_exportdlg")

        self.gridLayout.addWidget(self.cb_menu_exportdlg, 1, 0, 1, 1)

        self.stk_main.addWidget(self.pg_menu)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stk_main.addWidget(self.page_2)

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

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        self.pb_menu_exportdlg.setText(QCoreApplication.translate("main", u"Export DLG", None))
        pass
    # retranslateUi

