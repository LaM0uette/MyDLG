import functools
import sys
import time

from PySide6 import QtCore, QtWidgets, QtGui

from src import *
from src.gui import *


# Renommez des de bases
class main(Ui_main, QtWidgets.QWidget):
    dragPos: QtCore.QPoint

    def __init__(self):
        super(main, self).__init__()

        ### AJOUTS DE BASE ###
            # size_grip
        self.size_grip = QtWidgets.QSizeGrip(self)
            # tray
        self.tray = QtWidgets.QSystemTrayIcon(QtGui.QPixmap(f"{PaImg.MAIN}th3.svg"), self)
        self.tray.activated.connect(self.trayActivate)
        self.timer_double_click = QtCore.QTimer(self)
        self.timer_double_click.setSingleShot(True)
        self.timer_double_click.timeout.connect(self.traySingleClick)
            # tray_menu
        self.tray_menu = QtWidgets.QMenu()
        self.tray_menu.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ### VARIABLES DE BASES ###
        self.win_state = QtCore.Qt.WindowNoState
        self.marche = 24

        ### FONCTIONS AU LANCEMENT ###
        self.INIT(
            [self.IN_BASE, "Configuration des éléments principaux"],
            [self.IN_SETUP_UI, "Setup de l'interface graphique"],
            [self.IN_CLASSE, "Initialisation des Widgets"],
            [self.IN_WG, "Configuration de base des Widgets"],
            [self.IN_CONNECTIONS, "Ajout des connexions"],
            [self.IN_ACT, "Fonctions de base"],
            [self.IN_WG_BASE, "Etat de base des Widgets"],
            [self.IN_TRAY, "Finalisation de la Configuration"],
            [self.TEST_SQL, "Test de la connexion à la base de données"]
        )

        splash_screen.close()


        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseDoubleClickEvent = self.evt.mouseDoubleClickEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent
        self.mouseReleaseEvent = self.evt.mouseReleaseEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre principal ###
        self.setWindowTitle(Config.nom)
        self.setWindowIcon(QtGui.QPixmap(f"{PaImg.MAIN}th3.svg"))
        self.setWindowOpacity(Config.opacity)

        self.setGraphicsEffect(PaShadow.OMBRE_PORTEE(self))

        self.e_resize_screen()
    def IN_SETUP_UI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        ### Ui principal ###
        self.setupUi(self)
        self.vlay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ###  QPushButton  ###
        MyPushButton.MenuTop(self.pb_mt_option).option()
        MyPushButton.MenuTop(self.pb_mt_reduire).reduire()
        MyPushButton.MenuTop(self.pb_mt_agrandir).agrandir()
        MyPushButton.MenuTop(self.pb_mt_quitter).quitter()

        # Menu
        MyPushButton.Base(self.pb_menu_exportdlg).MenuPB()

        MyPushButton.MenuMarche(self.pb_menu_rip24).Rip24()
        MyPushButton.MenuMarche(self.pb_menu_rip40).Rip40()
        MyPushButton.MenuMarche(self.pb_menu_rip47).Rip47()

        # Dlg
        MyPushButton.Base(self.pb_retour_menu).RetourMenu()

        MyPushButton.DlgFiltre(self.pb_filtre_atraiter).ATraiter()
        MyPushButton.DlgFiltre(self.pb_filtre_tout).Tout()
        MyPushButton.DlgFiltre(self.pb_filtre_fait).Fait()

        MyPushButton.Base(self.pb_search_dlg).SearchDlg()
            # tools
        MyPushButton.Base(self.pb_tools_add_dlg).DlgTools()
        ### /QPushButton  ###


        ###  QToolButton  ###
        ### /QToolButton  ###


        ###  QRadioButton  ###
        ### /QRadioButton  ###


        ###  QCheckBox  ###
        ### /QCheckBox  ###


        ###  QCommandLinkButton  ###
        ### /QCommandLinkButton  ###


        # ### QListView ###
        # ### /QListView ###


        ### QTreeView ###
        ### /QTreeView ###


        ### QTableView ###
        ### /QTableView ###


        # ### QListWidget ###
        # ### /QListWidget ###


        ### QTreeWidget ###
        ### /QTreeWidget ###


        ### QTableWidget ###
        ### /QTableWidget ###


        # ### QScrollBoxArea ###
        MyScrollArea.Base(self.sca_dlg).DLG()
        # ### /QScrollBoxArea ###


        ### QToolBox ###
        ### /QToolBox ###


        ###  QFrame  ###
        MyFrame.Base(self.fr_body).Base_no_radius(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Menu(self.fr_menu_bottom).bottom()
        MyFrame.Cadre(self.fr_main).th2_fin()

        MyFrame.Base(self.fr_dlg_top).Base()
        MyFrame.Cadre(self.fr_dlg_body).th3()
        MyFrame.Base(self.fr_dlg_tools).Tools()
        ### /QFrame  ###


        ### QComboBox ###
        MyComboBox.Base(self.cb_marche).Marche()
        MyComboBox.Base(self.cb_filtre_search).Marche()
        ### /QComboBox ###


        ### QComboBox ###
        ### /QComboBox ###


        ### QLineEdit ###
        MyLineEdit.Base(self.le_search_dlg).SearchDLG()
        ### /QLineEdit ###


        ### QTextEdit ###
        ### /QTextEdit ###


        ### QPlainTextEdit ###
        ### /QPlainTextEdit ###


        ### QSpinBox ###
        ### /QSpinBox ###


        ### QDoubleSpinBox ###
        ### /QDoubleSpinBox ###


        ### QTimeEdit ###
        ### /QTimeEdit ###


        ### QDateEdit ###
        ### /QDateEdit ###


        ### QDateTimeEdit ###
        ### /QDateTimeEdit ###


        # ### QSlider ###
        # MySlider.Base(self.hsd_demo).th()
        # MySlider.Base(self.vsd_demo).rond()
        # ### /QSlider ###


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_main()
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
        MyLabel.Base(self.lb_mb_version).Transparent()
        ### /QLabel ###


        ### QProgressBar ###
        ### /QProgressBar ###
    def IN_WG(self):
        ### Base ###
        self.setCursor(Functions().SET_CURSOR(PaCur.SOURIS))

        ### Nom de l'app ###
        self.lb_mt_nom.setText(Config.nom)


        ### Widget blanc pour centrer le nom de l'app ###
        dim = PaDim.H9 * 1.4
        Functions().SET_DIM(self.wg_mt_blank, width=dim*8, height=dim)


        ### Version de l'app ###
        self.lb_mb_version.setText(f" Version : {Config.version}")


        ### size_grip ###
        if Config.resize:
            self.size_grip.setCursor(Functions().SET_CURSOR(PaCur.FLECHE_NWSE))
            self.size_grip.setStyleSheet(
                f"""
                QSizeGrip {{
                image: url({PaImg.RESIZE}th3.svg);
                width: {PaDim.H10}px;
                height: {PaDim.H10}px;
                }}
                """
            )
            self.hlay_menu_bottom.addWidget(self.size_grip)


        ### Menu - combobox marche ###
        self.cb_marche.addItems(["RIP24", "RIP40", "RIP47"])


        ### Dlg ###
        self.fr_dlg_top.setFixedHeight(PaDim.H9+10)
            # search
        self.le_search_dlg.setPlaceholderText("Filtre...")
        self.cb_filtre_search.addItems(["like", "=", "in", ".*"])  # ajoputer le nom du dlg dans les vues + nom dlg=export
    def IN_CONNECTIONS(self):
        ### Menu_top ###
        self.pb_mt_option.clicked.connect(lambda: OptionBox.MAIN(fen_main=fen))
        self.pb_mt_reduire.clicked.connect(lambda: self.evt.e_reduire())
        self.pb_mt_agrandir.clicked.connect(lambda: self.evt.e_agrandir())
        self.pb_mt_quitter.clicked.connect(lambda: self.evt.e_cacher())


        ### Menu ###
        self.pb_menu_exportdlg.clicked.connect(self.f_pbmenu_exportdlg)
        self.pb_retour_menu.clicked.connect(self.f_pbdlg_menu)


        ### DLG ###
        self.pb_tools_add_dlg.clicked.connect(self.f_add_dlg)
        self.cb_marche.currentTextChanged.connect(self.a_set_marche)

        ### marche ###
        self.pb_menu_rip24.clicked.connect(self.a_set_marche)
        self.pb_menu_rip40.clicked.connect(self.a_set_marche)
        self.pb_menu_rip47.clicked.connect(self.a_set_marche)


        # pb filtre vue
        self.pb_filtre_atraiter.clicked.connect(self.f_maj_dlg)
        self.pb_filtre_tout.clicked.connect(self.f_maj_dlg)
        self.pb_filtre_fait.clicked.connect(self.f_maj_dlg)
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        self.stk_main.setCurrentWidget(self.pg_menu)
        self.pb_menu_rip24.setChecked(True)
        self.pb_filtre_atraiter.setChecked(True)

        # Tempo
        self.f_maj_dlg()

        self.cb_filtre_search.setVisible(False)
        self.le_search_dlg.setVisible(False)
        self.pb_search_dlg.setVisible(False)
    def IN_TRAY(self):
        ### Actions ###
        Functions.ADD_QACTION(
            self,
            tray=self.tray_menu,
            ico=PaImg.QUITTER,
            ico_rgb="bn2",
            txt="Quitter",
            shortcut_txt="Shift+Esc",
            status_tip="Quitter",
            fct=self.e_quitter_tray,
            sht_1=PaKeys.SHIFT,
            sht_2=PaKeys.ESCAPE
        )

        # self.tray_menu.addSeparator()

        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()
    def TEST_SQL(self):
        if not CoSql().TEST_CO():
            MsgBox.ALERTE(title="Erreur SQL", msg="Une erreur est survenue lors de la connexion à la base de données.")
            quit()
    def INIT(self, *args):
        for fct in args:
            splash_screen.lb_chargement.setText(fct[1])
            splash_screen.pg_chargement.setValue(splash_screen.pg_chargement.value() + 100 / len(args))
            time.sleep(0.2)
            fct[0]()

        splash_screen.lb_chargement.setText("Lancement de l'application")
        splash_screen.pg_chargement.setValue(100)
        time.sleep(1)
    ############################
    ##    /INITIALISATION     ##
    ############################


    #####################
    ##     ACTIONS     ##
    #####################
    def a_set_marche(self):
        match self.cb_marche.currentText():
            case "RIP24": self.marche = 24
            case "RIP40": self.marche = 40
            case "RIP47": self.marche = 47
        self.f_maj_dlg()
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_add_dlg(self):
        FormDlgBox.ADD(marche=self.marche)
        self.f_maj_dlg()
    def f_pbmenu_exportdlg(self):
        if self.pb_menu_rip24.isChecked(): idx = 0
        elif self.pb_menu_rip40.isChecked(): idx = 1
        elif self.pb_menu_rip47.isChecked(): idx = 2
        else: return

        self.cb_marche.setCurrentIndex(idx)
        self.stk_main.setCurrentWidget(self.pg_dlg)
    def f_pbdlg_menu(self):
        idx = self.cb_marche.currentIndex()

        match idx:
            case 0: self.pb_menu_rip24.setChecked(True)
            case 1: self.pb_menu_rip40.setChecked(True)
            case 2: self.pb_menu_rip47.setChecked(True)

        self.stk_main.setCurrentWidget(self.pg_menu)

    def f_maj_dlg(self):
        while self.glay_dlg.count():
            child = self.glay_dlg.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if self.pb_filtre_atraiter.isChecked():
            dlgs = CoSql().GET_V_DLG(marche=self.marche, table='v_dlg_a_faire')
        elif self.pb_filtre_tout.isChecked():
            dlgs = CoSql().GET_V_DLG(marche=self.marche, table='v_dlg')
        elif self.pb_filtre_fait.isChecked():
            dlgs = CoSql().GET_V_DLG(marche=self.marche, table='v_dlg_fait')
        else:
            return

        pb_dlg = {}
        ligne_conc = 0
        i_init = 0

        for dlg in dlgs:
            last_export = str(CoSql().GET_LAST_EXPORT_FROM_DLG(dl_id=dlg[0], col='et_rgb')[0])
            rgb_str = last_export.split(r"|")
            rgb = int(rgb_str[0]), int(rgb_str[1]), int(rgb_str[2]), int(rgb_str[3])

            _date_fr = str(dlg[6])
            _date_fr_s = _date_fr.split(r"-")
            date_fr = f"{_date_fr_s[2]}/{_date_fr_s[1]}/{_date_fr_s[0]}"

            name_dlg = f"{dlg[7]}-{dlg[8]}\nNRO{dlg[2]}-PM{dlg[3]}\n{dlg[4]}\n{dlg[9]}-V{dlg[10]}\n{date_fr}"

            pb_dlg[dlg[0]] = QtWidgets.QPushButton(name_dlg)
            pb_dlg[dlg[0]].setObjectName(str(dlg[0]))
            pb_dlg[dlg[0]].clicked.connect(functools.partial(self.f_dlg_click, dlg[0], rgb, name_dlg))

            MyPushButton.Base(pb_dlg[dlg[0]]).DLG(rgb)

            if 4 < ligne_conc < 9:
                ligne_conc -= 5
                i_init += 1

            self.glay_dlg.addWidget(pb_dlg[dlg[0]], i_init, ligne_conc, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            ligne_conc += 1

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.glay_dlg.addItem(spacerItem, i_init + 1, 0, 1, 1)
    def f_dlg_click(self, dlg_id, rgb, name_dlg):
        DlgBox.EDIT(dlg_id=dlg_id, rgb=rgb, name_dlg=name_dlg)
        self.f_maj_dlg()
    #######################
    ##    /FONCTIONS     ##
    #######################


    ###################
    ##     EVENT     ##
    ###################
    def e_resize_screen(self):
        if Config.resize:
            self.setMinimumWidth(Config.widht)
            self.setMinimumHeight(Config.height)
        else:
            self.setFixedWidth(Config.widht)
            self.setFixedHeight(Config.height)
    #####
    def traySingleClick(self):
        screen = QtWidgets.QApplication.primaryScreen().availableGeometry()
        widget = toolBox.geometry()

        toolBox.open()
        toolBox.show()
        toolBox.activateWindow()

        toolBox.move(screen.width()-widget.width(), screen.height()-widget.height())
    def trayDoubleClick(self):
        self.timer_double_click.stop()
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)
    def trayActivate(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            self.timer_double_click.start(app.doubleClickInterval())

        elif reason == QtWidgets.QSystemTrayIcon.DoubleClick:
            self.trayDoubleClick()
    def e_quitter(self):
        """Permet de quitter l'application"""
        if not Config.auto_close:
            self.hide()
        elif ResponseBox.QUITTER():
            app.quit()
    def e_quitter_tray(self):
        self.show()
        fen.activateWindow()

        if fen.windowState() == QtCore.Qt.WindowMinimized:
            fen.setWindowState(QtCore.Qt.WindowActive)

        if ResponseBox.QUITTER():
            app.quit()
    #####
    def closeEvent(self, event):
        event.accept()
        app.quit()
    ###################
    ##    /EVENT     ##
    ###################


if __name__ == "__main__":
    if Config.debug:
        Functions().GEN_SVG()

    app = QtWidgets.QApplication(sys.argv)
    splash_screen = SplashScreen()
    splash_screen.open()
    toolBox = ToolBoxUi()
    app.processEvents()

    fen = main()
    fen.show()

    sys.exit(app.exec())
