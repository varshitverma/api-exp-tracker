from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Expense(BaseModel):
    id: Optional[int] = None
    amount: float
    category: str
    description: str
    date: datetime
    payment_method: str
    created_at: Optional[datetime] = None