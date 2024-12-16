from abc import ABC, abstractmethod
from typing import Any, Callable

from dearpygui import dearpygui as dpg

from dd_game_type.base import BaseModel
from NodeEditor import NodeEditor
from utils.BiDirectionalDict import BiDirectionalDict


class NodeSection(ABC):
    def __init__(
        self,
        node_editor: "ModelNodeEditor",
        model: BaseModel,
        field_name: str,
        value: Any,
    ):
        self.node_editor = node_editor
        self.init(model, field_name, value)
        self.draw(model, field_name, value)

    @staticmethod
    @abstractmethod
    def condition(model: BaseModel, field_name: str, value: Any) -> bool: ...
    @abstractmethod
    def init(self, model: BaseModel, field_name: str, value: Any): ...
    def callback(self, attr_id: int | str, value: Any):
        self.node_editor.set_value_callback(attr_id, value)

    @abstractmethod
    def set_items_values(self, value: Any): ...
    @abstractmethod
    def draw(self, model: BaseModel, field_name: str, value: Any): ...


class BaseNodeSection(NodeSection):
    def init(self, model: BaseModel, field_name: str, value: Any):
        pass

    @staticmethod
    def condition(model: BaseModel, field_name: str, value: Any):
        if type(value) in [str, int, float, bool]:
            return True
        return False

    def item_callback(self, sender: int | str, appdata: Any, userdata: Any):
        return self.callback(self.attr_id, appdata)

    def set_items_values(self, value: Any):
        dpg.set_value(self.item_id, value)

    def draw(self, model: BaseModel, field_name: str, value: str | int | float | bool):
        field_info = model.model_fields[field_name]
        with self.node_editor.node_attribute(
            attribute_type=dpg.mvNode_Attr_Static, user_data=(model, field_name)
        ) as id:
            self.attr_id = id
            if isinstance(value, str):
                title = field_info.title or field_name
                self.item_id = dpg.add_input_text(
                    default_value=value, label=title, callback=self.item_callback
                )
            elif isinstance(value, bool):
                title = field_info.title or field_name
                self.item_id = dpg.add_checkbox(
                    default_value=value, label=title, callback=self.item_callback
                )
            elif isinstance(value, int):
                title = field_info.title or field_name
                self.item_id = dpg.add_input_int(
                    default_value=value, label=title, callback=self.item_callback
                )
            else:
                title = field_info.title or field_name
                self.item_id = dpg.add_input_float(
                    default_value=value, label=title, callback=self.item_callback
                )


class ModelNodeEditor(NodeEditor):
    def __init__(
        self,
        node_editor_popup: Callable[[dict[int | str, list[int | str]]], None],
        node_popup: Callable[[dict[int | str, list[int | str]], int | str], None],
        node_attribute_popup: Callable[
            [dict[int | str, list[int | str]], int | str], None
        ],
        check_link: Callable[[int | str, int | str], bool] | None = None,
        delink_callback: Callable[[int | str, int | str], None] | None = None,
    ):
        super().__init__(
            node_editor_popup,
            node_popup,
            node_attribute_popup,
            check_link,
            delink_callback,
        )

        self.model_data_manager: BiDirectionalDict[int | str, tuple[BaseModel, str]] = (
            BiDirectionalDict()
        )

    def set_value_callback(self, attr_id: int | str, value: Any):
        if attr_id not in self.model_data_manager:
            return
        for i in self.model_data_manager[attr_id]:
            setattr(i[0], i[1], value)
