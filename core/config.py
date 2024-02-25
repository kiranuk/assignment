import os

import boto3
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME:str = "test_app"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER", "hos_app")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "hos_app")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT", 5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB", "test_db")
    print(os.getenv("POSTGRES_USER"))
    print(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB, '>>>>>>>>>>>>>>>>>>>>>>>>')
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    s3_client = boto3.client('s3', region_name='your-region', aws_access_key_id='your-access-key',
                             aws_secret_access_key='your-secret-key')
settings = Settings()