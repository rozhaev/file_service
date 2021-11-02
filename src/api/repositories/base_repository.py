from abc import ABC
from typing import Optional, AsyncGenerator

from bson import ObjectId

from api.connection_managers.mongo_connection_manager import MongoConnectionManager
from api.settings import Settings


class BaseRepository(ABC):

    def __init__(self, mongodb_connection_manager: MongoConnectionManager, settings: Settings) -> None:
        self.mongodb_connection_manager = mongodb_connection_manager
        self.database = settings.mongo_database

    async def get_connection_async(self):
        return await self.mongodb_connection_manager.get_connection_async()

    @property
    def collection_name(self) -> str:
        raise NotImplementedError

    async def get_data(self, criteria_dict: dict) -> Optional[dict]:
        connection = await self.get_connection_async()
        collection = connection[self.database][self.collection_name]

        data = await collection.find_one(criteria_dict)
        if not data:
            return None
        return data

    async def save_data(self, document: dict) -> None:
        connection = await self.get_connection_async()
        await connection[self.database][self.collection_name].insert_one(document)

    async def update_data(self, criteria_dict: dict, data: dict) -> None:
        connection = await self.get_connection_async()
        await connection[self.database][self.collection_name].update_one(criteria_dict, {'$set': data})

    async def upload_file(self, filename: str, source: bytes) -> str:
        connection = await self.get_connection_async()
        file_id = await connection[self.database][self.collection_name].upload_from_stream(filename, source)
        return file_id

    async def download_file(self, file_id: str) -> AsyncGenerator:
        connection = await self.get_connection_async()
        out = await connection[self.database][self.collection_name].open_download_stream(ObjectId(file_id))
        contents = await out.read()
        yield contents
