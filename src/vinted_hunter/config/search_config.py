from dataclasses import dataclass


@dataclass(slots=True)
class SearchConfig:
    brands: list[str]
    max_price: float
    min_price: float
    sizes: list[str]
    query: str