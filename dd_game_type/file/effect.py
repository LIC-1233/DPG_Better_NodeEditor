from pydantic import Field

from dd_game_type.base import BaseModel
from dd_game_type.effect.effect import Effect as effect_type


class effect_file(BaseModel):
    effect: list[effect_type] = Field(
        default=None,
    )
