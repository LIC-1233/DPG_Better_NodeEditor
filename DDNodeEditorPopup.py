from typing import Any

import dearpygui.dearpygui as dpg

from i18 import _
from NodeEditor import NodeEditor
from utils.Base import BaseModel  # type: ignore


class NodeEditorPopup:
    def __init__(self):
        self.node_editor: NodeEditor

    def set_node_editor(self, node_editor: NodeEditor):
        self.node_editor = node_editor

    # 编辑器右键菜单
    @staticmethod
    def node_editor_pop_wnd(node_atr_map: dict[int | str, list[int | str]]) -> Any:
        with dpg.window(popup=True, min_size=(0, 0)) as nodeditor_popup_wnd:
            with dpg.menu(label="node_editor"):
                for category in ["node_type_category_1", "node_type_category_2"]:
                    dpg.add_menu_item(label=category)
                    dpg.add_separator()
        return nodeditor_popup_wnd

    # 节点右键菜单
    def node_pop_wnd(
        self, node_atr_map: dict[int | str, list[int | str]], node_id: int | str
    ) -> Any:
        with dpg.window(popup=True, min_size=(0, 0)) as node_popup_wnd:
            dpg.add_text("node")
        return node_popup_wnd

    # 属性右键菜单
    def node_attribute_pop_wnd(
        self, node_atr_map: dict[int | str, list[int | str]], node_attr_id: int | str
    ) -> Any:
        user_data = dpg.get_item_user_data(node_attr_id)
        print(node_attr_id)
        print(user_data)

        # 非BaseModel属性
        if (
            user_data is None
            or not isinstance(user_data, tuple)
            or not len(user_data) == 2
            or not isinstance(user_data[0], BaseModel)
            or not isinstance(user_data[1], str)
        ):
            with dpg.window(popup=True, min_size=(0, 0)) as node_attribute_popup_wnd:
                dpg.add_text("no menu")
                return node_attribute_popup_wnd

        # BaseModel属性
        model: BaseModel = dpg.get_item_user_data(node_attr_id)[0]  # type: ignore
        feild: str = dpg.get_item_user_data(node_attr_id)[1]  # type: ignore

        require = model.model_fields[feild].is_required()

        with dpg.window(popup=True, min_size=(0, 0)) as node_attribute_popup_wnd:
            if require is False:
                dpg.add_menu_item(
                    label=_("delete attribute"),
                    callback=lambda: self.node_editor.delete_item(node_attr_id),
                )
            with dpg.menu(label="node_editor"):
                dpg.add_menu_item(label=model.__class__.__name__ + "." + feild)
        return node_attribute_popup_wnd

    # 属性右键菜单
    def node_link_pop_wnd(self) -> Any:
        with dpg.window(popup=True, min_size=(0, 0)) as node_attribute_popup_wnd:
            dpg.add_text("node_link")
        return node_attribute_popup_wnd
