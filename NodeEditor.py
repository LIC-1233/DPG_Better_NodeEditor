from contextlib import contextmanager
from typing import Any, Callable

from dearpygui import dearpygui as dpg

from utils.BiDirectionalDict import BiDirectionalDict


class NodeEditor:
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
        """
        这里是函数的简短描述。

        :param node_editor_popup: 节点编辑器右键弹出窗口,参数1:节点属性id->节点属性字典
        :param node_popup: 节点右键弹出窗口,参数1:节点属性id->节点属性字典; 参数2:节点id
        :param node_attribute_popup: 节点属性右键弹出窗口,参数1:节点属性id->节点属性字典; 参数2:节点属性id
        :param link_callback: 节点链接回调函数,参数1:输入节点属性id; 参数2:输出节点属性id
        :param delink_callback: 节点链接解除回调函数,参数1:输入节点属性id; 参数2:输出节点属性id
        :return: 函数不返回任何值。
        """
        self.node_editor_popup = node_editor_popup
        self.node_popup = node_popup
        self.node_attribute_popup = node_attribute_popup

        self.check_link = check_link if check_link else self.defult_check_link
        self.delink_callback = delink_callback

        self.node_editor_instance: int
        self.node_list = []
        self.node_attr_list = []
        self.node_attr_map: BiDirectionalDict[int | str, int | str] = (
            BiDirectionalDict()
        )
        self.link_list = []
        self.link_chain: BiDirectionalDict[int | str, int | str] = BiDirectionalDict()
        self.theme_normal = dpg.add_theme()
        with dpg.theme() as theme_node_attr_no_spacing:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 4, 0)
        self.theme_node_attr_no_spacing = theme_node_attr_no_spacing

    def _on_click_global(self):
        # 节点属性右键菜单
        for node_attribute in self.node_attr_list:
            for node_attribute_item in dpg.get_item_children(node_attribute, slot=1):  # type: ignore
                if dpg.get_item_state(node_attribute_item).get("hovered"):
                    self.node_attribute_popup(
                        self.node_attr_map.forward_map, node_attribute
                    )
                    return

        # 节点右键菜单
        for node in self.node_list:
            if dpg.get_item_state(node).get("hovered"):
                self.node_popup(self.node_attr_map.forward_map, node)
                return

        # 节点链接右键
        for link in self.link_list:
            if dpg.get_item_state(link).get("hovered"):
                self.delink(0, link)
                return

        # 节点编辑器菜单
        self.node_editor_popup(self.node_attr_map.forward_map)

    def _register_global_handler(self, node_editor: int | str):
        with dpg.handler_registry() as _handlers:
            dpg.add_mouse_click_handler(
                button=dpg.mvMouseButton_Right, callback=self._on_click_global
            )

    def _register_node(self, node: int | str):
        self.node_list.append(node)

    def _register_node_attribute(self, node_attribute: int | str):
        p = dpg.get_item_parent(node_attribute)
        while p and dpg.get_item_type(p) != "mvAppItemType::mvNode":
            p = dpg.get_item_parent(p)
        if p and dpg.get_item_type(p) == "mvAppItemType::mvNode":
            self.node_attr_map.add(p, node_attribute)
        self.node_attr_list.append(node_attribute)

    def node_collaps(
        self, sender: int | str, app_data: int | str, user_data: tuple[int | str, bool]
    ):
        node, collaps = user_data
        for node_attr in self.node_attr_map[node]:
            if collaps:
                for item in dpg.get_item_children(node_attr, slot=1):  # type: ignore
                    dpg.show_item(item)
                dpg.configure_item(sender, direction=dpg.mvDir_Down)
                dpg.bind_item_theme(node_attr, self.theme_normal)
            else:
                for item in dpg.get_item_children(node_attr, slot=1):  # type: ignore
                    dpg.hide_item(item)
                dpg.configure_item(sender, direction=dpg.mvDir_Right)
                dpg.bind_item_theme(node_attr, self.theme_node_attr_no_spacing)
        dpg.set_item_user_data(sender, (node, not collaps))

    # 链接双方的部件是否一样检查
    @staticmethod
    def defult_check_link(input_id: int | str, output_id: int | str):
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

        for input_child, output_child in zip(input_childs, output_childs, strict=False):
            if dpg.get_item_type(input_child) != dpg.get_item_type(output_child):
                print("input_child or output_child is not equal")
                return False
        print(
            [dpg.get_item_info(i) for i in input_childs],
            [dpg.get_item_info(i) for i in output_childs],
        )
        return True

    # 链接节点
    def link_attr(self, sender: int | str, app_data: tuple[int | str, int | str]):
        if not self.check_link(app_data[0], app_data[1]):
            return

        link_id = dpg.add_node_link(
            app_data[0],
            app_data[1],
            user_data=app_data,
            parent=self.node_editor_instance,
        )
        self.link_list.append(link_id)
        self.link_chain.add(app_data[0], app_data[1])
        print(link_id)
        return link_id

    # 删除链接
    def delink(self, sender: int | str, app_data: int | str):
        # app_data -> link_id
        self.delete_item(app_data)
        self.link_list.remove(app_data)
        in_attr, out_attr = dpg.get_item_user_data(app_data)  # type: ignore
        self.link_chain.remove(in_attr, out_attr)

    def get_link_id(self, attr_id: int | str) -> list[int | str]:
        return [
            link
            for link in self.link_list
            if attr_id in dpg.get_item_user_data(link)[0]  # type: ignore
        ]

    def gen_node_network(self, node_id: int | str | None = None):
        in_out_node_maps: BiDirectionalDict[int | str, int | str] = BiDirectionalDict()
        for in_attr, out_attr in self.link_chain:
            for in_node in self.node_attr_map.get_keys_by_value(in_attr):
                for out_node in self.node_attr_map.get_keys_by_value(out_attr):
                    in_out_node_maps.add(in_node, out_node)

        if node_id:
            root_nodes = {node_id}
        else:
            root_nodes = set(in_out_node_maps.keys()) - set(in_out_node_maps.values())

        nodes_level: list[list[int | str]] = [list(root_nodes)]
        result: list[list[int | str]] = [list(root_nodes)]
        while nodes_level:
            nodes = nodes_level.pop(0)
            sub_nodes: set[int | str] = set()
            for root_node in nodes:
                sub_nodes |= set(in_out_node_maps.get_values_by_key(root_node))
            if sub_nodes:
                nodes_level.append(list(sub_nodes))
                result.append(list(sub_nodes))

        return result

    def auto_layout(
        self, node_id: int | str | None = None, hgap: int = 150, vgap: int = 20
    ):
        nodes_level = self.gen_node_network(node_id)
        pos: dpg.List[int] = dpg.get_item_pos(nodes_level[0][0])

        offset = 0
        while nodes_level:
            nodes = nodes_level.pop(0)
            max_width = 0
            last_item_bottom = 0
            for index, node in enumerate(nodes):
                max_width = max(max_width, dpg.get_item_rect_size(node)[0])
                dpg.set_item_pos(
                    node,
                    (
                        pos[0] - offset - dpg.get_item_rect_size(node)[0] - hgap,  # type: ignore
                        pos[1] + last_item_bottom,
                    ),
                )
                last_item_bottom += dpg.get_item_rect_size(node)[1] + vgap
                if index == 15:
                    a = list(nodes[15:])
                    nodes_level = [a] + nodes_level
                    break
            offset += max_width

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
            callback=self.link_attr,
            delink_callback=self.delink
            if self.delink_callback is None
            else self.delink_callback,
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
                    dpg.add_button(
                        arrow=True,
                        direction=dpg.mvDir_Down,
                        width=20,
                        user_data=(node, False),
                        callback=self.node_collaps,
                    )
                    # anchor = dpg.add_spacer(width=min_width)
                    # button = dpg.add_button(
                    #     arrow=True,
                    #     direction=dpg.mvDir_Down,
                    #     width=20,
                    #     user_data=(node, False),
                    #     callback=self.node_collaps,
                    # )
                    # def adjust_position(
                    #     sender: int | str, app_data: Any, user_data: Any
                    # ):
                    #     max_width = min_width
                    #     for na in dpg.get_item_children(node, slot=1):  # type: ignore
                    #         for item in dpg.get_item_children(na, slot=1):  # type: ignore
                    #             try:
                    #                 item_width = dpg.get_item_rect_size(item)[0]
                    #                 max_width: int = max(max_width, item_width)
                    #             except Exception:
                    #                 pass
                    #     x, y = dpg.get_item_pos(anchor)
                    #     dpg.set_item_pos(button, [x + max_width, y - 30])

                    # with dpg.item_handler_registry() as move_handler:
                    #     dpg.add_item_visible_handler(callback=adjust_position)
                    # dpg.bind_item_handler_registry(node, move_handler)

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
        if item in self.node_list:
            self.node_list.remove(item)
            node_attrs = self.node_attr_map[item]
            for node_attr in node_attrs:
                self.node_attr_list.remove(node_attr)
            self.node_attr_map.remove_key(item)

        if item in self.node_attr_list:
            self.node_attr_list.remove(item)
            self.node_attr_map.remove_value(item)
            if item in self.link_chain:
                self.link_chain.remove(item)
        
        if item in self.link_list:
            in_attr, out_attr = dpg.get_item_user_data(item)  # type: ignore
            self.link_chain.remove(in_attr, out_attr)
            self.link_list.remove(item)
        dpg.delete_item(item, children_only=children_only, slot=slot, **kwargs)
