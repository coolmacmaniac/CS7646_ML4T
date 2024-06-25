from typing import List
from pydantic import BaseModel, StrictStr


class Allocation(BaseModel):
    description: StrictStr
    weights: List[float]


class Portfolio(BaseModel):
    start_date: StrictStr
    end_date: StrictStr
    symbols: List[StrictStr]
    allocations: List[Allocation]
    initial_value: int


class PortfolioConfig(BaseModel):
    portfolios: List[Portfolio]
