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
        self.theme_normal = dpg.add_theme()
        with dpg.theme() as theme_node_attr_no_spacing:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 4, 0)
        self.theme_node_attr_no_spacing = theme_node_attr_no_spacing
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

    def get_primary_key(self, model: BaseModel) -> str:
        if "primary_key" in model.model_config and model.model_config["primary_key"]:
            try:
                return getattr(model, model.model_config["primary_key"])
            except Exception:
                pass
        return self.get_title(type(model))

    def field_to_attribute(
        self,
        model: BaseModel,
        field_name: str,
        field_info: FieldInfo,
        value: Any = None,
    ):
        value = getattr(model, field_name) if value is None else value
        value_type = type(value)
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
        for condition, gen_method in self.gen_model_attribute_method[::-1]:
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

            # BaseModel
            if issubclass(value_type, BaseModel):
                with self.node_editor.node_attribute(
                    attribute_type=dpg.mvNode_Attr_Static, user_data=(model, field_name)
                ) as id:
                    dpg.add_button(
                        label=self.get_primary_key(value),
                        callback=lambda: dpg.configure_item(
                            id, attribute_type=dpg.mvNode_Attr_Input
                        ),
                    )

            # list
            elif get_origin(value_type) is list or value_type is list:
                with self.node_editor.node_attribute(
                    attribute_type=dpg.mvNode_Attr_Static
                ):
                    with dpg.group(horizontal=True):
                        button_id = dpg.add_button(
                            arrow=True, direction=dpg.mvDir_Down, user_data=(True, [])
                        )
                        dpg.add_text(field_info.title or field_name)
                sub_ids = []
                for v in value:
                    sub_id = self.field_to_attribute(model, field_name, field_info, v)
                    if sub_id is not None:
                        sub_ids.append(sub_id)
                dpg.set_item_user_data(button_id, (True, sub_ids))

                def collose_sub_items(
                    sender: Any, app_data: Any, user_data: tuple[bool, list[int | str]]
                ):
                    sub_node_attr_ids = user_data[1]
                    if user_data[0]:
                        for sub_node_attr_id in sub_node_attr_ids:
                            sub_items = dpg.get_item_children(sub_node_attr_id, slot=1)
                            if sub_items:
                                for sub_item in sub_items:
                                    dpg.hide_item(sub_item)
                            dpg.configure_item(sender, direction=dpg.mvDir_Right)
                            dpg.bind_item_theme(
                                sub_node_attr_id, self.theme_node_attr_no_spacing
                            )
                    else:
                        for sub_node_attr_id in sub_node_attr_ids:
                            sub_items = dpg.get_item_children(sub_node_attr_id, slot=1)
                            if sub_items:
                                for sub_item in sub_items:
                                    dpg.show_item(sub_item)
                            dpg.configure_item(sender, direction=dpg.mvDir_Down)
                            dpg.bind_item_theme(sub_node_attr_id, self.theme_normal)
                    dpg.set_item_user_data(
                        sender, (not user_data[0], sub_node_attr_ids)
                    )

                dpg.set_item_callback(button_id, collose_sub_items)
                collose_sub_items(button_id, None, (True, sub_ids))

            # base type
            else:
                with self.node_editor.node_attribute(
                    attribute_type=dpg.mvNode_Attr_Static, user_data=(model, field_name)
                ) as id:
                    if value_type is str:
                        title = field_info.title or field_name
                        dpg.add_input_text(
                            default_value=value,
                            label=title,
                            user_data=id,
                            callback=lambda: base_type_callback,
                        )
                    elif value_type is int:
                        title = field_info.title or field_name
                        dpg.add_input_int(
                            default_value=value,
                            label=title,
                            user_data=id,
                            callback=lambda: base_type_callback,
                        )
                    elif value_type is float:
                        title = field_info.title or field_name
                        dpg.add_input_float(
                            default_value=value,
                            label=title,
                            user_data=id,
                            callback=lambda: base_type_callback,
                        )
                    elif value_type is bool:
                        title = field_info.title or field_name
                        dpg.add_checkbox(
                            default_value=value,
                            label=title,
                            user_data=id,
                            callback=lambda: base_type_callback,
                        )

            def base_type_callback(
                sender: int | str, app_data: int | str, user_data: int | str
            ):
                parent_id = user_data
                model, field_name = dpg.get_item_user_data(parent_id)  # type: ignore
                setattr(model, field_name, app_data)

            if isinstance(id, str) or isinstance(id, int) or isinstance(id, NoneType):
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
