import datetime

from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import form_dlg_ui
from src.gui.events.Event import Event
from src.gui.dlg.MsgBox.MsgBox import MsgBox


class FormDlgBoxDlg(form_dlg_ui.Ui_FormDlg, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(
            self,
            title,
            ico,
            ico_rgb,
            txt_ok,
            width,
            height,
            opacity,
            marche,
    ):
        super(FormDlgBoxDlg, self).__init__()

        self.title = title
        self.ico = ico
        self.ico_rgb = ico_rgb
        self.txt_ok = txt_ok
        self.width = width
        self.height = height
        self.opacity = opacity

        match marche:
            case "RIP24": self.marche = 24
            case "RIP40": self.marche = 40
            case "RIP47": self.marche = 47

        self.INIT()

        ### CREATION DES EVENT ###
        self.evt = Event(self)
        self.mousePressEvent = self.evt.mousePressEvent
        self.mouseMoveEvent = self.evt.mouseMoveEvent

    ############################
    ##     INITIALISATION     ##
    ############################
    def IN_BASE(self):
        ### Fenetre ###
        self.setWindowTitle(self.title)
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        self.setWindowOpacity(self.opacity)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGraphicsEffect(PaShadow.OMBRE_PORTEE(self))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
    def IN_SETUP_UI(self):
        ### Ui ###
        self.setupUi(self)
        self.glay_main.setContentsMargins(v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP, v_gb.MARGIN_APP)
    def IN_CLASSE(self):
        ### QFrame ###
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Cadre(self.fr_main).th2_fin()
        MyFrame.Dlg(self.fr_body).th(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_msg_bottom).bottom_dlg()
        ### /QFrame ###


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.ico_rgb)
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
        ### /QLabel ###


        ### QPushButton ###
        MyPushButton.Dlg(self.pb_ok).ok()
        MyPushButton.MenuTop(self.pb_mt_quitter).quitter()
        ### /QPushButton ###


        ### QComboBox ###
        for wg in [
            self.cb_phase, self.cb_td
        ]: MyComboBox.Base(wg).Base()

        for wg in [
            self.cb_nro, self.cb_pm, self.cb_refcode3
        ]: MyComboBox.Base(wg).BaseEdit()
        ### /QComboBox ###


        ### QSpinBox ###
        MySpinBox.PlusMinus(self.sb_phase).Petit()
        for wg in [self.sb_livraison, self.sb_version]: MySpinBox.PlusMinus(wg).NumPetit()
        ### /QSpinBox ###


        ### QDateEdit ###
        MyDateEdit.Base(self.de_date_prev).Base()
        ### /QDateEdit ###


        ### QLabel ###
        for wg in [
            self.lb_phase, self.lb_td, self.lb_nro, self.lb_pm, self.lb_refcode3, self.lb_livraison, self.lb_version, self.lb_date_prev
        ]: MyLabel.Base(wg).Transparent()
        ### /QLabel ###
    def IN_WG(self):
        # Base
        self.setCursor(Functions().SET_CURSOR(cur=PaCur.SOURIS))

        # Frame menu_top
        self.fr_menu_top.setFixedHeight(PaDim.H9)

        # Menu_top
        self.lb_mt_nom.setText(self.title)

        # pb dlg
        self.pb_ok.setText(self.txt_ok)
        self.pb_ok.setDefault(True)


        # FORM DLG
        for phase in CoSql().GET_ALL_PHASE():
            self.cb_phase.addItem(phase[1])
        self.cb_phase.setCurrentIndex(1)

        self.cb_td.addItems(["Tout", "Transport", "Distribution"])

        self.cb_nro.addItem("")
        self.cb_pm.addItem("")
        self.cb_refcode3.addItem("")

        for nro in CoSql().GET_ALL_NRO(self.marche):
            self.cb_nro.addItem(str(nro[0]))
        for pm in CoSql().GET_ALL_PM(self.marche):
            self.cb_pm.addItem(str(pm[0]))
        for refcode3 in CoSql().GET_ALL_REFCODE3(self.marche):
            self.cb_refcode3.addItem(str(refcode3[0]))
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_ok.clicked.connect(self.f_ok)

        # Form dlg
        self.cb_phase.currentTextChanged.connect(self.a_phase_changed)
        self.cb_nro.editTextChanged.connect(self.f_get_refcode3)
        self.cb_pm.editTextChanged.connect(self.f_get_refcode3)
        self.cb_refcode3.editTextChanged.connect(self.f_get_nro_pm)
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        self.sb_phase.setValue(100)
    def INIT(self):
        self.IN_BASE()
        self.IN_SETUP_UI()
        self.IN_CLASSE()
        self.IN_WG()
        self.IN_CONNECTIONS()
        self.IN_ACT()
        self.IN_WG_BASE()
    ############################
    ##    /INITIALISATION     ##
    ############################


    #####################
    ##     ACTIONS     ##
    #####################
    def a_phase_changed(self):
        if self.cb_phase.currentText() == "DOE":
            self.sb_phase.setVisible(True)
        else:
            self.sb_phase.setVisible(False)
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_get_refcode3(self):
        try:
            refcode3 = CoSql().GET_REFCODE3(int(self.cb_nro.currentText()), int(self.cb_pm.currentText()))
            self.cb_refcode3.setCurrentText(refcode3[0])
        except: pass
    def f_get_nro_pm(self):
        try:
            req = CoSql().GET_NRO_PM(self.cb_refcode3.currentText())
            nro = str(req[0])
            pm = str(req[1])

            self.cb_nro.setCurrentText(nro)
            self.cb_pm.setCurrentText(pm)
        except: pass

    #####

    def f_ok(self):
        err = "Il manque des informations :\n"

        nro = self.cb_nro.currentText()
        pm = self.cb_pm.currentText()
        refcode3 = self.cb_refcode3.currentText()

        date_b = self.de_date_prev.date()
        date = datetime.date(date_b.year(), date_b.month(), date_b.day()).strftime("%Y-%m-%d")

        match self.cb_phase.currentText():
            case "EXE": phase = "EXE"
            case "PRO": phase = "PRO"
            case "DOE": phase = f"DOE_{self.sb_phase.value()}%"
            case _: phase = "NA"

        match self.cb_td.currentText():
            case "Tout": td = "TD"
            case "Transport": td = "T"
            case "Distribution": td = "D"
            case _: td = "TD"

        no_livraison = self.sb_livraison.value()
        no_version = self.sb_version.value()


        if len(nro) < 1:
            err += " | NRO | "
        if len(pm) < 1:
            err += " | PM | "
        if len(self.cb_refcode3.currentText()) < 1:
            err += " | REFCODE3 | "


        if err != "Il manque des informations :\n":
            MsgBox.ALERTE(title="ERREUR", msg=err)
            return

        dlg = CoSql().GET_DLG(
            refcode3=refcode3,
            phase=phase,
            td=td,
            num_livraison=no_livraison,
            num_version=no_version
        )

        if not dlg:
            CoSql().ADD_ZONE_DLG(self.marche, nro, pm, refcode3)
            CoSql().ADD_DLG(refcode3, date, phase, td, no_livraison, no_version)
        else:
            MsgBox.ALERTE(title="ERREUR", msg="Ce DLG existe déjà.")
            return

        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
