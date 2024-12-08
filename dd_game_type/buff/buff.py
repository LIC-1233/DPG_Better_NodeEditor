from typing import Optional

from pydantic import Field

from dd_game_type.base import BaseModel
from dd_game_type.enum.type_enum import buff_stat_types_enum


class buff_stat_types(BaseModel):
    hp_heal_amount: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_stat_multiply: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_stat_add: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resistance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    poison_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    bleed_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dmg_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dmg_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_heal_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_heal_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    party_surprise_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    monsters_surprise_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ambush_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    scouting_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    starving_damage_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    upgrade_discount: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    debuff_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resolve_check_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stun_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    move_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_negative_quirk_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    food_consumption_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resolve_xp_bonus_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    activity_side_effect_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    vampire_evolution_duration: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    quirk_evolution_death_immune: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    disable_combat_skill_attribute: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard_blocked: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag_blocked: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_protection: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_stealth: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit_received_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stealth: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_heal: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffle_dot: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guarded: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    status: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    vampire: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torch_increase_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torch_decrease_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torchlight_burn_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_on_miss: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_from_idle_in_town: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shard_reward_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shard_consume_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_reflect_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_duration_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_amount_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_amount_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_duration_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_amount_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_amount_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_duration_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_amount_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_amount_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_duration_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_amount_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_amount_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffle_dot_duration_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffle_dot_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard_duration_received_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_bleed_received_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_poison_received_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_bleed_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_poison_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    random_target_friendly_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    random_target_attack_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    transfer_debuff_from_attacker_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    transfer_buff_from_attacker_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    quirk_tag_evolution_duration: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    deathblow_chance: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    heartattack_stress_heal_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_guard: Optional[int] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_duration_percent: Optional[float] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_duration_percent: Optional[float] = Field(
        default=None,
    )


class rule_data_type(BaseModel):
    value: Optional[float] = Field(
        alias="float",
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    string: Optional[str] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class buff(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stat_type: Optional[buff_stat_types_enum] = Field(
        default=None,
        title="状态类型",
        description="状态类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stat_sub_type: Optional[str] = Field(
        default=None,
        title="状态子类型",
        description="状态子类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    amount: Optional[float] = Field(
        default=None,
        title="数量",
        description="数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    duration_type: Optional[str] = Field(
        default=None,
        title="持续类型",
        description="持续类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    duration: Optional[int] = Field(
        default=None,
        title="持续时间",
        description="持续时间",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_if_not_active: Optional[bool] = Field(
        default=None,
        title="不激活时删除",
        description="不激活时删除",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_on_battle_complete: Optional[bool] = Field(
        default=None,
        title="战斗结束时删除",
        description="战斗结束时删除",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rule_type: Optional[str] = Field(
        default=None,
        title="规则类型",
        description="规则类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_false_rule: Optional[bool] = Field(
        default=None,
        title="是否为反选",
        description="是否为反选",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rule_data: Optional[rule_data_type] = Field(
        default=None,
        title="规则数据",
        description="规则数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_clear_debuff_valid: Optional[bool] = Field(
        default=None,
        title="是否为清除Debuff",
        description="是否为清除Debuff",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    has_description: Optional[bool] = Field(
        default=None,
        title="是否有描述",
        description="是否有描述",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    fx: Optional[str] = Field(
        default=None,
        title="特效",
        description="特效",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class buff_table(BaseModel):
    buffs: Optional[list[buff]] = Field(
        default=None,
        title="buff列表",
        description="buff列表",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
