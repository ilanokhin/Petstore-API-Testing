from typing import Optional

from pydantic import BaseModel


class TagModel(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
