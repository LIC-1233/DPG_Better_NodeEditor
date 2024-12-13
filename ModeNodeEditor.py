from typing import Any, Callable

from dd_game_type.base import BaseModel
from NodeEditor import NodeEditor
from utils.BiDirectionalDict import BiDirectionalDict


class ModelNodeEditor(NodeEditor):
    def __init__(
        self,
        node_editor_popup: Callable[[dict[int | str, list[int | str]]], None],
        node_popup: Callable[[dict[int | str, list[int | str]], int | str], None],
        node_attribute_popup: Callable[
            [dict[int | str, list[int | str]], int | str], None
        ],
        check_link: Callable[[int | str, int | str], bool] | None = None,
        delink_callback: Callable[[int | str, int | str], None] | None = None,
    ):
        super().__init__(
            node_editor_popup,
            node_popup,
            node_attribute_popup,
            check_link,
            delink_callback,
        )

        self.model_data_manager: BiDirectionalDict[int | str, tuple[BaseModel, str]] = (
            BiDirectionalDict()
        )


    def set_value(self, attr_id: int | str, value: Any):
        