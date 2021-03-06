from .WgClass.MyQPushButtonStyle import Style
from src.lib.palettes import *


##################
##     BASE     ##
##################
class Base:
    def __init__(self, widget):
        self.widget = widget

    def Base(self):
        Style(
            widget=self.widget,
        )
    def Transparent(self):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1
            ),
        )

    def MenuPB(self):
        Style(
            widget=self.widget,
            font=PaFont.HH1,

            dim=DcDim.Base(
                fixed_width=PaDim.H4,
                fixed_height=PaDim.H4,
            ),

            border=DcBorder.Base(
                radius=(3, 3, 0, 0)
            )
        )
    def RetourMenu(self):
        Style(
            widget=self.widget,
            pb_type="ico_click",

            dim=DcDim.Base(
                fixed_width=PaDim.H9,
                fixed_height=PaDim.H9,
            ),

            img=DcImg.Base(
                base=PaImg.MENU,
                base_hover=PaImg.MENU,
                base_rgb="th1",
                base_hover_rgb="bn1",
            ),

            border=DcBorder.Base(
                radius=(0, 3, 0, 3)
            )
        )
    def SearchDlg(self):
        Style(
            widget=self.widget,
            pb_type="ico_click",

            dim=DcDim.Base(
                fixed_width=PaDim.H9,
                fixed_height=PaDim.H9,
            ),

            img=DcImg.Base(
                base=PaImg.LOUPE,
                base_hover=PaImg.LOUPE,
                base_rgb="th1",
                base_hover_rgb="bn1",
            ),

            border=DcBorder.Base(
                gen=(0, 2, 0, 0),
                gen_rgb=PaRgb.TH2,
                radius=(0, )*4
            )
        )

    def DlgTools(self):
        Style(
            widget=self.widget,
            pb_type="ico_click",
            dim=DcDim.Base(
                fixed_width=PaDim.H7,
                fixed_height=PaDim.H7,
            ),
            img=DcImg.Base(
                base=PaImg.PLUS,
                base_hover=PaImg.PLUS,
                base_rgb="th1",
                base_hover_rgb="bn1",
            ),
            border=DcBorder.Base(
                radius=(0, )*4
            )
        )

    def DLG(self, rgb):
        Style(
            widget=self.widget,

            pb_type="shadow",

            dim=DcDim.Base(
                fixed_width=PaDim.H5,
                fixed_height=PaDim.H5,
            ),

            font=PaFont.HH3,

            background=DcRgbBg.Base(
                gen=PaRgb.TH1
            ),

            foreground=DcRgbBg.Base(
                gen=PaRgb.TH3
            ),

            border=DcBorder.Base(
                gen=(3, )*4,
                gen_rgb=rgb,
                radius=(15, )*4
            )
        )
    def DLG_simple(self, rgb):
        Style(
            widget=self.widget,

            dim=DcDim.Base(
                fixed_width=PaDim.H4,
                fixed_height=PaDim.H4,
            ),

            cursor=PaCur.SOURIS,

            font=PaFont.HH3,

            background=DcRgbBg.Base(
                gen=PaRgb.TH1
            ),

            foreground=DcRgbBg.Base(
                gen=PaRgb.TH3
            ),

            border=DcBorder.Base(
                gen=(3, )*4,
                gen_rgb=rgb,
                radius=(15, )*4
            )
        )
    def DLG_edit(self, rgb):
        Style(
            widget=self.widget,

            checkable=True,

            auto_actions=DcAutoActions.Base(
                auto_exclusive=True
            ),

            size_policy=DcSizePolicy.Base(
                horizontal=PaSizePolicy.EXPANDING
            ),

            dim=DcDim.Base(
                fixed_height=PaDim.H9+5,
            ),

            background=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.TH1,
                pressed=PaRgb.TH1,
                checked=rgb,
                checked_hover=rgb,
                checked_pressed=rgb,
            ),

            foreground=DcRgbBg.Base(
                gen=PaRgb.TH3
            ),

            border=DcBorder.Base(
                gen=(3, )*4,
                gen_rgb=rgb,
                radius=(3, )*4
            )
        )


