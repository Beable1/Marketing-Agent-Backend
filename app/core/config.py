from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    project_name: str = "Marketing Agent API"
    debug: bool = False

    # S3
    aws_access_key_id: str
    aws_secret_access_key: str
    s3_endpoint_url: str | None = None   # None for AWS
    s3_region: str = "us-east-1"
    s3_bucket: str = "marketing-files"

settings = Settings()