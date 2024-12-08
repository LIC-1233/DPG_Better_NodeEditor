import sys
from pathlib import Path

from dearpygui import dearpygui as dpg

project_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(project_dir))


from dd_game_type.hero import info
from DDNodeEditorPopup import NodeEditorPopup
from i18 import _
from ModelGen import ModelNodeGenerator
from NodeEditor import NodeEditor

hero_info = info.HeroesInfo(
    resistances=info.Resistances(
        stun=0.2,
        poison=0.3,
        bleed=0.4,
        disease=0.5,
        move=0.6,
        debuff=0.7,
        death_blow=0.8,
        trap=0.9,
    ),
    weapon=[
        info.Weapon(
            name="test",
            atk=0.1,
            dmg=(1, 2),
            crit=0.1,
            spd=1,
        )
    ],
)
hero_info = info.HeroesInfo.model_validate_json(
    open("test/阿比盖尔_heroinfo.json").read()
)


def register_font():
    with dpg.font_registry():
        with dpg.font(
            str(Path(".").absolute() / "test" / "assets" / "fonts" / "hyrgs.ttf"),
            13,
        ) as font2:
            dpg.add_font_range_hint(dpg.mvFontRangeHint_Chinese_Full)
            dpg.add_font_range(0x300, 0x400)
            dpg.bind_font(font2)
        pass


def check_link(a: int, b: int):
    print(a, b)
    return True


def run():
    dpg.create_context()

    register_font()
    editor_id = dpg.generate_uuid()
    node_editor_popup = NodeEditorPopup()
    node_editor = NodeEditor(
        node_editor_popup=node_editor_popup.node_editor_pop_wnd,
        node_popup=node_editor_popup.node_pop_wnd,
        node_attribute_popup=node_editor_popup.node_attribute_pop_wnd,
        check_link=check_link,  # type: ignore
    )
    node_editor_popup.set_node_editor(node_editor)

    dpg.create_viewport(title=" ", width=1400, height=1040)
    with dpg.window(label=" ", width=1400, height=1040, tag="main_window"):
        dpg.set_primary_window("main_window", True)
        with node_editor.node_editor(tag=editor_id, minimap=True):
            model_node_generator = ModelNodeGenerator(node_editor)
            model_node_generator.auto_gen_model_node(hero_info, (100, 100))
            with node_editor.node(label="阿比盖尔", pos=(400, 400)) as node:  # type: ignore
                with node_editor.node_attribute() as node_attribute:
                    dpg.add_button(
                        label="test",
                        callback=lambda: print(node_editor.get_link_id(node_attribute)),
                    )

            with node_editor.node(label="阿比盖尔", pos=(400, 400)) as node:  # type: ignore
                with node_editor.node_attribute(
                    attribute_type=dpg.mvNode_Attr_Output
                ) as node_attribute:
                    dpg.add_button(
                        label="test",
                        callback=lambda: print(node_editor.get_link_id(node_attribute)),
                    )

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvNodeAttribute):
            dpg.add_theme_color(
                dpg.mvNodeCol_NodeOutline, (255, 0, 255), category=dpg.mvThemeCat_Nodes
            )
            # dpg.add_theme_style(dpg.mvStyleVar_, 5, category=dpg.mvThemeCat_Core)
    dpg.bind_theme(global_theme)
    # dpg.show_style_editor()
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def test():
    for k, v in hero_info.model_fields.items():
        print(k, v.annotation)
    for k, v in hero_info.model_dump().items():
        print(k, v)


run()
# test()

# print(test_attribute1)
# print(test_attribute1.model_dump())
# print(test_attribute2)
# print(test_node_attribute1.model_fields)
