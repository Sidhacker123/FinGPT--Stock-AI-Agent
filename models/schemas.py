
from pydantic import BaseModel
from typing import List, Optional

class UserRequest(BaseModel):
    user_id: str
    income: float
    risk_tolerance: str
    goals: List[str]
    debt_details: Optional[List[str]] = None

class AIResponse(BaseModel):
    summary: str
    actions: List[str]
    data: Optional[dict]
