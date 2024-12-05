import sys
from pathlib import Path
from typing import Any

from dearpygui import dearpygui as dpg

project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from NodeAtrManager import NodeAtributeManager
from utils.Base import BaseModel
from NodeEditor import NodeEditor


class test_node_attribute1(BaseModel):
    test1: str = "test1"
    test2: int = 0
    test3: int = 1
    test4: int = 2


class test_node_data1(BaseModel):
    test_attribute1: test_node_attribute1 = test_node_attribute1()
    test1: str = "test1"


def node_attribute_int():
    dpg.add_input_int()


test_attribute1 = test_node_attribute1()
test_attribute2 = test_node_attribute1()


def callback(sender: int | str, app_data: Any, user_data: Any):
    print(sender, app_data, user_data)
    setattr(user_data[0], user_data[1], app_data)


node_atribute_manager = NodeAtributeManager()
node_editor = NodeEditor()


def run():
    dpg.create_context()
    dpg.create_viewport(title=" ", width=800, height=600)
    with dpg.window(label=" ", width=800, height=600, tag="main_window"):
        dpg.set_primary_window("main_window", True)
        with node_editor.node_editor(minimap=True):
            with node_editor.node(pos=(200, 100), user_data=test_attribute1):
                dpg.draw_circle((100, 100), 25, color=(255, 255, 255, 255))
                for field, value in test_attribute1.model_dump().items():
                    print(value, type(value))
                    if type(value) is int:
                        with node_editor.node_attribute(
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
                    if type(value) is str:
                        with node_editor.node_attribute(
                            attribute_type=dpg.mvNode_Attr_Output,
                            user_data=field,
                        ):
                            node_atr_1 = dpg.add_input_text(
                                width=100,
                                label=field,
                                user_data=(test_attribute1, field),
                                default_value=value,
                            )
                        node_atribute_manager.register_node_atribute(
                            test_attribute1, field, node_atr_1
                        )
            with node_editor.node(pos=(200, 200)):
                for field, value in test_attribute2.model_dump().items():
                    if type(value) is int:
                        with node_editor.node_attribute(
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
                    if type(value) is str:
                        with node_editor.node_attribute(
                            attribute_type=dpg.mvNode_Attr_Output,
                            user_data=field,
                        ):
                            node_atr_1 = dpg.add_input_text(
                                width=100,
                                label=field,
                                user_data=(test_attribute1, field),
                                default_value=value,
                            )
                        node_atribute_manager.register_node_atribute(
                            test_attribute1, field, node_atr_1
                        )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


run()
# print(test_attribute1)
# print(test_attribute1.model_dump())
# print(test_attribute2)
# print(test_node_attribute1.model_fields)
