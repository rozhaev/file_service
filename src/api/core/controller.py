from fastapi import Depends
from injector import Injector

from src.api.core.container import get_container_injector


class BaseController:
    injector: Injector = Depends(get_container_injector)
