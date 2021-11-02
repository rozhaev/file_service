from typing import AsyncGenerator
from uuid import uuid4
from datetime import date

from api.models.file_model import FileModel
from api.repositories.bucket_repository import BucketRepository
from api.repositories.file_repository import FileRepository
from api.serializers.file_serializers import FileSerializer, FileInfoSerializer


class FileService:

    def __init__(
            self,
            bucket_repository: BucketRepository,
            file_repository: FileRepository
    ) -> None:
        self.bucket_repository = bucket_repository
        self.file_repository = file_repository

    async def save_file(self, file: bytes) -> str:
        user_id = str(uuid4())
        file_id = await self.bucket_repository.upload_async(file)
        await self.file_repository.save_async(FileModel(user_id=user_id, date=date.today(), file_id=file_id))
        return file_id

    async def download_file(self, file_serializer: FileSerializer) -> AsyncGenerator[bytes, None]:
        return await self.bucket_repository.download_async(file_serializer.file_id)

    async def get_file_information(self, file_serializer: FileSerializer) -> FileInfoSerializer:
        file_model = await self.file_repository.get_file_information_by_file_id(file_serializer.file_id)
        return FileInfoSerializer(**file_model.dict())
