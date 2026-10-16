from typing import Optional

from pydantic import BaseModel


class CategoryModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
