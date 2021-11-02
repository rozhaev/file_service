from src.api.core.application import Application
from src.api.core.container import ApplicationContainer
from src.api.settings import Settings


def init_app():
    settings = Settings()
    application = Application(settings, ApplicationContainer)
    return application


app = init_app()
