from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, Dict
from datetime import datetime


class Prediction(SQLModel, table=True):
    prediction_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    user_preferences: Dict = Field(default={})
    selected_outfits: List[int] = Field(default=[])
    recommended_items: List[int] = Field(default=[])
    
    user: Optional["User"] = Relationship(back_populates="predictions")


class PredictionRequest(SQLModel, table=True):
    request_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    timestamp: str

    user: Optional["User"] = Relationship(back_populates="prediction_requests")


class PredictionHistory(SQLModel, table=True):
    history_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    request_id: int = Field(foreign_key="predictionrequest.request_id")
    predicted_item_id: int = Field(foreign_key="item.item_id")
    cost: float

    user: Optional["User"] = Relationship(back_populates="prediction_history")
    request: Optional[PredictionRequest] = Relationship(back_populates="history")