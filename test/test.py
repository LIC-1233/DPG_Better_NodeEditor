import sys
from pathlib import Path
from typing import Any

from dearpygui import dearpygui as dpg
from pydantic import BaseModel

project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))
from NodeAtrManager import NodeAtributeManager


class test_node_attribute1(BaseModel):
    model_config = {"frozen": True}
    test1: str = "test1"
    test2: int = 0
    test3: int = 1
    test4: int = 2


class test_node_data1(BaseModel):
    model_config = {"frozen": True}
    test_attribute1: test_node_attribute1 = test_node_attribute1()
    test1: str = "test1"


def node_attribute_int():
    dpg.add_input_int()


test_attribute1 = test_node_attribute1()


def callback(sender: int | str, app_data: Any, user_data: Any):
    print(sender, app_data, user_data)
    setattr(user_data[0], user_data[1], app_data)


def link_callback(sender: int | str, app_data: tuple[int | str, int | str]):
    # app_data -> (link_id1, link_id2)
    dpg.add_node_link(app_data[0], app_data[1], parent=sender)


def delink_callback(sender: int | str, app_data: int | str):
    # app_data -> link_id
    dpg.delete_item(app_data)


node_atribute_manager = NodeAtributeManager()


def run():
    dpg.create_context()
    dpg.create_viewport(title=" ", width=800, height=600)
    with dpg.window(label=" ", width=800, height=600, tag="main_window"):
        dpg.set_primary_window("main_window", True)
        with dpg.node_editor(
            minimap=True, callback=link_callback, delink_callback=delink_callback
        ):
            with dpg.node(pos=(200, 100), user_data=test_attribute1):
                for field, value in test_attribute1.model_dump().items():
                    if type(value) is int:
                        with dpg.node_attribute(
                            attribute_type=dpg.mvNode_Attr_Output,
                            user_data=field,
                        ):
                            node_atr_1 = dpg.add_input_int(
                                width=100,
                                label=field,
                                user_data=(test_attribute1, field),
                                default_value=value,
                            )
                        node_atribute_manager.register_node_atribute(
                            test_attribute1, field, node_atr_1
                        )
                    print(field)
            with dpg.node(pos=(200, 200)):
                for field, value in test_attribute1.model_dump().items():
                    if type(value) is int:
                        with dpg.node_attribute(
                            attribute_type=dpg.mvNode_Attr_Input,
                            user_data=field,
                        ):
                            node_atr_2 = dpg.add_input_int(
                                width=100,
                                label=field,
                                user_data=(test_attribute1, field),
                                default_value=value,
                                callback=callback,
                            )
                        node_atribute_manager.register_node_atribute(
                            test_attribute1, field, node_atr_2
                        )
                    print(field)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


run()
# print(test_attribute1)
# print(test_attribute1)
# print(test_node_attribute1.model_fields)
