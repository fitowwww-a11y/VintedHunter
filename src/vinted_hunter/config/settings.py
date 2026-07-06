from dataclasses import dataclass
from pathlib import Path
import os

from dotenv import load_dotenv

# Корень проекта
BASE_DIR = Path(__file__).resolve().parents[3]

# Загружаем .env
load_dotenv(BASE_DIR / ".env")


@dataclass
class Settings:
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")

    check_interval: int = int(os.getenv("CHECK_INTERVAL", "60"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()