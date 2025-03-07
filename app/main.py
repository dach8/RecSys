from models.user import User
from models.services import UserService, HistoryService, PredictionHistory

if __name__ == "__main__":
    # Регистрация пользователя
    user = UserService.register_user(
        name="Иван Иванов",
        email="ivan@example.com",
        male=True,
        password="securepassword123"
    )

    # Получение аккаунта
    account = UserService.get_account(user.user_id)

    # Пополнение баланса
    account.add_balance(1000.0)

    # Проверка пароля
    print(user.check_password("wrongpass"))  # False
    print(user.check_password("securepassword123"))  # True

    # История операций
    history_entry = PredictionHistory(...)
    HistoryService.add_history(history_entry)

    print(test_user)