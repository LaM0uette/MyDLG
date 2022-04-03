from .WgClass.MyQScrollAreaStyle import Style
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
        )

    def Main(self):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TH1),
        )
    def DLG(self):
        Style(
            widget=self.widget,

            background=DcRgbBg.Base(gen=PaRgb.TH1),

            border=DcBorder.Base(radius=(5, )*4)
        )
