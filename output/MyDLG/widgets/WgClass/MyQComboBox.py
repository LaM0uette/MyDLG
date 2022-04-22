from .MyQWidget import MyQWidget


class MyQComboBox(MyQWidget):
    def __init__(
            self,
            widget,
            size_policy,
            dim,
            font,
            cursor,
            focus_policy,
            layout_direction,

            editable,
            max_visible_items,
            insert_policy,
            set_frame,
            align,
    ):
        super().__init__(widget,size_policy,dim,font,cursor,focus_policy,layout_direction)

        widget.setEditable(editable)
        widget.setMaxVisibleItems(max_visible_items)
        widget.setInsertPolicy(insert_policy)
        widget.setFrame(set_frame)

        if align.horizontal and editable: widget.lineEdit().setAlignment(align.horizontal)
