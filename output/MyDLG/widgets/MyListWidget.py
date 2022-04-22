from .WgClass.MyQListWidgetStyle import Style
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
            border_item=DcBorder.Base(
                radius=(0,) * 4)
        )
    def DLG(self):
        Style(
            widget=self.widget,

            cursor=PaCur.SOURIS,

            dim=DcDim.Base(
                fixed_width=PaDim.H4,
            ),

            background=DcRgbBg.Base(
                gen=PaRgb.TH3,
            ),
            background_item=DcRgbBg.Base(
                gen=PaRgb.TH3,
            ),

            foreground=DcRgbBg.Base(
                gen=PaRgb.TH1
            ),
            foreground_item=DcRgbBg.Base(
                gen=PaRgb.TH1
            ),

            border=DcBorder.Base(
                radius=(3,) * 4),

            border_item=DcBorder.Base(
                radius=(3,) * 4)
        )
    def Transparent(self):
        Style(
            widget=self.widget,
            background=DcRgbBg.Base(gen=PaRgb.TR),
            foreground_item=DcRgbBg.Base(
                base=PaRgb.TH3,
                checked=PaRgb.BN1,
            ),
            border_item=DcBorder.Base(
                radius=(0,)*4)
        )
