from types import NoneType
from typing import Any, Literal, Optional, Union, get_args, get_origin

from dearpygui import dearpygui as dpg
from pydantic.fields import FieldInfo

from dd_game_type.base import BaseModel
from NodeEditor import NodeEditor


class ModelNodeGenerator:
    def __init__(self, node_editor: NodeEditor) -> None:
        self.node_editor = node_editor

    def create_widget(
        self,
        field_name: str,
        model: BaseModel,
        field_info: FieldInfo,
        value: Any,
        models: list[tuple[int, BaseModel]],
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
            ) as parent_attr_id:
                widget = dpg.add_text(title)
                with dpg.tooltip(widget):
                    dpg.add_text(description)
            if is_list:
                for i in value:
                    models.append((parent_attr_id, i))
            else:
                models.append((parent_attr_id, value))
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

    def auto_gen_model_node(
        self, model: BaseModel, offset: tuple[int | float, int | float]
    ):
        root_node = None
        models: list[tuple[int, BaseModel]] = [(0, model)]
        while models:
            parentID_model = models.pop()
            parent_attr_id, model = parentID_model
            node_title = ""
            if (
                "title" in model.__class__.model_config
                and model.__class__.model_config["title"]
            ):
                node_title = model.__class__.model_config["title"]
            else:
                node_title = model.__class__.__name__

            with self.node_editor.node(
                label=node_title,
                user_data=model,
            ) as node:
                if not root_node:
                    root_node = node
                with self.node_editor.node_attribute(
                    attribute_type=dpg.mvNode_Attr_Output
                ) as self_id:
                    if (
                        "title" in model.__class__.model_config
                        and model.__class__.model_config["title"]
                    ):
                        title = model.__class__.model_config["title"]
                    else:
                        title = model.__class__.__name__
                    dpg.add_text(title)
                if parent_attr_id != 0:
                    self.node_editor.link_attr(0, (parent_attr_id, self_id))

                for field_name, field_info in model.model_fields.items():
                    if value := getattr(model, field_name):
                        anntation = field_info.annotation
                        if get_origin(anntation) is Union:
                            anntation = [
                                i for i in get_args(anntation) if i not in [NoneType]
                            ]
                            if len(anntation) == 1:
                                anntation = anntation[0]
                            else:
                                print(anntation)
                        if get_origin(anntation) is list:
                            anntation = get_args(anntation)[0]

                        # print(anntation)

                        self.create_widget(field_name, model, field_info, value, models)

        # self.node_editor.auto_layout(root_node)
