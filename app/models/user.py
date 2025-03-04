class User:
    def __init__(self, user_id: int, name: str, male: bool, email: str, password: str, balance: float = 0.0):
        self.__user_id = user_id
        self.__name = name
        self.__male = male
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