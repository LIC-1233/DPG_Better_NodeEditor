from pydantic import Field

from dd_game_type.base import BaseModel
from dd_game_type.buff.buff import buff


class buff_file(BaseModel):
    buffs: list[buff] = Field(
        default=None,
    )
