import sys
from pathlib import Path

from dearpygui import dearpygui as dpg

project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from ModelGen import auto_gen_model_node
from NodeAtrManager import NodeAtributeManager
from NodeEditor import NodeEditor
from NodeEditorPopup import NodeEditorPopup
from utils.Base import BaseModel


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
test_node1 = test_node_data1()


node_atribute_manager = NodeAtributeManager()
node_editor = NodeEditor(
    node_editor_popup=NodeEditorPopup.node_editor_pop_wnd,
    node_popup=NodeEditorPopup.node_pop_wnd,
    node_attribute_popup=NodeEditorPopup.node_attribute_pop_wnd,
)


def run():
    dpg.create_context()
    dpg.create_viewport(title=" ", width=800, height=600)
    with dpg.window(label=" ", width=800, height=600, tag="main_window"):
        dpg.set_primary_window("main_window", True)
        with node_editor.node_editor(minimap=True):
            auto_gen_model_node(node_editor, test_node1, (400, 400))
            with node_editor.node(
                pos=(200, 100), user_data=test_attribute1, min_width=200
            ):
                for field, value in test_attribute1.model_dump().items():
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
            with node_editor.node(pos=(200, 250)):
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

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvNodeAttribute):
            dpg.add_theme_color(
                dpg.mvNodeCol_NodeOutline, (255, 0, 255), category=dpg.mvThemeCat_Nodes
            )
            # dpg.add_theme_style(dpg.mvStyleVar_, 5, category=dpg.mvThemeCat_Core)
    dpg.bind_theme(global_theme)
    dpg.show_style_editor()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def test():
    for k, v in test_node1.model_fields.items():
        print(k, v.annotation is BaseModel)


run()
# test()

# print(test_attribute1)
# print(test_attribute1.model_dump())
# print(test_attribute2)
# print(test_node_attribute1.model_fields)
