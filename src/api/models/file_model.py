from pydantic import BaseModel
from datetime import date


class FileModel(BaseModel):
    user_id: str
    date: date
    file_id: str
