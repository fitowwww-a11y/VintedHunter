from vinted_hunter.models.item import Item
from vinted_hunter.storage.sent_items import SentItemsStorage


class DuplicateChecker:

    def __init__(self):
        self.storage = SentItemsStorage()
        self.sent = self.storage.load()

    def filter(self, items: list[Item]) -> list[Item]:
        result = []

        for item in items:

            if item.id in self.sent:
                continue

            result.append(item)

            self.storage.save(item.id)

        return result