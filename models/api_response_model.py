from typing import Optional

from pydantic import BaseModel


class ApiResponseModel(BaseModel):
    code: Optional[int] = None
    type: Optional[str] = None
    message: Optional[str] = None
