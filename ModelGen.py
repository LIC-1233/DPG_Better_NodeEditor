from types import NoneType
from typing import Any, Callable, Literal, get_args, get_origin

from dearpygui import dearpygui as dpg
from pydantic.fields import FieldInfo

from dd_game_type.base import BaseModel
from NodeEditor import NodeEditor


class ModelNodeGenerator:
    def __init__(self, node_editor: NodeEditor) -> None:
        self.node_editor = node_editor
        self.dis_gen_types = [NoneType]
        self.gen_model_attribute_method: list[
            tuple[
                Callable[[type, FieldInfo], bool],
                Callable[[BaseModel, str, Any], int | str | None],
            ]
        ] = []
        self.register_base_method()

    def create_widget(
        self,
        field_name: str,
        model: BaseModel,
        field_info: FieldInfo,
        value: Any,
    ):
        anntation = type(value)
        title: str = field_info.title or field_name
        description = field_info.description or field_name
        is_list = False
        if anntation is list:
            is_list = True
            anntation = type(value[0])
        if issubclass(anntation, BaseModel):  # type: ignore
            with self.node_editor.node_attribute(
                user_data=(model, field_name),
                attribute_type=dpg.mvNode_Attr_Input,
            ):
                widget = dpg.add_text(title)
                with dpg.tooltip(widget):
                    dpg.add_text(description)
            return
        with self.node_editor.node_attribute(
            user_data=(model, field_name),
            attribute_type=dpg.mvNode_Attr_Static,
        ):
            if is_list:
                values = value
            else:
                values = [value]
            for value in values:
                if anntation is str:
                    widget = dpg.add_input_text(
                        default_value=value,
                        width=100,
                        label=title,
                    )
                    with dpg.tooltip(widget):
                        dpg.add_text(description)
                elif anntation is int:
                    widget = dpg.add_input_int(
                        default_value=value,
                        width=100,
                        label=title,
                    )
                    with dpg.tooltip(widget):
                        dpg.add_text(description)
                elif anntation is float:
                    widget = dpg.add_input_float(
                        default_value=value,
                        width=100,
                        label=title,
                    )
                    with dpg.tooltip(widget):
                        dpg.add_text(description)
                elif anntation is bool:
                    widget = dpg.add_checkbox(
                        default_value=value,
                        label=title,
                    )
                    with dpg.tooltip(widget):
                        dpg.add_text(description)
                elif get_origin(anntation) is Literal:
                    widget = dpg.add_combo(
                        items=get_args(anntation),
                        default_value=value,
                        width=100,
                        label=title,
                    )
                    with dpg.tooltip(widget):
                        dpg.add_text(description)
                else:
                    dpg.add_text(f"not support type {anntation}")

    def get_title(self, model: type[BaseModel]) -> str:
        if "title" in model.model_config and model.model_config["title"]:
            return model.model_config["title"]
        else:
            return model.__name__

    def field_to_attribute(
        self,
        model: BaseModel,
        field_name: str,
        field_info: FieldInfo,
        value: Any = None,
    ):
        value = getattr(model, field_name) if value is None else value
        value_type = type(value)
        print(value_type)
        if value_type in self.dis_gen_types:
            return
        gen_method = self.get_gen_attribute_method(value_type, field_info)
        if gen_method is not None:
            return gen_method(model, field_name, value)
        else:
            return

    def get_gen_attribute_method(
        self, value_type: type, field_info: FieldInfo
    ) -> Callable[[BaseModel, str, FieldInfo], int | str | None] | None:
        for condition, gen_method in self.gen_model_attribute_method:
            if condition(value_type, field_info):
                return gen_method

    def register_gen_node_atribute_method(
        self,
        condition: Callable[[type, FieldInfo], bool],
        gen_method: Callable[[BaseModel, str, Any], int | str | None],
    ):
        self.gen_model_attribute_method.append((condition, gen_method))

    def register_base_method(self):
        def base_type_condition(value_type: type, field_info: FieldInfo) -> bool:
            if (
                value_type in [str, int, float, bool]
                or issubclass(value_type, BaseModel)
                or get_origin(value_type) is list
                or value_type is list
            ):
                return True
            return False

        def gen_model_attribute_base_type(
            model: BaseModel, field_name: str, value: Any
        ):
            field_info = model.model_fields[field_name]
            value_type = type(value)
            id = None
            if issubclass(value_type, BaseModel):
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                    id = dpg.add_button(label=self.get_title(value_type))
            if get_origin(value_type) is list or value_type is list:
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                    id = dpg.add_button(label="collose", user_data=(True, []))
                sub_ids = []
                for v in value:
                    sub_id = self.field_to_attribute(model, field_name, field_info, v)
                    if sub_id is not None:
                        sub_ids.append(sub_id)
                dpg.set_item_user_data(id, (True, sub_ids))

                def collose_sub_items(
                    sender: Any, app_data: Any, user_data: tuple[bool, list[int | str]]
                ):
                    print(sender, app_data, user_data)
                    sub_ids = user_data[1]
                    if user_data[0]:
                        for sub_id in sub_ids:
                            dpg.hide_item(sub_id)
                    else:
                        for sub_id in sub_ids:
                            dpg.show_item(sub_id)
                    dpg.set_item_user_data(sender, (not user_data[0], sub_ids))

                dpg.set_item_callback(id, collose_sub_items)
            with dpg.node_attribute(
                attribute_type=dpg.mvNode_Attr_Static, user_data=(model, field_name)
            ):
                if value_type is str:
                    title = field_info.title or field_name
                    id = dpg.add_input_text(default_value=value, label=title)
                elif value_type is int:
                    title = field_info.title or field_name
                    id = dpg.add_input_int(default_value=value, label=title)
                elif value_type is float:
                    title = field_info.title or field_name
                    id = dpg.add_input_float(default_value=value, label=title)
                elif value_type is bool:
                    title = field_info.title or field_name
                    id = dpg.add_checkbox(default_value=value, label=title)
            return id

        self.register_gen_node_atribute_method(
            base_type_condition, gen_model_attribute_base_type
        )

    def model_to_node(self, model: BaseModel, offset: tuple[int, int]):
        node_title = self.get_title(model.__class__)

        with self.node_editor.node(
            label=node_title,
            user_data=model,
            pos=offset,
        ):
            with self.node_editor.node_attribute(attribute_type=dpg.mvNode_Attr_Output):
                node_attribute_title = self.get_title(model.__class__)
                dpg.add_text(node_attribute_title)

            for field_name, field_info in model.model_fields.items():
                if _value := getattr(model, field_name):
                    self.field_to_attribute(model, field_name, field_info)
