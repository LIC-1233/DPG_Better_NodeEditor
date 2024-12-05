import threading
from typing import Any, ClassVar

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    _id_counter: ClassVar[int] = 0  # 类变量用于计数
    _lock: ClassVar[threading.Lock] = threading.Lock()  # 线程锁

    @classmethod
    def _generate_base_unique_id(cls) -> int:
        with cls._lock:  # 正确：使用线程锁作为上下文管理器
            cls._id_counter += 1
            return cls._id_counter

    def __hash__(self):
        return self._base_unique_id

    def __init__(self, **data: Any):
        super().__init__(**data)
        self._base_unique_id = self._generate_base_unique_id()
