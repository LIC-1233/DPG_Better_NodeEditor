from collections import defaultdict
from typing import Any

from dearpygui import dearpygui as dpg
from pydantic import BaseModel


class NodeAtributeManager:
    def __init__(self):
        self._value_atr_map: dict[tuple[BaseModel, str], list[int | str]] = defaultdict(
            list
        )

    def register_node_atribute(
        self, model: BaseModel, feild: str, node_atribute: int | str
    ):
        self._value_atr_map[(model, feild)].append(node_atribute)
        dpg.set_item_callback(node_atribute, self.callback)

    def callback(
        self, sender: int | str, app_data: Any, user_data: tuple[BaseModel, str]
    ):
        print(sender, app_data, user_data)
        model, feild = user_data
        setattr(model, feild, app_data)
        for node_atribute in self._value_atr_map[(model, feild)]:
            dpg.set_value(node_atribute, app_data)
