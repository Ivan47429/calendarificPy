import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Central configuration class for the testing framework."""

    @staticmethod
    def get_env_variable(key: str, default: Optional[str] = None) -> str:
        value = os.getenv(key, default)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is not set and no default provided")
        return value

    @staticmethod
    def get_calendarific_api_key() -> str:
        return Config.get_env_variable("CALENDARIFIC_API_KEY")

    @staticmethod
    def get_base_url() -> str:
        from common.constants import CALENDARIFIC_BASE_URL
        return Config.get_env_variable("CALENDARIFIC_BASE_URL", CALENDARIFIC_BASE_URL)


# Singleton instance
config = Config()
