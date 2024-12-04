import sys
from pathlib import Path

from dearpygui import dearpygui as dpg
from pydantic import BaseModel

project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))

from main import NodeEditor  # noqa: E402


def register_font():
    with dpg.font_registry():
        with dpg.font(
            str(Path(".").absolute() / "test" / "assets" / "fonts" / "hyrgs.ttf"),
            13,
        ) as default_font:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x300, 0x400)
            dpg.bind_font(default_font)


def create_window():
    with dpg.window(label=" ", width=800, height=600, tag="main_window"):
        dpg.set_primary_window("main_window", True)
        NodeEditor()

class test_node_attribute1(BaseModel):
    test1: str = "test1"
    test2: int = 0


class test_node_data1(BaseModel):
    test_attribute1: test_node_attribute1 = test_node_attribute1()


def add_node(node_data: BaseModel):
    print("123123123")
    print(node_data.model_json_schema())


def create_NE_window():
    with dpg.window(label=" ", width=800, height=600, tag="main_window"):
        dpg.set_primary_window("main_window", True)
        with dpg.node_editor():
            # add_node(test_node_data1())
            pass


add_node(test_node_data1())

# dpg.create_context()
# register_font()
# dpg.create_viewport(title=" ", width=800, height=600)
# create_NE_window()
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()
