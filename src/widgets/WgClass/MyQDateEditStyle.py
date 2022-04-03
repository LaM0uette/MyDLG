from .MyQDateEdit import MyQDateEdit
from src.lib.globals import v_wg
from src.lib.palettes import *



class Style(MyQDateEdit):
    def __init__(
            self,
            widget,
            size_policy=v_wg.SIZE_POLICY,
            dim=v_wg.DIM_WG,
            font=v_wg.FONT,
            cursor=v_wg.CUR_ACTION,
            focus_policy=v_wg.FOCUS_POLICY,
            layout_direction=v_wg.LAYOUT_DIRECTION,

            wrapping=False,
            frame=False,
            align=DcAlign.Base,
            read_only=False,
            button_symbols=PaButtonSymbols.PLUS_MINUS,
            accelerated=True,

            date_time=DcDateTime.Base,
            calendar_popup=True,

            background=v_wg.BACKGROUND,
            background_header=v_wg.BACKGROUND,
            background_item=v_wg.BACKGROUND,
            foreground=v_wg.FOREGROUND,
            foreground_header=v_wg.FOREGROUND,
            foreground_item=v_wg.FOREGROUND,
            img=v_wg.IMG,
            border=v_wg.BORDER,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated,date_time,calendar_popup)

        font_size = PaFont.H4
        bg_mois=PaRgb.TH2
        fg_mois=PaRgb.TH1

        border_day_size = PaStyleBase.BORDER,
        border_day_style = "solid",
        border_day_rgb = PaRgb.BN1,

        style = f"""
                /* WIDGET */
                QDateEdit {{
                background-color: rgba{background.base};
                color: rgba{foreground.base};
                selection-background-color: rgba{background.selection};
                selection-color: rgba{foreground.selection};
                }}
                QDateEdit:hover {{
                background-color: rgba{background.hover};
                color: rgba{foreground.hover};
                }}

                /* IMG CALENDRIER */
                QDateEdit::drop-down {{
                image: url({f"{img.base}{img.base_rgb}.svg"});
                width: {img.width}px;
                height: {img.height}px;
                margin-top: {img.margin[0]}px;
                margin-bottom: {img.margin[1]}px;
                margin-right: {img.margin[2]}px;
                margin-left: {img.margin[3]}px;
                }}
                QDateEdit::drop-down:hover {{
                image: url({f"{img.base_hover}{img.base_hover_rgb}.svg"});
                }}

                /* WIDGETS */
                QCalendarWidget QWidget {{
                alternate-background-color: rgba{bg_mois};
                color: rgb{fg_mois};
                }}

                /* TOOL BUTTON */
                QCalendarWidget QToolButton {{
                font-size: {font_size}px;
                background-color: rgba{background_header.base};
                color: rgba{foreground_header.base};
                }}
                QCalendarWidget QToolButton:hover {{
                background-color: rgba{background_header.hover};
                color: rgba{foreground_header.hover};
                }}

                /* FLECHE GAUCHE DROITE */
                QToolButton#qt_calendar_nextmonth  {{
                qproperty-icon: url({f"{img.right}{img.right_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}
                QToolButton#qt_calendar_prevmonth {{
                qproperty-icon: url({f"{img.left}{img.left_rgb}.svg"});
                icon-size: {font_size}px, {font_size}px;
                }}

                /* MENU DEROULANT */
                QCalendarWidget QMenu {{
                width: 150px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{background_header.base};
                color: rgba{foreground_header.base};
                }}

                /* SPIN BOX */
                QCalendarWidget QSpinBox {{
                width: 60px;
                font-size: {font_size}px;
                font-family: {font};
                background-color: rgba{background_header.base};
                color: rgba{foreground_header.base};
                selection-background-color: rgba{background_header.selection};
                selection-color: rgba{foreground_header.selection};
                }}

                /* JOURS */
                QCalendarWidget QAbstractItemView {{
                font-size: {font_size}px;
                font-family: {font};
                font-weight: 30;
                outline: 0px;
                }}
                QCalendarWidget QAbstractItemView:enabled {{
                background-color: rgba{background_item.base};
                color: rgba{foreground_item.base};
                selection-background-color: rgba{foreground_item.base};
                selection-color: rgba{background_item.base};
                }}
                QCalendarWidget QWidget:item:hover, QCalendarWidget QWidget:item:selected {{
                background-color: rgba{background_item.hover};
                color: rgba{foreground_item.hover};
                border: {border_day_size}px {border_day_style} rgba{border_day_rgb};
                }}

                /* BARRE HAUT */
                QCalendarWidget QWidget#qt_calendar_navigationbar {{
                background-color: rgba{background_header.base};
                }}

                /* BORDURES */
                .QDateEdit {{
                border-top: {border.base[0]}px {border.base_style} rgba{border.base_rgb};
                border-bottom: {border.base[1]}px {border.base_style} rgba{border.base_rgb};
                border-right: {border.base[2]}px {border.base_style} rgba{border.base_rgb};
                border-left: {border.base[3]}px {border.base_style} rgba{border.base_rgb};
                }}
                .QDateEdit:hover {{
                border-top: {border.hover[0]}px {border.hover_style} rgba{border.hover_rgb};
                border-bottom: {border.hover[1]}px {border.hover_style} rgba{border.hover_rgb}
                border-right: {border.hover[2]}px {border.hover_style} rgba{border.hover_rgb};
                border-left: {border.hover[3]}px {border.hover_style} rgba{border.hover_rgb};
                }}

                /* RAYONS */
                .QDateEdit {{
                border-top-right-radius: {border.radius[0]}px;
                border-top-left-radius: {border.radius[1]}px;
                border-bottom-right-radius: {border.radius[2]}px;
                border-bottom-left-radius: {border.radius[3]}px;
                }}"""
        widget.setStyleSheet(style)