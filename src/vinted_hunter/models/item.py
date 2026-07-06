from dataclasses import dataclass


@dataclass(slots=True)
class Item:
    id: str
    title: str
    brand: str
    price: float
    size: str
    url: str
    image_url: str