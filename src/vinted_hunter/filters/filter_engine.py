from vinted_hunter.models.item import Item


class FilterEngine:
    def __init__(
        self,
        brands: list[str],
        max_price: float,
    ):
        self.brands = [brand.lower() for brand in brands]
        self.max_price = max_price

    def filter(self, items: list[Item]) -> list[Item]:
        result = []

        for item in items:
            if item.brand.lower() not in self.brands:
                continue

            if item.price > self.max_price:
                continue

            result.append(item)

        return result