from pydantic import Field

from dd_game_type.base import BaseModel
from dd_game_type.loot.loot import (
    darkness_bonuses as darkness_bonuses_type,
)
from dd_game_type.loot.loot import loot


class loot_file(BaseModel):
    loot_tables: list[loot] = Field(
        default=None,
        title="战利品表",
        description="战利品表",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    darkness_bonuses: list[darkness_bonuses_type] = Field(
        default=None,
        title="暗黑增益",
        description="暗黑增益",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
