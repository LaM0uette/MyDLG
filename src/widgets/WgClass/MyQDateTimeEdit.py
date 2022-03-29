from .MyQAbstractSpinBox import MyQAbstractSpinBox


class MyQDateTimeEdit(MyQAbstractSpinBox):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            wrapping,
            frame,
            align,
            read_only,
            button_symbols,
            accelerated,

            date_time,
            calendar_popup,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction,wrapping,frame,align,read_only,button_symbols,accelerated)

        widget.setDateTime(date_time.date_time)
        widget.setCalendarPopup(calendar_popup)
