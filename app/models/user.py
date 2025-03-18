from sqlmodel import SQLModel, Field, Relationship
import hashlib
from typing import Optional, List
from .account import Account


class User(SQLModel, table=True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str = Field(unique=True)
    male: bool
    password_hash: str

    account: Optional[Account] = Relationship(back_populates="user")
    predictions: List["Prediction"] = Relationship(back_populates="user")
    prediction_requests: List["PredictionRequest"] = Relationship(back_populates="user")
    prediction_history: List["PredictionHistory"] = Relationship(back_populates="user")

    def set_password(self, password: str):
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password: str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()