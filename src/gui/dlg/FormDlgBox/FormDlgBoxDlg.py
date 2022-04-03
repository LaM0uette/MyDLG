from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import form_dlg_ui
from src.gui.events.Event import Event


class FormDlgBoxDlg(form_dlg_ui.Ui_FormDlg, QtWidgets.QDialog):
    dragPos: QtCore.QPoint

    def __init__(
            self,
            title,
            msg,
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
        self.msg = msg
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
            self.cb_phase, self.cb_td, self.cb_nro, self.cb_pm, self.cb_refcode3
        ]: MyComboBox.Base(wg).Base()
        ### /QComboBox ###


        ### QSpinBox ###
        MySpinBox.PlusMinus(self.sb_phase).Petit()
        ### /QSpinBox ###
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
        for phase in CoSql().GET_PHASE():
            self.cb_phase.addItem(phase[1])
        self.cb_phase.setCurrentIndex(1)

        self.cb_td.addItems(["Tout", "Transport", "Distribution"])

        self.cb_nro.addItem("")
        self.cb_pm.addItem("")
        self.cb_refcode3.addItem("")

        for nro in CoSql().GET_NRO(self.marche):
            self.cb_nro.addItem(str(nro[0]))
        for pm in CoSql().GET_PM(self.marche):
            self.cb_pm.addItem(str(pm[0]))
        for refcode3 in CoSql().GET_REFCODE3(self.marche):
            self.cb_refcode3.addItem(str(refcode3[0]))
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_ok.clicked.connect(lambda: self.close())

        # Form dlg
        self.cb_phase.currentTextChanged.connect(self.a_phase_changed)
    def IN_ACT(self):
        pass
    def IN_WG_BASE(self):
        pass
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