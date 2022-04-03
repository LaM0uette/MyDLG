from PySide6 import QtCore, QtWidgets

from src import *
from src.gui.ui import dlg_ui
from src.gui.events.Event import Event
from src.gui.dlg.MsgBox.MsgBox import MsgBox


class DlgBoxDlg(dlg_ui.Ui_Dlg, QtWidgets.QDialog):
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
            dlg_id,
            rgb,
            name_dlg,
    ):
        super(DlgBoxDlg, self).__init__()

        self.title = title
        self.ico = ico
        self.ico_rgb = ico_rgb
        self.txt_ok = txt_ok
        self.width = width
        self.height = height
        self.opacity = opacity
        self.dlg_id = dlg_id
        self.rgb = rgb
        self.name_dlg = name_dlg

        self.INIT()

        print(self.dlg_id)

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
        ### QPushButton ###
        MyPushButton.Dlg(self.pb_ok).ok()
        MyPushButton.MenuTop(self.pb_mt_quitter).quitter()

        MyPushButton.Base(self.pb_dlg).DLG_simple(self.rgb)

        all_rgb = CoSql().GET_ALL_ETATS_RGB()

        MyPushButton.Base(self.pb_edit_afa).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[0][0]))
        MyPushButton.Base(self.pb_edit_gex).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[1][0]))
        MyPushButton.Base(self.pb_edit_cma).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[2][0]))
        MyPushButton.Base(self.pb_edit_cch).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[3][0]))
        MyPushButton.Base(self.pb_edit_edl).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[4][0]))
        MyPushButton.Base(self.pb_edit_eok).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[5][0]))
        MyPushButton.Base(self.pb_edit_dok).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[6][0]))
        MyPushButton.Base(self.pb_edit_dno).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[7][0]))
        MyPushButton.Base(self.pb_edit_pok).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[8][0]))
        MyPushButton.Base(self.pb_edit_pno).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[9][0]))
        MyPushButton.Base(self.pb_edit_lcl).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[10][0]))
        MyPushButton.Base(self.pb_edit_pau).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[11][0]))
        MyPushButton.Base(self.pb_edit_ann).DLG_edit(self.a_tuple_from_text_rgb(all_rgb[12][0]))
        ### /QPushButton ###


        ### QListWidget ###
        MyListWidget.Base(self.lw_dlg).DLG()
        ### /QListWidget ###


        ### QFrame ###
        MyFrame.Menu(self.fr_menu_top).top()
        MyFrame.Cadre(self.fr_main).th2_fin()
        MyFrame.Dlg(self.fr_body).th(rgb=PaRgb.TH1)
        MyFrame.Menu(self.fr_dlg_bottom).bottom_dlg()
        MyFrame.Cadre(self.fr_dlg_body).th3()
        ### /QFrame ###
        #lw_dlg


        ### QLabel ###
        MyLabel.Base(self.lb_mt_ico).ico_custom(img=self.ico, img_rgb=self.ico_rgb)
        MyLabel.Base(self.lb_mt_nom).Transparent(font=PaFont.HH3)
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

        # DLG
        self.pb_dlg.setText(self.name_dlg)
    def IN_CONNECTIONS(self):
        ## Menu_top
        self.pb_mt_quitter.clicked.connect(lambda: self.close())

        # pb dlg
        self.pb_ok.clicked.connect(self.f_ok)
    def IN_ACT(self):
        self.f_maj_all_exports()
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
    def a_tuple_from_text_rgb(self, rgb):
        rgb_str = rgb.split(r"|")
        _rgb = int(rgb_str[0]), int(rgb_str[1]), int(rgb_str[2]), int(rgb_str[3])
        return _rgb
    #####################
    ##    /ACTIONS     ##
    #####################


    #######################
    ##     FONCTIONS     ##
    #######################
    def f_maj_all_exports(self):
        exps = CoSql().GET_ALL_EXPORTS_ONE_DLG(self.dlg_id)

        for exp in exps:
            _code = str(exp[0])
            code = _code.split("_")

            _datetime = str(exp[1])

            _date = str(_datetime.split(r" ")[0])
            date = _date.split(r"-")

            _heure = str(_datetime.split(r" ")[1])
            heure = _heure.split(r":")

            date_fr = f"{date[2]}/{date[1]}/{date[0]}"
            heure_fr = f"{heure[0]}/{heure[1]}/{heure[1]}"

            self.lw_dlg.addItem(f"{code[1]} - {date_fr} à {heure_fr}")

    #####

    def f_ok(self):

        self.close()
    #######################
    ##    /FONCTIONS     ##
    #######################
