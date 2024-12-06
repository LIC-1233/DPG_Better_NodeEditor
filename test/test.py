from typing import Any, Callable

import dearpygui.dearpygui as dpg

dpg.create_context()


class Button:
    def __init__(self, label: str):
        with dpg.stage() as self._staging_container_id:
            self._id = dpg.add_button(label=label)

    def set_callback(self, callback: Callable[..., Any]):
        dpg.set_item_callback(self._id, callback)

    def get_label(self):
        return dpg.get_item_label(self._id)

    def submit(self, parent: int | str):
        dpg.push_container_stack(parent)
        dpg.unstage(self._staging_container_id)
        dpg.pop_container_stack()


my_button = Button("Press me")
my_button.set_callback(lambda: print("I've been pressed!"))

print(my_button.get_label())

with dpg.window(label="Tutorial", tag="main_win"):
    dpg.add_text("hello world")

my_button.submit("main_win")

dpg.create_viewport(title="Custom Title", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
