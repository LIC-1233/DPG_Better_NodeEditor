from dearpygui import dearpygui as dpg

from NodeType import NodeAttributePrototype, NodePrototype


class NodeAttributeInt(NodeAttributePrototype):
    name = "node_attribute_int"

    def __init__(
        self,
        label: str = "",
        max_value: int = 100,
        min_value: int = 0,
        default_value: int = 0,
    ):
        self.label = label
        self.max_value = max_value
        self.min_value = min_value
        self.default_value = default_value
        super().__init__()

    def draw_attribute(self):
        dpg.add_slider_int(
            label=self.label,
            min_value=self.min_value,
            max_value=self.max_value,
            default_value=self.default_value,
        )


class NodeInt(NodePrototype):
    name = "node_int"
    attribute_name_list = ["node_attribute_int"]

    def __init__(self):
        pass


class Node:
    def __init__(self):
        pass
