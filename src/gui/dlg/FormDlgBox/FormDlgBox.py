from functools import partial

from src import *
from src.gui.dlg.FormDlgBox.FormDlgBoxDlg import FormDlgBoxDlg


class FormDlgBox:

    @staticmethod
    def __rtn(title, msg, ico, ico_rgb, txt_ok, width, height, opacity, marche):
        form_dlg = FormDlgBoxDlg(
            title=title,
            msg=msg,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            width=width,
            height=height,
            opacity=opacity,
            marche=marche,
        )
        form_dlg.exec()


    __WIDTH, __HEIGHT, __OPACITY = 650, 800, 1

    ADD = partial(__rtn, title="INFO", msg="", ico=PaImg.INFO, ico_rgb="th3", txt_ok="Ok", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
