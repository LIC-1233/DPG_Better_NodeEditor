from typing import Any

import dearpygui.dearpygui as dpg  # type: ignore


class NodeEditorPopup:
    def __init__(self):
        pass

    # 编辑器右键菜单
    @staticmethod
    def node_editor_pop_wnd() -> Any:
        with dpg.window(popup=True, show=False, min_size=(0, 0)) as nodeditor_popup_wnd:
            with dpg.menu(label="添加节点"):
                for category in ["node_type_category_1", "node_type_category_2"]:
                    dpg.add_menu_item(label=category)
                    dpg.add_separator()
        return nodeditor_popup_wnd

    # 节点右键菜单
    @staticmethod
    def node_pop_wnd() -> Any:
        with dpg.window(popup=True, show=False, min_size=(0, 0)) as node_popup_wnd:
            dpg.add_text("test")
        return node_popup_wnd

    # 属性右键菜单
    @staticmethod
    def node_attribute_pop_wnd() -> Any:
        with dpg.window(
            popup=True, show=False, min_size=(0, 0)
        ) as node_attribute_popup_wnd:
            dpg.add_text("test")
        return node_attribute_popup_wnd