######################
##     MENU TOP     ##
######################
class MenuTop:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(
            self,
            img=PaImg.MAIN,
            img_rgb="th2",
    ):
        Style(
            self.widget,
            pb_type="zoom",
            dim=DcDim.Base(fixed_width=PaDim.H9 * 1.2, fixed_height=PaDim.H9),
            cursor=PaCur.SOURIS_MAIN,

            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground=DcRgbFg.Base(
                checked=PaRgb.TH3
            ),
            img=DcImg.Base(
                base=img,
                base_rgb=img_rgb
            ),
        )

    def option(self):
        self._rtn(
            img=PaImg.OPTION
        )
    def reduire(self):
        self._rtn(
            img=PaImg.REDUIRE,
            img_rgb="bn1"
        )
    def agrandir(self):
        self._rtn(
            img=PaImg.AGRANDIR,
            img_rgb="th3"
        )
    def quitter(self):
        self._rtn(
            img=PaImg.QUITTER,
            img_rgb="bn2"
        )


##################
##     MENU     ##
##################
class MenuMarche:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(self, rd):
        Style(
            widget=self.widget,
            auto_actions=DcAutoActions.Base(
                auto_exclusive=True
            ),
            checkable=True,

            dim=DcDim.Base(
                fixed_height=PaDim.H9,
            ),

            background=DcRgbBg.Base(
                gen=PaRgb.TH3
            ),

            foreground=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.TH1,
                checked=PaRgb.BN1,
                checked_hover=PaRgb.BN1,
            ),

            border=DcBorder.Base(
                gen=(3, 0, 0, 0),
                base_rgb=PaRgb.TH3,
                hover_rgb=PaRgb.TH3,
                checked_rgb=PaRgb.BN1,
                checked_hover_rgb=PaRgb.BN1,
                radius=rd
            )
        )

    def Rip24(self): self._rtn(rd=(0, 0, 0, 3))
    def Rip40(self): self._rtn(rd=(0, 0, 0, 0))
    def Rip47(self): self._rtn(rd=(0, 0, 3, 0))


#################
##     DLG     ##
#################
class DlgFiltre:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(self, rd):
        Style(
            widget=self.widget,
            auto_actions=DcAutoActions.Base(
                auto_exclusive=True
            ),
            checkable=True,

            dim=DcDim.Base(
                fixed_width=PaDim.H6,
                fixed_height=PaDim.H9,
            ),

            background=DcRgbBg.Base(
                base=PaRgb.TH3,
                hover=PaRgb.TH3,
                checked=PaRgb.TH2,
                checked_hover=PaRgb.TH2,
            ),

            foreground=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.TH1,
                checked=PaRgb.BN1,
                checked_hover=PaRgb.BN1,
            ),

            border=DcBorder.Base(
                radius=rd
            )
        )

    def ATraiter(self): self._rtn(rd=(3, 3, 3, 3))
    def Tout(self): self._rtn(rd=(3, 3, 3, 3))
    def Fait(self): self._rtn(rd=(3, 3, 3, 3))


#################
##     TXT     ##
#################
class Txt:
    def __init__(self, widget):
        self.widget = widget

    def txt(self):
        Style(
            self.widget,
            background=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.TH3,
                pressed=PaRgb.TH3,
                checked=PaRgb.TH3,
                checked_hover=PaRgb.TH1,
                checked_pressed=PaRgb.TH1,
            ),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH3,
                hover=PaRgb.TH1,
                checked=PaRgb.TH1,
                checked_hover=PaRgb.TH3
            ),
            border=DcBorder.Base(
                gen=(PaStyleBase.BORDER,) * 4,
                gen_rgb=PaRgb.TH3
            )
        )
    def inverse(self):
        Style(
            self.widget,
            background=DcRgbBg.Base(
                base=PaRgb.TH3,
                hover=PaRgb.TH1,
                pressed=PaRgb.TH1,
                checked=PaRgb.TH1,
                checked_hover=PaRgb.TH3,
                checked_pressed=PaRgb.TH3,
            ),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.TH3,
                checked=PaRgb.TH3,
                checked_hover=PaRgb.TH1
            ),
            border=DcBorder.Base(
                gen=(PaStyleBase.BORDER,) * 4,
                gen_rgb=PaRgb.TH3
            )
        )


