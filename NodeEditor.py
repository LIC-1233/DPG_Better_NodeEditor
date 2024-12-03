from dearpygui import dearpygui as dpg

from NodeEditorPopup import NodeEditorPopup


class NodeEditor:
    def register_global_handler(self, node_editor: int | str):
        nodeditor_popup_wnd = NodeEditorPopup.node_editor_pop_wnd()
        node_popup_wnd = NodeEditorPopup.node_pop_wnd()
        node_attribute_popup_wnd = NodeEditorPopup.node_attribute_pop_wnd()

        def on_click_global():
            if dpg.get_item_state(node_editor).get("hovered"):
                for node in dpg.get_item_children(node_editor, slot=1):  # type: ignore
                    if dpg.get_item_state(node).get("hovered"):
                        for node_attribute in dpg.get_item_children(node, slot=1):  # type: ignore
                            for node_item in dpg.get_item_children(
                                node_attribute, slot=1
                            ):  # type: ignore
                                if dpg.get_item_state(node_item).get("hovered"):
                                    # 节点属性右键
                                    # selected_node_attribute = node_attribute
                                    # selected_node_item = node_item
                                    dpg.show_item(node_attribute_popup_wnd)
                                    return
                        # 节点右键
                        # selected_node = node
                        dpg.show_item(node_popup_wnd)
                        return
                # 节点编辑器右键
                dpg.show_item(nodeditor_popup_wnd)

        with dpg.handler_registry() as _handlers:
            dpg.add_mouse_click_handler(
                button=dpg.mvMouseButton_Right, callback=on_click_global
            )

    def link_callback(self, sender: int | str, app_data: tuple[int | str, int | str]):
        # app_data -> (link_id1, link_id2)
        dpg.add_node_link(app_data[0], app_data[1], parent=sender)

    def delink_callback(self, sender: int | str, app_data: int | str):
        # app_data -> link_id
        dpg.delete_item(app_data)

    def __init__(self):
        with dpg.node_editor(
            callback=self.link_callback, delink_callback=self.delink_callback
        ) as node_editor:
            self.register_global_handler(node_editor)
