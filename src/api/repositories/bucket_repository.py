from typing import AsyncGenerator
from uuid import uuid4

from api.repositories.base_repository import BaseRepository


class BucketRepository(BaseRepository):

    @property
    def collection_name(self) -> str:
        return 'bucket'

    async def upload_async(self, file: bytes) -> str:
        user_id = str(uuid4())
        return await self.upload_file(user_id, file)

    async def download_async(self, file_id: str) -> AsyncGenerator:
        return self.download_file(file_id)
