from abc import ABC, abstractmethod
from typing import Any

from pydantic import BaseModel, field_validator


class NodeAttributePrototype(ABC):
    name: str = "node_attribute_default_name"

    def __init__(self):
        NodeAttributePrototypeManager.register_node_attribute_prototype(self)

    # 检查是否已经注册
    def check_name(self, name: str):
        if not isinstance(name, str):  # type: ignore
            raise TypeError("name must be a string")
        if NodeAttributePrototypeManager.get_node_attribute_prototype(name):
            raise ValueError(f"NodeAttributePrototype {name} already exists")
        return name

    @abstractmethod
    def draw_attribute(self): ...


class NodeAttributePrototypeManager:
    _instance = None  # 用于存储唯一实例的私有类变量
    _node_attribute_prototypes: dict[str, NodeAttributePrototype] = {}

    def __new__(cls, *args: Any, **kwargs: Any):
        if not cls._instance:
            cls._instance = super(NodeAttributePrototypeManager, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance

    @staticmethod
    def register_node_attribute_prototype(node_attribute: NodeAttributePrototype):
        if (
            node_attribute.name
            in NodeAttributePrototypeManager._node_attribute_prototypes
        ):
            raise ValueError(
                f"NodeAttributePrototype {node_attribute.name} already exists"
            )
        NodeAttributePrototypeManager._node_attribute_prototypes[
            node_attribute.name
        ] = node_attribute

    @staticmethod
    def get_node_attribute_prototype(name: str) -> NodeAttributePrototype | None:
        return NodeAttributePrototypeManager._node_attribute_prototypes.get(name, None)

    @staticmethod
    def get_all_node_attribute_prototypes() -> dict[str, NodeAttributePrototype]:
        return NodeAttributePrototypeManager._node_attribute_prototypes

    @staticmethod
    def remove_node_attribute_prototype(name: str) -> None:
        if name not in NodeAttributePrototypeManager._node_attribute_prototypes:
            raise ValueError(f"NodeAttributePrototype {name} not found")
        NodeAttributePrototypeManager._node_attribute_prototypes.pop(name)


class NodePrototype(BaseModel):
    name: str
    attribute_name_list: list[str]

    @field_validator("name", mode="before")
    def check_name(cls, name: str):
        if not isinstance(name, str):  # type: ignore
            raise ValueError("name must be a str")
        if NodePrototypeManager.get_node_prototype(name):
            raise ValueError(f"NodePrototype {name} already exists")
        return name

    @field_validator("attribute_name_list", mode="before")
    def check_attribute_name_list(cls, attribute_name_list: list[str]):
        if not (
            isinstance(attribute_name_list, list)  # type: ignore
            and all(isinstance(item, str) for item in attribute_name_list)  # type: ignore
        ):
            raise ValueError("attribute_name_list must be a list of str")
        for attribute_name in attribute_name_list:
            if not NodeAttributePrototypeManager.get_node_attribute_prototype(
                attribute_name
            ):
                raise ValueError(f"NodeAttributePrototype {attribute_name} not found")
        return attribute_name_list


class NodePrototypeManager:
    _instance = None  # 用于存储唯一实例的私有类变量
    _node_prototypes: dict[str, NodePrototype] = {}

    def __new__(cls, *args: Any, **kwargs: Any):
        if not cls._instance:
            cls._instance = super(NodePrototypeManager, cls).__new__(
                cls, *args, **kwargs
            )
        return cls._instance

    @staticmethod
    def register_node_prototype(node_prototype: NodePrototype):
        NodePrototypeManager._node_prototypes[node_prototype.name] = node_prototype

    @staticmethod
    def get_node_prototype(name: str):
        return NodePrototypeManager._node_prototypes.get(name, None)

    @staticmethod
    def get_all_node_prototypes():
        return NodePrototypeManager._node_prototypes

    @staticmethod
    def remove_node_prototype(name: str):
        NodePrototypeManager._node_prototypes.pop(name)
