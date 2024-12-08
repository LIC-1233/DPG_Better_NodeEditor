from typing import Optional

from pydantic import Field

from dd_game_type.base import BaseModel
from dd_game_type.hero.info import (
    activity_modifier as activity_modifier_type,
)
from dd_game_type.hero.info import (
    armour as armour_type,
)
from dd_game_type.hero.info import (
    combat_skill as combat_skill_type,
)
from dd_game_type.hero.info import (
    controlled as controlled_type,
)
from dd_game_type.hero.info import (
    crit as crit_type,
)
from dd_game_type.hero.info import (
    death_reaction as death_reaction_type,
)
from dd_game_type.hero.info import (
    deaths_door as deaths_door_type,
)
from dd_game_type.hero.info import (
    extra_battle_loot as extra_battle_loot_type,
)
from dd_game_type.hero.info import (
    extra_curio_loot as extra_curio_loot_type,
)
from dd_game_type.hero.info import (
    generation as generation_type,
)
from dd_game_type.hero.info import (
    hp_reaction as hp_reaction_type,
)
from dd_game_type.hero.info import (
    id_index as id_index_type,
)
from dd_game_type.hero.info import (
    incompatible_party_member as incompatible_party_member_type,
)
from dd_game_type.hero.info import (
    mode as mode_type,
)
from dd_game_type.hero.info import (
    overstressed_modifier as overstressed_modifier_type,
)
from dd_game_type.hero.info import (
    quirk_modifier as quirk_modifier_type,
)
from dd_game_type.hero.info import (
    Resistances as resistances_type,
)
from dd_game_type.hero.info import (
    skill_selection as skill_selection_type,
)
from dd_game_type.hero.info import (
    tag as tag_type,
)
from dd_game_type.hero.info import (
    weapon as weapon_type,
)


class heroes_info(BaseModel):
    resistances: Optional[list[resistances_type]] = Field(
        default=None,
        title="抗性",
        description="抗性",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: Optional[list[crit_type]] = Field(
        default=None,
        title="暴击效果",
        description="暴击效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    weapon: Optional[list[weapon_type]] = Field(
        default=None,
        title="武器",
        description="武器",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    armour: Optional[list[armour_type]] = Field(
        default=None,
        title="护甲",
        description="护甲",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_skill: Optional[list[combat_skill_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_skill: Optional[list[combat_skill_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_move_skill: Optional[list[combat_skill_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag: Optional[list[tag_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    mode: Optional[list[mode_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    overstressed_modifier: Optional[list[overstressed_modifier_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    quirk_modifier: Optional[list[quirk_modifier_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    activity_modifier: Optional[list[activity_modifier_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    incompatible_party_member: Optional[list[incompatible_party_member_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    deaths_door: Optional[list[deaths_door_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_reaction: Optional[list[hp_reaction_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    death_reaction: Optional[list[death_reaction_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    controlled: Optional[list[controlled_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    id_index: Optional[list[id_index_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_battle_loot: Optional[list[extra_battle_loot_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_curio_loot: Optional[list[extra_curio_loot_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    skill_selection: Optional[list[skill_selection_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    generation: Optional[list[generation_type]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
