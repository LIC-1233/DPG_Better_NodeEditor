from dearpygui import dearpygui as dpg


class DDlinkhandler:
    def __init__(self):
        pass

    def check_link(self, input_id: int | str, output_id: int | str):
        input_attr = dpg.get_item_user_data(input_id)
        output_attr = dpg.get_item_user_data(output_id)

        if not (input_attr and output_attr):
            print("input_attr or output_attr is None")
            return False

        return True
