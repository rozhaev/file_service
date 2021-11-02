from typing import Iterator

from injector import Module, singleton, provider, Injector
from starlette.requests import Request

from api.connection_managers.mongo_connection_manager import MongoConnectionManager
from api.repositories.bucket_repository import BucketRepository
from api.repositories.file_repository import FileRepository
from api.services.file_service import FileService
from api.settings import Settings


class ApplicationContainer(Module):

    @singleton
    @provider
    def provide_settings(self) -> Settings:
        return Settings()

    @singleton
    @provider
    def provide_mongo_connection_manager(self, settings: Settings) -> MongoConnectionManager:
        return MongoConnectionManager(settings)

    @singleton
    @provider
    def provide_bucket_repository(
            self,
            mongo_connection_manager: MongoConnectionManager,
            settings: Settings
    ) -> BucketRepository:
        return BucketRepository(mongo_connection_manager, settings)

    @singleton
    @provider
    def provide_file_repository(
            self,
            mongo_connection_manager: MongoConnectionManager,
            settings: Settings
    ) -> FileRepository:
        return FileRepository(mongo_connection_manager, settings)

    @singleton
    @provider
    def provide_file_service(
            self,
            bucket_repository: BucketRepository,
            file_repository: FileRepository
    ) -> FileService:
        return FileService(bucket_repository, file_repository)


async def get_container_injector(request: Request) -> Iterator[Injector]:
    container = Injector(request.app.container_clazz())
    try:
        yield container
    finally:
        del container
