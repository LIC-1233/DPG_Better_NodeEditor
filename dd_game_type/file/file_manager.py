from pydantic import BaseModel

from dd_game_type.buff.buff import buff
from dd_game_type.file.effect import effect_file
from dd_game_type.file.hero_info import heroes_info_file
from dd_game_type.loot.loot import loot
from dd_game_type.trait.trait import trait


class file_manager:
    def __init__(self):
        self.dataModel_regexFile: dict[type[BaseModel], list[str]] = {}

    def init(self):
        self.dataModel_regexFile = {
            buff: [
                "shared/buffs/*.json",
                "dlc/*/shared/buffs/*.json",
                "dlc/*/features/*/shared/buffs/*.json",
            ],
            loot: [
                "loot/*.json",
                "dlc/*/loot/*.json",
                "dlc/*/features/*/loot/*.json",
            ],
            trait: [
                "shared/trait/*.json",
                "dlc/*/shared/trait/*.json",
                "dlc/*/features/*/shared/trait/*.json",
            ],
            effect_file: [
                "effects/*.darkest",
                "modes/*/effects/*.darkest",
                "dlc/*/effects/*.darkest",
                "dlc/*/modes/*/effects/*.darkest",
                "dlc/*/features/*/effects/*.darkest",
                "dlc/*/features/*/modes/*/effects/*.darkest",
            ],
            heroes_info_file: [
                "heroes/*/*info.darkest",
                "heroes/*/*override.darkest",
                "dlc/*/heroes/*/*info.darkest",
                "dlc/*/heroes/*/*override.darkest",
                "dlc/*/features/*/heroes/*/*info.darkest",
                "dlc/*/features/*/heroes/*/*override.darkest",
            ],
        }
