from vinted_hunter.models.item import Item
from vinted_hunter.providers.base import SearchProvider


class VintedProvider(SearchProvider):
    async def search(self) -> list[Item]:
        """
        Здесь позже будет получение товаров.
        Пока возвращаем пустой список.
        """
        return []