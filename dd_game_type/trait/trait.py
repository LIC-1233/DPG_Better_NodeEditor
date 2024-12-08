from typing import Optional

from pydantic import Field

from dd_game_type.base import BaseModel
from dd_game_type.buff.buff import buff
from dd_game_type.effect.effect import Effect as effect_type


class combat_start_turn_act_outs_data_type(BaseModel):
    number_value: Optional[float] = Field(
        default=None,
        title="数值",
        description="数值",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    string_value: Optional[str] = Field(
        default=None,
        title="字符串",
        description="字符串",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    effect: Optional[str | effect_type] = (
        Field(  # TODO 可能是非法 原版没有这个，mod幻术师有这个
            default=None,
            title="效果",
            description="效果",
            json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
        )
    )


class combat_start_turn_act_outs_type(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    data: Optional[combat_start_turn_act_outs_data_type] = Field(
        default=None,
        title="数据",
        description="数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    chance: Optional[float | int] = (
        Field(  # 他妈的傻逼阿比盖尔作者，写了一个无法被float转换的int值
            default=None,
            title="几率",
            description="几率",
            json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
        )
    )
    raid_limit: Optional[int] = Field(
        default=None,
        title="每场战斗限制",
        description="每场战斗限制",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    valid_hero_class_ids: Optional[list[str]] = Field(
        default=None,
        title="有效英雄职业",
        description="有效英雄职业",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class reaction_act_outs_data_type(BaseModel):
    effect: Optional[str | effect_type] = Field(
        default=None,
        title="效果",
        description="效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class reaction_act_outs_type(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    data: Optional[reaction_act_outs_data_type] = Field(
        default=None,
        title="数据",
        description="数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    chance: Optional[float | int] = (
        Field(  # 他妈的傻逼阿比盖尔作者，写了一个无法被float转换的int值
            default=None,
            title="几率",
            description="几率",
            json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
        )
    )


class trait(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_generated: Optional[bool] = Field(
        default=None,
        title="是否生成",
        description="是否生成",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    overstress_type: Optional[str] = Field(  # TODO 可能是[美德,折磨]枚举
        default=None,
        title="爆压类型",
        description="爆压类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    curio_tag: Optional[str] = Field(
        default=None,
        title="爆压子类型",
        description="爆压子类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    curio_tag_chance: Optional[float] = Field(
        default=None,
        title="爆压子类型概率",
        description="爆压子类型概率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    keep_loot: Optional[bool] = Field(
        default=None,
        title="是否保留战利品",
        description="是否保留战利品",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    required_dungeon_history: Optional[list[str]] = Field(
        default=None,
        title="需要的副本历史",
        description="需要的副本历史",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    generate_chance_modifier: Optional[float] = Field(
        default=None,
        title="生成几率修正",
        description="生成几率修正",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_ids: Optional[list[str | buff]] = Field(
        default=None,
        title="增益ID",
        description="增益ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_start_turn_act_outs: Optional[list[combat_start_turn_act_outs_type]] = Field(
        default=None,
        title="战斗开始时动作",
        description="战斗开始时动作",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    reaction_act_outs: Optional[list[reaction_act_outs_type]] = Field(
        default=None,
        title="?",
        description="?",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tags: Optional[list[str]] = Field(  # TODO 可能是非法 原版没有这个，mod季灾有这个
        default=None,
        title="标签",
        description="标签",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    validate_act_out_barks: Optional[bool] = (
        Field(  # TODO 可能是非法 原版没有这个，mod魔像有这个
            default=None,
            title="是否校验号叫动作",
            description="是否校验号叫动作",
            json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
        )
    )
