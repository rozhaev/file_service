import http
from typing import Type

from fastapi import FastAPI
from injector import Injector
from starlette.middleware.cors import CORSMiddleware

from api.connection_managers.mongo_connection_manager import MongoConnectionManager
from api.core.container import ApplicationContainer
from api.core.exception import ExceptionModel
from api.settings import Settings

from src.api.controllers.file_controller import router as file_routing


class Application(FastAPI):

    def __init__(self, settings: Settings, container_clazz: Type[ApplicationContainer]) -> None:
        super().__init__(title=settings.service_name)
        self.container_clazz = container_clazz
        self.container = Injector(container_clazz())
        self.connection_manager = self.container.get(MongoConnectionManager)
        self.__init_cors()
        self.__init_routes()

    def __init_cors(self) -> None:
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __init_routes(self) -> None:
        file_routing.responses[http.HTTPStatus.NOT_FOUND] = ExceptionModel
        self.include_router(file_routing)