#################
##     DLG     ##
#################
class Dlg:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(
            self,
            background,
            foreground,
            bd_rgb=PaRgb.BN1,
    ):
        Style(
            self.widget,

            size_policy=DcSizePolicy.Base(
                vertical=PaSizePolicy.EXPANDING
            ),

            dim=DcDim.Base(
                fixed_width=PaDim.H6,
                fixed_height=None,
            ),

            background=background,
            foreground=foreground,
            border=DcBorder.Base(
                gen=(PaStyleBase.BORDER,) * 4,
                gen_rgb=bd_rgb
            )
        )

    def ok(self):
        self._rtn(
            background=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.BN1,
                pressed=PaRgb.BN1,
            ),
            foreground=DcRgbFg.Base(
                base=PaRgb.BN1,
                hover=PaRgb.TH1,
                pressed=PaRgb.TH1,
            ),

            bd_rgb=PaRgb.BN1,
        )
    def ok_inv(self):
        self._rtn(
            background=DcRgbBg.Base(
                base=PaRgb.BN1,
                hover=PaRgb.TH1,
                pressed=PaRgb.TH1,
            ),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.BN1,
                pressed=PaRgb.BN1,
            ),

            bd_rgb=PaRgb.BN1,
        )
    def nok(self):
        self._rtn(
            background=DcRgbBg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.BN2,
                pressed=PaRgb.BN2,
            ),
            foreground=DcRgbFg.Base(
                base=PaRgb.BN2,
                hover=PaRgb.TH1,
                pressed=PaRgb.TH1,
            ),

            bd_rgb=PaRgb.BN2,
        )
    def nok_inv(self):
        self._rtn(
            background=DcRgbBg.Base(
                base=PaRgb.BN2,
                hover=PaRgb.TH1,
                pressed=PaRgb.TH1,
            ),
            foreground=DcRgbFg.Base(
                base=PaRgb.TH1,
                hover=PaRgb.BN2,
                pressed=PaRgb.BN2,
            ),

            bd_rgb=PaRgb.BN2,
        )


###################
##     PLEIN     ##
###################
class Plein:
    def __init__(self, widget):
        self.widget = widget

    def _rtn(
            self,
            height=PaDim.H5,

            bg_gen=PaRgb.TR,
            fg_gen=PaRgb.TR,

            border_gen=(0, )*4,
            border_gen_rgb=PaRgb.TR,
            cursor=PaCur.MAIN
    ):
        Style(
            self.widget,
            dim=DcDim.Base(fixed_height=height),
            cursor=cursor,

            background=DcRgbBg.Base(gen=bg_gen),
            foreground=DcRgbFg.Base(gen=fg_gen),
            border=DcBorder.Base(
                gen=border_gen,
                gen_rgb=border_gen_rgb,
                radius=(0, )*4
            ),
        )

    def th1(self):
        self._rtn(
            bg_gen=PaRgb.TH1,
            fg_gen=PaRgb.TH3,
            border_gen=(PaStyleBase.BORDER,) * 4,
            border_gen_rgb=PaRgb.TH2,
        )
    def th2(self):
        self._rtn(
            bg_gen=PaRgb.TH2,
            fg_gen=PaRgb.TH3,
        )
    def th3(self):
        self._rtn(
            bg_gen=PaRgb.TH3,
            fg_gen=PaRgb.TH1,
        )
    def bn1(self):
        self._rtn(
            bg_gen=PaRgb.BN1,
            fg_gen=PaRgb.TH3,
        )
    def bn2(self):
        self._rtn(
            bg_gen=PaRgb.BN2,
            fg_gen=PaRgb.TH3,
        )
