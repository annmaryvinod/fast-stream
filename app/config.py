from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    kafka_bootstrap_servers: str = "localhost:9092"

    class Config:
        env_file = ".env"

settings = Settings()
