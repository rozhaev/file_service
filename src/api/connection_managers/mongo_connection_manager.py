from motor.motor_asyncio import AsyncIOMotorClient
from api.settings import Settings


class MongoConnectionManager:

    def __init__(self, settings: Settings) -> None:
        self.mongo_dsn = settings.mongo_dsn
        self._connection = None

    async def __aenter__(self):
        await self.get_connection_async()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close_connection_async()

    async def get_connection_async(self) -> AsyncIOMotorClient:
        """
        Create connection if it not exists
        :return:
        """
        if self._connection is None:
            self._connection = AsyncIOMotorClient(self.mongo_dsn)

        return self._connection

    async def close_connection_async(self):
        """
        Close all connection by async method
        :return:
        """
        self._connection.close()
        await self._connection.wait_closed()
