from typing import Generic, TypeVar, Optional, List, Any
from pydantic import BaseModel

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    status: str = "success"
    message: Optional[str] = None
    data: Optional[T] = None

class PaginatedResponse(BaseModel, Generic[T]):
    status: str = "success"
    message: Optional[str] = None
    data: List[T]
    total: int
    page: int
    size: int
