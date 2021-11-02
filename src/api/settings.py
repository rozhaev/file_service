from pathlib import Path

from pydantic import BaseSettings

base_dir = Path(__file__).parent.parent.parent.absolute()


class Settings(BaseSettings):
    mongo_username: str
    mongo_password: str
    mongo_host: str
    mongo_port: str
    mongo_database: str
    redis_host: str
    redis_port: str
    redis_db: int

    @property
    def mongo_dsn(self) -> str:
        return 'mongodb://{}:{}@{}:{}/'.format(
            self.mongo_username,
            self.mongo_password,
            self.mongo_host,
            self.mongo_port,
        )

    @property
    def redis_dsn(self) -> str:
        return 'redis://{}:{}/{}'.format(
            self.redis_host,
            self.redis_port,
            self.redis_db
        )

    class Config:
        env_file = f'{base_dir}/.env'
