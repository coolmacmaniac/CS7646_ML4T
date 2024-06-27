from typing import List
from pydantic import BaseModel, StrictStr


class Portfolio(BaseModel):
    description: StrictStr
    symbols: List[StrictStr]
    start_date: StrictStr
    end_date: StrictStr
    weights: List[float]
    initial_value: int


class PortfolioConfig(BaseModel):
    portfolio: Portfolio
