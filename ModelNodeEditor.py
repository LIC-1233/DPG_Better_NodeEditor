import contextvars
from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any, Callable

from dearpygui import dearpygui as dpg

from dd_game_type.base import BaseModel
from NodeEditor import NodeEditor
from utils.BiDirectionalDict import BiDirectionalDict as BDict

node_editor_context = contextvars.ContextVar("node_editor_context")
node_context = contextvars.ContextVar("node_context")


def get_title(model: type[BaseModel]) -> str:
    if "title" in model.model_config and model.model_config["title"]:
        return model.model_config["title"]
    else:
        return model.__name__


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

        self.node_model: BDict[int | str, BaseModel] = BDict()
        self.attr_modelField: BDict[int | str, tuple[BaseModel, str]] = BDict()

    def set_value_callback(self, attr_id: int | str, value: Any):
        pass

    @contextmanager  # type: ignore
    def node_editor(
        self,
        *,
        label: str | None = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        tag: int | str = 0,
        width: int = 0,
        height: int = 0,
        parent: int | str = 0,
        before: int | str = 0,
        show: bool = True,
        filter_key: str = "",
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        menubar: bool = False,
        minimap: bool = False,
        minimap_location: int = 2,
        **kwargs: Any,
    ) -> int | str:  # type: ignore
        with super().node_editor(
            label=label,  # type: ignore
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            width=width,
            height=height,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            menubar=menubar,
            minimap=minimap,
            minimap_location=minimap_location,
            **kwargs,
            callback=self.link_attr,
            delink_callback=self.delink
            if self.delink_callback is None
            else self.delink_callback,
        ) as node_editor:
            self.token = node_editor_context.set(self)
            self._register_global_handler(node_editor)
            self.node_editor_instance = node_editor
            yield node_editor  # type: ignore

        node_editor_context.reset(self.token)

    @contextmanager  # type: ignore
    def node(  # type: ignore
        self,
        *,
        label: str | None = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        tag: int | str = 0,
        parent: int | str = 0,
        before: int | str = 0,
        payload_type: str = "$$DPG_PAYLOAD",
        drag_callback: Callable = None,  # type: ignore
        drop_callback: Callable = None,  # type: ignore
        show: bool = True,
        pos: list[int] | tuple[int, ...] = (),
        filter_key: str = "",
        delay_search: bool = False,
        tracked: bool = False,
        track_offset: float = 0.5,
        draggable: bool = True,
        min_width: int = 100,
        cllose_button: bool = True,
        **kwargs: Any,
    ):
        with super().node(
            label=label,  # type: ignore
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            parent=parent,
            before=before,
            payload_type=payload_type,
            drag_callback=drag_callback,
            drop_callback=drop_callback,
            show=show,
            pos=pos,
            filter_key=filter_key,
            delay_search=delay_search,
            tracked=tracked,
            track_offset=track_offset,
            draggable=draggable,
            **kwargs,
        ) as node:
            yield node


class ModelNode:
    def __init__(self, model: BaseModel):
        node_editor = node_editor_context.get(None)
        if node_editor is None:
            raise ValueError("No active Node context found.")
        self.node_editor: ModelNodeEditor = node_editor
        self.model = model
        self.model_fields = self.model.model_fields

    def __enter__(self):  # type: ignore
        self.token = node_context.set(self)
        node_title = get_title(self.model.__class__)
        with self.node_editor.node(
            label=node_title,
            user_data=self.model,
        ) as node:
            self.node = node

        return node

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any):
        node_context.reset(self.token)


class NodeSection(ABC):
    def __init__(
        self,
        field_name: str,
        value: Any,
        callback: Callable[[int | str, Any], None] | None = None,
    ):
        node = node_context.get(None)
        if node is None:
            raise ValueError("No active Node context found.")
        self.node: ModelNode = node
        self.init(field_name, value)
        self.draw(field_name, value)

    @staticmethod
    @abstractmethod
    def condition(field_name: str, value: Any) -> bool: ...
    @abstractmethod
    def init(self, field_name: str, value: Any): ...
    def callback(self, attr_id: int | str, value: Any):
        self.node.node_editor.set_value_callback(attr_id, value)

    @abstractmethod
    def set_items_values(self, value: Any): ...
    @abstractmethod
    def draw(self, field_name: str, value: Any): ...


class BaseNodeSection(NodeSection):
    def init(self, field_name: str, value: Any):
        pass

    @staticmethod
    def condition(field_name: str, value: Any):
        if type(value) in [str, int, float, bool]:
            return True
        return False

    def item_callback(self, sender: int | str, appdata: Any, userdata: Any):
        return self.callback(self.attr_id, appdata)

    def set_items_values(self, value: Any):
        dpg.set_value(self.item_id, value)

    def draw(self, field_name: str, value: str | int | float | bool):
        field_info = self.node.model.model_fields[field_name]
        with self.node.node_editor.node_attribute(
            attribute_type=dpg.mvNode_Attr_Static,
            user_data=(self.node.model, field_name),
        ) as id:
            self.attr_id = id
            if isinstance(value, str):
                title = field_info.title or field_name
                self.item_id = dpg.add_input_text(
                    default_value=value,
                    label=title,
                    width=100,
                    callback=self.item_callback,
                )
            elif isinstance(value, bool):
                title = field_info.title or field_name
                self.item_id = dpg.add_checkbox(
                    default_value=value,
                    label=title,
                    width=100,
                    callback=self.item_callback,
                )
            elif isinstance(value, int):
                title = field_info.title or field_name
                self.item_id = dpg.add_input_int(
                    default_value=value,
                    label=title,
                    width=100,
                    callback=self.item_callback,
                )
            else:
                title = field_info.title or field_name
                self.item_id = dpg.add_input_float(
                    default_value=value,
                    label=title,
                    width=100,
                    callback=self.item_callback,
                )
