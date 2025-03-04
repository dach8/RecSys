from item import ClothingItem
from prediction import PredictionRequest, PredictionHistory
from services import UserService, HistoryService
class MLModel:
    def __init__(self, model_id: int, name: str):
        self.__model_id = model_id
        self.__name = name

    def predict(self, clothing_items: list[ClothingItem]) -> ClothingItem:
        #Здесь будет логика предсказания
        #TODO
        if clothing_items:
            return clothing_items[0]
        raise ValueError("Список вещей для предсказания пуст")

    def get_model_id(self) -> int:
        return self.__model_id

    def get_name(self) -> str:
        return self.__name

class MLTask:
    def __init__(self, task_id: int, user_id: int, request: PredictionRequest, model: MLModel):
        self.__task_id = task_id
        self.__user_id = user_id
        self.__request = request
        self.__model = model

    def execute(self) -> ClothingItem:
        # Проверка баланса пользователя
        user = UserService.get_user_by_id(self.__user_id)
        if user.get_balance() >= 10.0:
            predicted_item = self.__model.predict(self.__request.get_clothing_items())
            user.deduct_balance(10.0)
            history = PredictionHistory(
                history_id=HistoryService.generate_history_id(),
                user_id=self.__user_id,
                request_id=self.__request.get_request_id(),
                predicted_item=predicted_item,
                cost=10.0
            )
            HistoryService.add_history(history)
            return predicted_item
        else:
            raise ValueError("Недостаточно средств на балансе")