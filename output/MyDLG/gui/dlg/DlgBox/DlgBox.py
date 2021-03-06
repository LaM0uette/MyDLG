from functools import partial

from src import *
from src.gui.dlg.DlgBox.DlgBoxDlg import DlgBoxDlg


class DlgBox:

    @staticmethod
    def __rtn(title, ico, ico_rgb, txt_ok, width, height, opacity, dlg_id, rgb, name_dlg):
        dlg = DlgBoxDlg(
            title=title,
            ico=ico,
            ico_rgb=ico_rgb,
            txt_ok=txt_ok,
            width=width,
            height=height,
            opacity=opacity,
            dlg_id=dlg_id,
            rgb=rgb,
            name_dlg=name_dlg,
        )
        dlg.exec()


    __WIDTH, __HEIGHT, __OPACITY = 800, 800, 1

    EDIT = partial(__rtn, title="Modification DLG", ico=PaImg.EDIT, ico_rgb="th3", txt_ok="Modifier", width=__WIDTH, height=__HEIGHT, opacity=__OPACITY)
