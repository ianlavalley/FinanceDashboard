from dataclasses import dataclass
from typing import List

@dataclass
class BuyerInfo:
    name: str
    monthly_income: float
    monthly_stock: float
    savings_all: float
    monthly_all_total: float

@dataclass
class Buyers:
    buyer_info: List[BuyerInfo]