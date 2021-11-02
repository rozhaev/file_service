from typing import Dict

from pydantic import BaseModel


class ExceptionModel(BaseModel):
    message: str
    params: Dict[str, str]
