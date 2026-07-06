from vinted_hunter.core.logger import app_logger
from vinted_hunter.database.init_db import init_database
from vinted_hunter.database.repository import ItemRepository
from vinted_hunter.filters.filter_engine import FilterEngine
from vinted_hunter.providers.fake_provider import FakeProvider
from vinted_hunter.services.notification_service import NotificationService


class Application:
    def __init__(self) -> None:
        self.provider = FakeProvider()
        self.repository = ItemRepository()
        self.notifications = NotificationService()

        self.filter_engine = FilterEngine(
            brands=["Nike", "Adidas"],
            max_price=100,
        )

    async def run_once(self) -> None:
        init_database()

        items = await self.provider.search()
        app_logger.info(f"Found {len(items)} items")

        filtered = self.filter_engine.filter(items)
        app_logger.info(f"After filtering: {len(filtered)} items")

        new_items = []

        for item in filtered:
            if self.repository.exists(item.id):
                app_logger.info(f"Skipping existing item: {item.title}")
                continue

            self.repository.save(item)
            app_logger.info(f"Saved: {item.title}")
            new_items.append(item)

        await self.notifications.send_items(new_items)