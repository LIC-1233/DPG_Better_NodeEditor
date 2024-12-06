from collections import defaultdict
from contextlib import contextmanager
from typing import Any, Callable

from dearpygui import dearpygui as dpg


class NodeEditor:
    def __init__(
        self,
        node_editor_popup: Callable[[dict[int | str, list[int | str]]], None],
        node_popup: Callable[[dict[int | str, list[int | str]]], None],
        node_attribute_popup: Callable[[dict[int | str, list[int | str]]], None],
    ):
        """
        这里是函数的简短描述。

        :param node_editor_popup: 节点编辑器右键弹出窗口,参数是节点编辑器的所有节点->节点属性字典
        :param node_popup: 节点右键弹出窗口,参数是节点编辑器的所有节点->节点属性字典
        :param node_attribute_popup: 节点属性右键弹出窗口,参数是节点编辑器的所有节点->节点属性字典
        :return: 函数不返回任何值。
        """
        self.node_editor_popup = node_editor_popup
        self.node_popup = node_popup
        self.node_attribute_popup = node_attribute_popup

        self.node_editor_instance: int
        self.node_list = []
        self.node_atr_list = []
        self.node_atr_map: dict[int | str, list[int | str]] = defaultdict(list)
        self.link_list = []

    def _on_click_global(self):

        # 节点属性右键菜单
        for node_attribute in self.node_atr_list:
            for node_attribute_item in dpg.get_item_children(node_attribute, slot=1):  # type: ignore
                if dpg.get_item_state(node_attribute_item).get("hovered"):
                    self.node_attribute_popup(self.node_atr_map)
                    return

        # 节点右键菜单
        for node in self.node_list:
            if dpg.get_item_state(node).get("hovered"):
                self.node_popup(self.node_atr_map)
                return

        # 节点链接右键
        for link in self.link_list:
            if dpg.get_item_state(link).get("hovered"):
                self.delink_callback(0, link)
                return

        # 节点编辑器菜单
        self.node_editor_popup(self.node_atr_map)

    def _register_global_handler(self, node_editor: int | str):
        with dpg.handler_registry() as _handlers:
            dpg.add_mouse_click_handler(
                button=dpg.mvMouseButton_Right, callback=self._on_click_global
            )

    def _register_node(self, node: int | str):
        self.node_list.append(node)

    def _register_node_attribute(self, node_attribute: int | str):
        p = dpg.get_item_parent(node_attribute)
        if p and dpg.get_item_type(p) == "mvAppItemType::mvNode":
            self.node_atr_map[p].append(node_attribute)
        self.node_atr_list.append(node_attribute)

    def node_collaps(
        self, sender: int | str, app_data: int | str, user_data: tuple[int | str, bool]
    ):
        node, collaps = user_data
        for node_attr in self.node_atr_map[node]:
            if collaps:
                dpg.show_item(node_attr)
            else:
                dpg.hide_item(node_attr)
        dpg.set_item_user_data(sender, (node, not collaps))

    # 链接节点
    def link_callback(self, sender: int | str, app_data: tuple[int | str, int | str]):
        # app_data -> (link_id1, link_id2)

        # 链接双方的部件是否一样检查
        def check_link(input_id: int | str, output_id: int | str):
            input_attr = dpg.get_item_user_data(input_id)
            output_attr = dpg.get_item_user_data(output_id)

            if not (input_attr and output_attr):
                print("input_attr or output_attr is None")
                return False
            input_childs = dpg.get_item_children(input_id, slot=1)
            output_childs = dpg.get_item_children(output_id, slot=1)

            if not (input_childs and output_childs) and not (
                isinstance(input_childs, list) and isinstance(output_childs, list)
            ):
                print("input_childs or output_childs is None")
                return False
            if not (isinstance(input_childs, list) and isinstance(output_childs, list)):
                print("input_childs or output_childs is not list")
                return False
            if len(input_childs) != len(output_childs):
                print("input_childs or output_childs is not equal")
                return False

            for input_child, output_child in zip(
                input_childs, output_childs, strict=False
            ):
                if dpg.get_item_type(input_child) != dpg.get_item_type(output_child):
                    print("input_child or output_child is not equal")
                    return False
            print(
                [dpg.get_item_info(i) for i in input_childs],
                [dpg.get_item_info(i) for i in output_childs],
            )
            return True

        # 移除输入端的已存在的链接
        # TODO 未来优化方向 = 建立[输出端_id:link_id]的index
        def remove_exist_link(sender: int | str, app_data: tuple[int | str, int | str]):
            for link in self.link_list:
                if app_data[1] == dpg.get_item_user_data(link)[1]:  # type: ignore
                    self.delink_callback(sender, link)

        if not check_link(app_data[0], app_data[1]):
            return
        remove_exist_link(sender, app_data)

        link_id = dpg.add_node_link(
            app_data[0], app_data[1], user_data=app_data, parent=sender
        )
        self.link_list.append(link_id)

    # 删除链接
    def delink_callback(self, sender: int | str, app_data: int | str):
        # app_data -> link_id
        dpg.delete_item(app_data)
        self.link_list.remove(app_data)

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
        with dpg.node_editor(
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
            callback=self.link_callback,
            delink_callback=self.delink_callback,
        ) as node_editor:
            self._register_global_handler(node_editor)
            self.node_editor_instance = node_editor
            yield node_editor  # type: ignore

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
        with dpg.node(
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
            self._register_node(node)
            if cllose_button:
                with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
                    anchor = dpg.add_spacer(width=min_width)
                    button = dpg.add_button(
                        arrow=True,
                        direction=dpg.mvDir_Right,
                        width=20,
                        user_data=(node, False),
                        callback=self.node_collaps,
                    )

                    def adjust_position(
                        sender: int | str, app_data: Any, user_data: Any
                    ):
                        max_width = 0
                        for na in dpg.get_item_children(node, slot=1):  # type: ignore
                            for item in dpg.get_item_children(na, slot=1):  # type: ignore
                                try:
                                    item_width = dpg.get_item_rect_size(item)[0]
                                    max_width = max(max_width, item_width)
                                except Exception:
                                    pass
                        x, y = dpg.get_item_pos(anchor)
                        dpg.set_item_pos(button, [x + max_width, y - 30])

                    with dpg.item_handler_registry() as move_handler:
                        dpg.add_item_visible_handler(callback=adjust_position)
                    dpg.bind_item_handler_registry(node, move_handler)

            yield node

    @contextmanager  # type: ignore
    def node_attribute(  # type: ignore
        self,
        *,
        label: str | None = None,
        user_data: Any = None,
        use_internal_label: bool = True,
        tag: int | str = 0,
        indent: int = -1,
        parent: int | str = 0,
        before: int | str = 0,
        show: bool = True,
        filter_key: str = "",
        tracked: bool = False,
        track_offset: float = 0.5,
        attribute_type: int = 0,
        shape: int = 1,
        category: str = "general",
        **kwargs: Any,
    ):
        with dpg.node_attribute(
            label=label,  # type: ignore
            user_data=user_data,
            use_internal_label=use_internal_label,
            tag=tag,
            indent=indent,
            parent=parent,
            before=before,
            show=show,
            filter_key=filter_key,
            tracked=tracked,
            track_offset=track_offset,
            attribute_type=attribute_type,
            shape=shape,
            category=category,
            **kwargs,
        ) as node_attribute:
            self._register_node_attribute(node_attribute)
            yield node_attribute

    def delete_item(
        self,
        item: int | str,
        *,
        children_only: bool = False,
        slot: int = -1,
        **kwargs: Any,
    ):
        try:
            self.node_list.remove(item)
            self.node_atr_list.remove(item)
        except ValueError:
            pass
        dpg.delete_item(item, children_only=children_only, slot=slot, **kwargs)
