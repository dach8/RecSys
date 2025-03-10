from enum import Enum

class Category(Enum):
    T_SHIRT = "T-shirt"
    JEANS = "Jeans"
    DRESS = "Dress"
    SUIT = "Suit"
    SKIRT = "Skirt"
    TROUSERS = "Trousers"
    BOOTS = "Boots"
    SNEAKERS = "Sneakers"
    SHOES = "Shoes"

class ClothingStyle(Enum):
    SPORTY = "Sporty "
    CASUAL = "Casual"
    CLASSIC = "Classic"
    STREETWEAR = "Streetwear"
    PUNK = "Punk"

class Size(Enum):
    XS = "XS"
    S = "S"
    M = "M"
    L = "L"
    XL = "XL"
    XXL = "XXL"

class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    CYAN = "Cyan"
    MAGENTA = "Magenta"
    BLACK = "Black"
    WHITE = "White"
    GRAY = "Gray"
    ORANGE = "Orange"
    PURPLE = "Purple"
    BROWN = "Brown"
    PINK = "Pink"

class Material(Enum):
    COTTON = "Cottom"
    LINEN = "Linen"
    WOOL = "Wool"
    SILK = "Silk"
    POLYESTER = "Polyester"
    NYLON = "Nylon"
    LEATHER = "Leather"
    SUEDE = "Suede"
    DENIM = "Denim"
class User:
    def __init__(self, user_id: int, name: str, sex: bool, email: str, password: str, balance: float = 0.0):
        self.__user_id = user_id
        self.__name = name
        self.__sex = sex
        self.__email = email
        self.__password = password
        self.__balance = balance

    def get_user_id(self) -> int:
        return self.__user_id

    def get_name(self) -> str:
        return self.__name

    def get_email(self) -> str:
        return self.__email

    def get_sex(self) -> bool:
        return self.__sex

    def get_balance(self) -> float:
        return self.__balance

    def set_balance(self, amount: float):
        if amount >= 0:
            self.__balance = amount
        else:
            raise ValueError("Баланс не может быть отрицательным")

    def deduct_balance(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств на балансе")

    def add_balance(self, amount: float):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма пополнения должна быть положительной")

class Item:
    def __init__(self, item_id: int, discription: str, color: Color, material: Material, name: str, category: Category, price: float):
        self.__item_id = item_id
        self.__name = name
        self.__discription = discription
        self.__color = color
        self.__material = material
        self.__category = category
        self.__price = price


    def get_item_id(self) -> int:
        return self.__item_id

    def get_discription(self) -> str:
        return self.__discription

    def get_material(self) -> Material:
        return self.__material

    def get_color(self) -> Color:
        return self.__color

    def get_name(self) -> str:
        return self.__name

    def get_category(self) -> Category:
        return self.__category

    def get_price(self) -> float:
        return self.__price

class ClothingItem(Item):
    def __init__(self, item_id: int, discription: str, color: Color, material: Material, name: str, category: Category, price: float,
                 style: ClothingStyle, size: Size):
        super().__init__(item_id, discription, color, material, name, category, price)
        self.__style = style
        self.__size = size

    def get_style(self) -> ClothingStyle:
        return self.__style

    def get_size(self) -> Size:
        return self.__size

    # Переопределение метода
    def get_category(self) -> str:
        return f"Clothes: {super().get_category()}"

    def get_clothes_category(self) -> Category:
        return super().get_category()

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

class UserService:
    __users = {}

    @staticmethod
    def add_user(user: User):
        UserService.__users[user.get_user_id()] = user

    @staticmethod
    def get_user_by_id(user_id: int) -> User:
        return UserService.__users.get(user_id)

class HistoryService:
    __history = []
    @staticmethod
    def add_history(history: PredictionHistory):
        HistoryService.__history.append(history)

    @staticmethod
    def generate_history_id() -> int:
        return len(HistoryService.__history) + 1


