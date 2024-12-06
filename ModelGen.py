from dearpygui import dearpygui as dpg

from NodeEditor import NodeEditor
from utils.Base import BaseModel


def auto_gen_model_node(
    node_editor: NodeEditor, model: BaseModel, offset: tuple[int | float, int | float]
):
    print(model.model_fields)
    models = [model]
    while models:
        model = models.pop()
        with node_editor.node(pos=offset, user_data=model):  # type: ignore
            with node_editor.node_attribute(
                attribute_type=dpg.mvNode_Attr_Output,
            ):
                dpg.add_text(model.__class__.__name__)
            for field_name, field_info in model.model_fields.items():
                print(field_name, field_info)
                if value := getattr(model, field_name):
                    if field_info.annotation is str:
                        with node_editor.node_attribute(
                            user_data=(model, field_name),
                            attribute_type=dpg.mvNode_Attr_Static,
                        ):
                            dpg.add_input_text(
                                default_value=value,
                                width=100,
                                label=field_name + "111111",
                            )
                    if field_info.annotation is int:
                        with node_editor.node_attribute(
                            user_data=(model, field_name),
                            attribute_type=dpg.mvNode_Attr_Static,
                        ):
                            dpg.add_input_int(
                                default_value=value,
                                width=100,
                                label=field_name + "111111",
                            )
                    if field_info.annotation is float:
                        with node_editor.node_attribute(
                            user_data=(model, field_name),
                            attribute_type=dpg.mvNode_Attr_Static,
                        ):
                            dpg.add_input_float(
                                default_value=value,
                                width=100,
                                label=field_name + "111111",
                            )
                    if field_info.annotation is bool:
                        with node_editor.node_attribute(
                            user_data=(model, field_name),
                            attribute_type=dpg.mvNode_Attr_Static,
                        ):
                            dpg.add_checkbox(
                                default_value=value,
                                width=100,
                                label=field_name + "111111",
                            )
                    if issubclass(field_info.annotation, BaseModel):  # type: ignore
                        with node_editor.node_attribute(
                            user_data=(model, field_name),
                            attribute_type=dpg.mvNode_Attr_Input,
                        ):
                            dpg.add_text(field_name)
                        models.append(value)
