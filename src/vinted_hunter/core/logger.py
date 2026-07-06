from pathlib import Path

from loguru import logger

# Корень проекта
BASE_DIR = Path(__file__).resolve().parents[3]

# Папка логов
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Удаляем стандартный логгер
logger.remove()

# Красивый вывод в терминал
logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
    colorize=True,
)

# Запись в файл
logger.add(
    LOG_DIR / "vinted_hunter.log",
    rotation="10 MB",
    retention="30 days",
    level="DEBUG",
    encoding="utf-8",
)

app_logger = logger