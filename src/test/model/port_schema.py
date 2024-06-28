from typing import List, Optional
from pydantic import BaseModel, StrictStr


class Portfolio(BaseModel):
    description: StrictStr
    symbols: List[StrictStr]
    start_date: Optional[StrictStr] = None
    end_date: Optional[StrictStr] = None
    weights: List[float]
    initial_value: int


class PortfolioConfig(BaseModel):
    portfolio: Portfolio
