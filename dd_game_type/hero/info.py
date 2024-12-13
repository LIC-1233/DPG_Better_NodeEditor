from typing import Optional

from pydantic import Field, ValidationError

from dd_game_type.base import BaseModel
from dd_game_type.buff.buff import buff
from dd_game_type.effect.effect import Effect
from dd_game_type.loot.loot import loot
from dd_game_type.trait.trait import trait


class Resistances(BaseModel):
    model_config = {**BaseModel.model_config, "title": "抗性"}

    stun: Optional[float] = Field(
        default=None,
        title="眩晕抗性",
        description="眩晕抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    poison: Optional[float] = Field(
        default=None,
        title="中毒抗性",
        description="中毒抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    bleed: Optional[float] = Field(
        default=None,
        title="流血抗性",
        description="流血抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    disease: Optional[float] = Field(
        default=None,
        title="疾病抗性",
        description="疾病抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    move: Optional[float] = Field(
        default=None,
        title="移动抗性",
        description="移动抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    debuff: Optional[float] = Field(
        default=None,
        title="减益抗性",
        description="减益抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    death_blow: Optional[float] = Field(
        default=None,
        title="死亡抗性",
        description="死亡抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    trap: Optional[float] = Field(
        default=None,
        title="陷阱抗性",
        description="陷阱抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Crit(BaseModel):
    effects: Optional[list[Effect | str]] = Field(
        default=None,
        title="暴击效果",
        description="暴击效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Weapon(BaseModel):
    name: Optional[str] = Field(
        default=None,
        title="武器名",
        description="武器名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    atk: Optional[float] = Field(
        default=None,
        title="武器命中",
        description="武器命中",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dmg: Optional[tuple[int, int]] = Field(
        default=None,
        title="武器伤害",
        description="武器伤害",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: Optional[float] = Field(
        default=None,
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    spd: Optional[int] = Field(
        default=None,
        title="武器速度",
        description="武器速度",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defence: Optional[float] = Field(
        default=None,
        alias="def",
        title="闪避",
        description="闪避",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    prot: Optional[float] = Field(
        default=None,
        title="减伤",
        description="减伤",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp: Optional[int] = Field(
        default=None,
        title="生命",
        description="生命",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    upgradeRequirementCode: Optional[int] = Field(
        default=None,
        title="升级需求",
        description="升级需求",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Armour(BaseModel):
    name: Optional[str] = Field(
        default=None,
        title="武器名",
        description="武器名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    atk: Optional[float] = Field(
        default=None,
        title="武器命中",
        description="武器命中",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dmg: Optional[tuple[int, int]] = Field(
        default=None,
        title="武器伤害",
        description="武器伤害",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: Optional[float] = Field(
        default=None,
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    spd: Optional[int] = Field(
        default=None,
        title="武器速度",
        description="武器速度",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defence: Optional[float] = Field(
        default=None,
        alias="def",
        title="闪避",
        description="闪避",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    prot: Optional[float] = Field(
        default=None,
        title="减伤",
        description="减伤",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp: Optional[int] = Field(
        default=None,
        title="生命",
        description="生命",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    upgradeRequirementCode: Optional[int] = Field(
        default=None,
        title="升级需求",
        description="升级需求",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class CombatSkill(BaseModel):
    class Config:
        extra = "allow"  # 忽略额外字段

    def __post_init__(self):
        # 获取模型中定义的字段名

        if self.__pydantic_extra__:
            defined_fields = set(self.model_fields.keys())

            # 提取特定名称的额外字段
            allowed_extra_fields = {
                k for k in self.__pydantic_extra__.keys() if k.endswith("_effects")
            }  # 这里定义允许的额外字段

            # 如果有不允许的额外字段，抛出 ValidationError
            disallowed_extra = {
                k
                for k in self.__pydantic_extra__.keys()
                if k not in allowed_extra_fields | defined_fields
            }
            if disallowed_extra:
                raise ValidationError(f"Disallowed extra fields: {disallowed_extra}")

    id: Optional[str] = Field(
        default=None,
        title="技能id",
        description="技能id",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    level: Optional[int] = Field(
        default=None,
        title="技能等级",
        description="技能等级",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    type: Optional[str] = Field(
        default=None,
        title="技能类型",
        description="技能类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    atk: Optional[float] = Field(
        default=None,
        title="武器命中",
        description="武器命中",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dmg: Optional[float] = Field(
        default=None,
        title="武器伤害增加",
        description="武器伤害增加",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: Optional[float] = Field(
        default=None,
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defence: Optional[float] = Field(
        default=None,
        alias="def",
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    move: Optional[tuple[int, int]] = Field(
        default=None,
        title="可移动距离[前,后]",
        description="可移动距离[前,后]",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    starting_cooldown: Optional[int] = Field(
        default=None,
        title="初始冷却时间",
        description="初始冷却时间",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    per_battle_limit: Optional[int] = Field(
        default=None,
        title="每场战斗限制",
        description="每场战斗限制",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    per_turn_limit: Optional[int] = Field(
        default=None,
        title="每回合限制",
        description="每回合限制",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_continue_turn: Optional[bool] = Field(
        default=None,
        title="是否连续回合",
        description="是否连续回合",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    launch: Optional[str] = Field(
        default=None,
        title="技能释放位置",
        description="技能释放位置",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    target: Optional[str] = Field(
        default=None,
        title="技能目标位置",
        description="技能目标位置",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    self_target_valid: Optional[bool] = Field(
        default=None,
        title="是否自身目标",
        description="是否自身目标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_targets_chance: Optional[float] = Field(
        default=None,
        title="额外目标概率",
        description="额外目标概率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_targets_count: Optional[int] = Field(
        default=None,
        title="额外目标数量",
        description="额外目标数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_crit_valid: Optional[bool] = Field(
        default=None,
        title="是否暴击",
        description="是否暴击",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    effect: Optional[list[Effect | str]] = Field(
        default=None,
        title="技能效果",
        description="技能效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    valid_modes: Optional[list[str]] = Field(
        default=None,
        title="有效模式",
        description="有效模式",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_stealth: Optional[bool] = Field(
        default=None,
        title="是否无视隐身",
        description="是否无视隐身",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_guard: Optional[bool] = Field(
        default=None,
        title="是否无视防御",
        description="是否无视防御",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_miss: Optional[bool] = Field(
        default=None,
        title="是否允许闪避",
        description="是否允许闪避",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_be_riposted: Optional[bool] = Field(
        default=None,
        title="是否允许反击",
        description="是否允许反击",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_protection: Optional[bool] = Field(
        default=None,
        title="是否无视防御",
        description="是否无视防御",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    required_performer_hp_range: Optional[tuple[int, int]] = Field(
        default=None,
        title="执行者生命值范围",
        description="执行者生命值范围",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rank_damage_modifiers: Optional[float] = Field(
        default=None,
        title="等级伤害修正",
        description="等级伤害修正",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    heal: Optional[bool] = Field(
        default=None,
        title="是否治疗",
        description="是否治疗",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_crit_heal: Optional[bool] = Field(
        default=None,
        title="是否允许暴击治疗",
        description="是否允许暴击治疗",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    generation_guaranteed: Optional[bool] = Field(
        default=None,
        title="是否强制生成",
        description="是否强制生成",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_user_selected_targets: Optional[bool] = Field(
        default=None,
        title="是否用户选择目标",
        description="是否用户选择目标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_knowledgeable: Optional[bool] = Field(
        default=None,
        title="是否擅长",
        description="是否擅长",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_monster_rerank_valid_on_attack: Optional[bool] = Field(
        default=None,
        title="是否攻击时重排怪物",
        description="是否攻击时重排怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_monster_rerank_valid_on_friendly_presentation_end: Optional[bool] = Field(
        default=None,
        title="是否友方回合结束时重排怪物",
        description="是否友方回合结束时重排怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_monster_rerank_valid_on_friendly_post_result: Optional[bool] = Field(
        default=None,
        title="是否友方回合结束后重排怪物",
        description="是否友方回合结束后重排怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_stall_invalidating: Optional[bool] = Field(
        default=None,
        title="是否无效",
        description="是否无效",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    refresh_after_each_wave: Optional[bool] = Field(
        default=None,
        title="是否刷新每波",
        description="是否刷新每波",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_heal_base_class_ids: Optional[list[str]] = Field(
        default=None,
        title="伤害治疗基类ID",
        description="伤害治疗基类ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_deathsdoor: Optional[bool] = Field(
        default=None,
        title="是否忽略死亡门",
        description="是否忽略死亡门",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Tag(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="标签ID",
        description="标签ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Mode(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="模式ID",
        description="模式ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_raid_default: Optional[bool] = Field(
        default=None,
        title="是否默认",
        description="是否默认",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    battle_complete_combat_skill_id: Optional[CombatSkill | str] = Field(
        default=None,
        title="战斗完成时战斗技能ID",
        description="战斗完成时战斗技能ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_targetable: Optional[bool] = Field(
        default=None,
        title="是否可选目标",
        description="是否可选目标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class OverstressedModifier(BaseModel):
    override_trait_type_ids: Optional[list[trait | str]] = Field(
        default=None,
        title="爆压traitID",
        description="爆压traitID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    override_trait_type_chances: Optional[list[float]] = Field(
        default=None,
        title="爆压trait几率",
        description="爆压trait几率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class QuirkModifier(BaseModel):
    incompatible_class_ids: Optional[list[str]] = Field(
        default=None,
        title="不兼容ClassID",
        description="不兼容ClassID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class ActivityModifier(BaseModel):
    override_valid_activity_ids: Optional[list[str]] = Field(
        default=None,
        title="有效活动ID",
        description="有效活动ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class IncompatiblePartyMember(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hero_tag: Optional[str] = Field(
        default=None,
        title="英雄ID",
        description="英雄ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class DeathsDoor(BaseModel):
    enter_effects: Optional[list[Effect | str]] = Field(
        default=None,
        title="死门入effectID",
        description="死门入effectID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buffs: Optional[list[buff | str]] = Field(
        default=None,
        title="死门buffID",
        description="死门buffID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    recovery_buffs: Optional[list[buff | str]] = Field(
        default=None,
        title="死门恢复buffID",
        description="死门恢复buffID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    recovery_heart_attack_buffs: Optional[list[buff | str]] = Field(
        default=None,
        title="死门死buff亡ID",
        description="死门死亡buffID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class HpReaction(BaseModel):
    hp_ratio: Optional[float] = Field(
        default=None,
        title="血量比例",
        description="血量比例",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_under: Optional[bool] = Field(
        default=None,
        title="是否低于时生效",
        description="是否低于时生效",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    effects: Optional[list[Effect | str]] = Field(
        default=None,
        title="effectID",
        description="effectID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class DeathReaction(BaseModel):
    target_allies: Optional[bool] = Field(
        default=None,
        title="是否目标盟友",
        description="是否目标盟友",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    target_enemies: Optional[bool] = Field(
        default=None,
        title="是否目标敌人",
        description="是否目标敌人",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    effects: Optional[list[Effect | str]] = Field(
        default=None,
        title="effectID",
        description="effectID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Controlled(BaseModel):
    target_rank: Optional[int] = Field(
        default=None,
        title="目标优先级",
        description="目标优先级",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class IdIndex(BaseModel):
    index: Optional[int] = Field(
        default=None,
        title="索引",
        description="索引",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class ExtraBattleLoot(BaseModel):
    code: Optional[loot | str] = Field(
        default=None,
        title="Code",
        description="Code",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    count: Optional[int] = Field(
        default=None,
        title="数量",
        description="数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class ExtraCurioLoot(BaseModel):
    code: Optional[loot | str] = Field(
        default=None,
        title="Code",
        description="Code",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    count: Optional[int] = Field(
        default=None,
        title="数量",
        description="数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class SkillSelection(BaseModel):
    can_select_combat_skills: Optional[bool] = Field(
        default=None,
        title="是否可选战斗技能",
        description="是否可选战斗技能",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_selected_combat_skills_max: Optional[int] = Field(
        default=None,
        title="最大可选战斗技能数量",
        description="最大可选战斗技能数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class Generation(BaseModel):
    is_generation_enabled: Optional[bool] = Field(
        default=None,
        title="是否生效",
        description="是否生效",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_positive_quirks_min: Optional[int] = Field(
        default=None,
        title="最小正面quirk数量",
        description="最小正面quirk数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_positive_quirks_max: Optional[int] = Field(
        default=None,
        title="最大正面quirk数量",
        description="最大正面quirk数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_negative_quirks_min: Optional[int] = Field(
        default=None,
        title="最小负面quirk数量",
        description="最小负面quirk数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_negative_quirks_max: Optional[int] = Field(
        default=None,
        title="最大负面quirk数量",
        description="最大负面quirk数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_class_specific_camping_skills: Optional[int] = Field(
        default=None,
        title="最小类特定camping技能数量",
        description="最小类特定camping技能数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_shared_camping_skills: Optional[int] = Field(
        default=None,
        title="共享camping技能数量",
        description="共享camping技能数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_random_combat_skills: Optional[int] = Field(
        default=None,
        title="随机战斗技能数量",
        description="随机战斗技能数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    number_of_cards_in_deck: Optional[int] = Field(
        default=None,
        title="卡牌数量",
        description="卡牌数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    card_chance: Optional[float] = Field(
        default=None,
        title="卡牌概率",
        description="卡牌概率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class HeroesInfo(BaseModel):
    model_config = {**BaseModel.model_config, "title": "英雄信息"}

    resistances: Optional[Resistances] = Field(
        default=None,
        title="抗性",
        description="抗性",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: Optional[Crit] = Field(
        default=None,
        title="暴击效果",
        description="暴击效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    weapon: Optional[list[Weapon]] = Field(
        default=None,
        title="武器",
        description="武器",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    armour: Optional[list[Armour]] = Field(
        default=None,
        title="护甲",
        description="护甲",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_skill: Optional[list[CombatSkill]] = Field(
        default=None,
        title="战斗技能",
        description="战斗技能",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_skill: Optional[list[CombatSkill]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_move_skill: Optional[list[CombatSkill]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag: Optional[list[Tag]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    mode: Optional[list[Mode]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    overstressed_modifier: Optional[list[OverstressedModifier]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    quirk_modifier: Optional[list[QuirkModifier]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    activity_modifier: Optional[list[ActivityModifier]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    incompatible_party_member: Optional[list[IncompatiblePartyMember]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    deaths_door: Optional[list[DeathsDoor]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_reaction: Optional[list[HpReaction]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    death_reaction: Optional[list[DeathReaction]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    controlled: Optional[list[Controlled]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    id_index: Optional[IdIndex] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_battle_loot: Optional[list[ExtraBattleLoot]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_curio_loot: Optional[list[ExtraCurioLoot]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    skill_selection: Optional[list[SkillSelection]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    generation: Optional[list[Generation]] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
