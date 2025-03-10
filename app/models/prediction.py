from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from .item import Item
from .user import User


class PredictionRequest(SQLModel, table=True):
    request_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    timestamp: str

    user: Optional[User] = Relationship()


class PredictionHistory(SQLModel, table=True):
    history_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    request_id: int = Field(foreign_key="predictionrequest.request_id")
    predicted_item_id: int = Field(foreign_key="item.item_id")
    cost: float

    user: Optional[User] = Relationship()
    predicted_item: Optional[Item] = Relationship()
# class PredictionRequest:
#     def __init__(self, request_id: int, user_id: int, clothing_items: list[ClothingItem], timestamp: str):
#         self.__request_id = request_id
#         self.__user_id = user_id
#         self.__clothing_items = clothing_items  #Список вещей для предсказания
#         self.__timestamp = timestamp
#
#     @property
#     def request_id(self) -> int:
#         return self.__request_id
#
#     @property
#     def user_id(self) -> int:
#         return self.__user_id
#
#     @property
#     def clothing_items(self) -> list[ClothingItem]:
#         return self.__clothing_items
#
#     @property
#     def timestamp(self) -> str:
#         return self.__timestamp
#
#
# class PredictionHistory:
#     def __init__(self, history_id: int, user_id: int, request_id: int, predicted_item: ClothingItem, cost: float):
#         self.__history_id = history_id
#         self.__user_id = user_id
#         self.__request_id = request_id
#         self.__predicted_item = predicted_item  #Предсказанная вещь
#         self.__cost = cost  #Стоимость предсказания
#
#     @property
#     def history_id(self) -> int:
#         return self.__history_id
#
#     @property
#     def user_id(self) -> int:
#         return self.__user_id
#
#     @property
#     def request_id(self) -> int:
#         return self.__request_id
#
#     @property
#     def predicted_item(self) -> ClothingItem:
#         return self.__predicted_item
#
#     @property
#     def cost(self) -> float:
#         return self.__cost
