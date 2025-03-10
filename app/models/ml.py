from item import Item
from prediction import PredictionHistory
from settings import EXECUTION_COST
from ..services.crud.account import get_account_by_user_id, update_account_balance
from ..services.crud.prediction import create_prediction_history
from ..services.crud.user import get_user_by_id

from sqlmodel import SQLModel, Field, Relationship, Session
from typing import Optional, List
from .prediction import PredictionRequest


class MLModel(SQLModel, table=True):
    model_id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    def predict(self, session: Session, clothing_items: List[Item]) -> Item:
        if not clothing_items:
            raise ValueError("Список вещей для предсказания пуст")

        # TODO: Реализовать логику предсказания
        # Временная заглушка - возвращаем первый элемент
        return clothing_items[0]

    def execute(self, session: Session) -> Item:
        # Получаем пользователя и аккаунт через CRUD
        user = get_user_by_id(session, self.user_id)
        user_account = get_account_by_user_id(session, self.user_id)

        if not user or not user_account:
            raise ValueError("Пользователь или аккаунт не найден")

        try:
            if user_account.balance >= EXECUTION_COST:
                # Обновляем баланс через CRUD
                updated_account = update_account_balance(
                    session=session,
                    account=user_account,
                    new_balance=user_account.balance - EXECUTION_COST
                )

                # Получаем связанный запрос
                request = session.get(PredictionRequest, self.request_id)
                if not request:
                    raise ValueError("Запрос на предсказание не найден")

                # Выполняем предсказание
                predicted_item = self.model.predict(
                    session=session,
                    clothing_items=request.clothing_items
                )

                # Создаем запись истории через CRUD
                history = PredictionHistory(
                    user_id=self.user_id,
                    request_id=self.request_id,
                    predicted_item_id=predicted_item.item_id,
                    cost=EXECUTION_COST
                )
                create_prediction_history(session=session, history=history)

                return predicted_item
            else:
                raise ValueError("Недостаточно средств на балансе")

        except Exception as e:
            # Откатываем транзакцию при ошибке
            session.rollback()
            # Восстанавливаем баланс
            if user_account:
                update_account_balance(
                    session=session,
                    account=user_account,
                    new_balance=user_account.balance + EXECUTION_COST
                )
            raise e


class MLTask(SQLModel, table=True):
    task_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id")
    request_id: int = Field(foreign_key="predictionrequest.request_id")
    model_id: int = Field(foreign_key="mlmodel.model_id")

    user: Optional["User"] = Relationship()
    request: Optional[PredictionRequest] = Relationship()
    model: Optional[MLModel] = Relationship()





# class MLModel:
#     def __init__(self, model_id: int, name: str):
#         self.__model_id = model_id
#         self.__name = name
#
#     @property
#     def model_id(self) -> int:
#         return self.__model_id
#
#     @property
#     def name(self) -> str:
#         return self.__name
#

#
#
# class MLTask:
#     def __init__(self, task_id: int, user_id: int, request: PredictionRequest, model: MLModel):
#         self.__task_id = task_id
#         self.__user_id = user_id
#         self.__request = request
#         self.__model = model
#
#
