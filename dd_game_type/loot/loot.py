from typing import Any, Literal, Optional

from pydantic import Field

from dd_game_type.base import BaseModel


class loot_tables_data_type(BaseModel):
    table: Optional["loot | str"] = Field(
        default=None,
        title="战利品表",
        description="战利品表",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    type: Optional[str] = Field(
        default=None,
        title="类型",
        description="类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    amount: Optional[int] = Field(
        default=None,
        title="数量",
        description="数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    specific_page_index: Optional[int] = Field(
        default=None,
        title="特定页面索引",
        description="特定页面索引",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    max_page_index: Optional[int] = Field(
        default=None,
        title="最大页面索引",
        description="最大页面索引",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    min_page_index: Optional[int] = Field(
        default=None,
        title="最小页面索引",
        description="最小页面索引",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rarity: Optional[str] = Field(
        default=None,
        title="稀有度",
        description="稀有度",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_auto_open: Optional[bool] = Field(
        default=None,
        title="是否自动打开",
        description="是否自动打开",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    read_outside_of_dungeon: Optional[bool] = Field(
        default=None,
        title="是否在副本外读取",
        description="是否在副本外读取",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )

    def model_dump(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        d = super().model_dump(*args, **kwargs)
        if d["table"]:
            d["table"] = d["table"].id
        return super().model_dump(*args, **kwargs)


class entry(BaseModel):
    type: Optional[Literal["nothing", "item", "table", "trinket", "journal_page"]] = (
        Field(
            default=None,
            title="类型",
            description="类型",
            json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
        )
    )
    chances: Optional[float] = (
        Field(  # TODO 是int还是float 原版只有int，mod明日方舟饰品有float
            default=None,
            title="几率",
            description="几率",
            json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
        )
    )
    data: Optional[loot_tables_data_type] = Field(
        default=None,
        title="数据",
        description="数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class loot(BaseModel):
    id: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    difficulty: Optional[int] = Field(
        default=None,
        title="难度",
        description="难度",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dungeon: Optional[str] = Field(
        default=None,
        title="副本",
        description="副本",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    entries: Optional[list[entry]] = Field(
        default=None,
        title="战利品",
        description="战利品",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    infestation_sequence_element: Optional[str] = Field(
        default=None,
        title="猩红序列元素",
        description="猩红序列元素",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class darkness_bonuses_data_type(BaseModel):
    darkness: Optional[int] = Field(
        default=None,
        title="暗黑",
        description="暗黑",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    chance: Optional[float] = Field(
        default=None,
        title="几率",
        description="几率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    codes: Optional[list[str]] = Field(
        default=None,
        title="战利品表",
        description="战利品表",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class darkness_bonuses(BaseModel):
    key: Optional[str] = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    data: Optional[list[darkness_bonuses_data_type]] = Field(
        default=None,
        title="数据",
        description="数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
