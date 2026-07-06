from vinted_hunter.config.settings import settings
from vinted_hunter.core.logger import app_logger


def main():
    app_logger.info("Vinted Hunter started")
    app_logger.info(f"Check interval: {settings.check_interval}")
    app_logger.info(f"Log level: {settings.log_level}")


if __name__ == "__main__":
    main()