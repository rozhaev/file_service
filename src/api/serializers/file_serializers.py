from pydantic.main import BaseModel
from datetime import date


class FileSerializer(BaseModel):
    file_id: str


class FileInfoSerializer(BaseModel):
    user_id: str
    date: date
    file_id: str
