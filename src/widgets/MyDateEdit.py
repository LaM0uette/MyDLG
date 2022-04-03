from .WgClass.MyQDateEditStyle import Style
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

            focus_policy=PaFocusPolicy.STRONG,

            img=DcImg.Base(
                base=PaImg.CALENDRIER,
                base_hover=PaImg.CALENDRIER,
                base_rgb="",
                base_hover_rgb="",
            )
        )
    def Transparent(self):
        Style(
            widget=self.widget,
        )
