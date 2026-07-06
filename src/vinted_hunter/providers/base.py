from abc import ABC, abstractmethod

class SearchProvider(ABC):

    @abstractmethod
    async def search(self):
        ...
    from abc import ABC, abstractmethod

from vinted_hunter.models.item import Item


class SearchProvider(ABC):
    @abstractmethod
    async def search(self) -> list[Item]:
        """Return found items."""
        raise NotImplementedError