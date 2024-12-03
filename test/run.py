import sys
from pathlib import Path

from dearpygui import dearpygui as dpg

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


dpg.create_context()
register_font()
dpg.create_viewport(title=" ", width=800, height=600)
create_window()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
