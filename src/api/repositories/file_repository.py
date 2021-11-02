from typing import Optional

from api.models.file_model import FileModel
from api.repositories.base_repository import BaseRepository


class FileRepository(BaseRepository):

    @property
    def collection_name(self) -> str:
        return 'files'

    async def save_async(self, document: FileModel) -> None:
        return await self.save_data(document.dict())

    async def update_request_count_async(self, sdk_version: str, ad_requests: int) -> None:
        data = {
            'ad_requests': ad_requests,
        }
        await self.update_data({'sdk_version': sdk_version}, data)

    async def get_file_information_by_file_id(self, file_id: str) -> Optional[FileModel]:
        criteria = {
            'file_id': file_id
        }
        document = await self.get_data(criteria)
        if not document:
            return
        return FileModel(**document)
