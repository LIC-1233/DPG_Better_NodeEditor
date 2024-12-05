from collections import defaultdict
from typing import Any

from dearpygui import dearpygui as dpg
from pydantic import BaseModel


class NodeAtributeManager:
    def __init__(self):
        self._node_atr_map: dict[tuple[BaseModel, str], list[int | str]] = defaultdict(
            list
        )
        self.callback = {}

    def register_node_atribute(
        self, model: BaseModel, feild: str, node_atribute: int | str
    ):
        self._node_atr_map[(model, feild)].append(node_atribute)
        self.callback[node_atribute] = dpg.get_item_callback(node_atribute)
        dpg.set_item_callback(node_atribute, self._callback)

    def _callback(
        self, sender: int | str, app_data: Any, user_data: tuple[BaseModel, str]
    ):
        print(sender, app_data, user_data)

        # 原始callback
        if sender in self.callback and self.callback[sender] is not None:
            self.callback[sender](sender, app_data, user_data)

        # 同步模型和使用模型的项目
        model, feild = user_data
        setattr(model, feild, app_data)
        for node_atribute in self._node_atr_map[(model, feild)]:
            dpg.set_value(node_atribute, app_data)