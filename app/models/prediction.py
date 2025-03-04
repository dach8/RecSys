from item import ClothingItem
class PredictionRequest:
    def __init__(self, request_id: int, user_id: int, clothing_items: list[ClothingItem], timestamp: str):
        self.__request_id = request_id
        self.__user_id = user_id
        self.__clothing_items = clothing_items  #Список вещей для предсказания
        self.__timestamp = timestamp

    def get_request_id(self) -> int:
        return self.__request_id

    def get_user_id(self) -> int:
        return self.__user_id

    def get_clothing_items(self) -> list[ClothingItem]:
        return self.__clothing_items

    def get_timestamp(self) -> str:
        return self.__timestamp


class PredictionHistory:
    def __init__(self, history_id: int, user_id: int, request_id: int, predicted_item: ClothingItem, cost: float):
        self.__history_id = history_id
        self.__user_id = user_id
        self.__request_id = request_id
        self.__predicted_item = predicted_item  #Предсказанная вещь
        self.__cost = cost  #Стоимость предсказания

    def get_history_id(self) -> int:
        return self.__history_id

    def get_user_id(self) -> int:
        return self.__user_id

    def get_request_id(self) -> int:
        return self.__request_id

    def get_predicted_item(self) -> ClothingItem:
        return self.__predicted_item

    def get_cost(self) -> float:
        return self.__cost