# from models.user import User
import os, sys

my_lib_path = os.path.abspath('C:/Users/Pussy Killer/Desktop/ML/ML_Ops/project_recommendation/app/models/')
sys.path.append(my_lib_path)

from sqlmodel import Session
from app.database import init_db, get_session
from app.services.crud.user import register_user, get_user_by_id, get_user_by_email
from app.services.crud.account import get_account_by_user_id, update_account_balance

def test_user_creation():
    # Инициализация БД
    init_db()
    session = next(get_session())

    try:
        # Создание пользователя через CRUD
        user = register_user(
            session=session,
            name="Test User",
            email="test@example.com",
            male=True,
            password="secure_password123"
        )
        assert user.user_id is not None

        # Проверка существования пользователя
        db_user = get_user_by_id(session, user.user_id)
        assert db_user.email == "test@example.com"

        # Проверка создания аккаунта
        account = get_account_by_user_id(session, user.user_id)
        assert account.balance == 0.0

        # Тест пополнения баланса
        update_account_balance(session, account, 150.0)
        updated_account = get_account_by_user_id(session, user.user_id)
        assert updated_account.balance == 150.0

        # Проверка поиска по email
        found_user = get_user_by_email(session, "test@example.com")
        assert found_user.user_id == user.user_id

    finally:
        # Очистка после теста
        session.rollback()
        session.close()

if __name__ == "__main__":
    test_user_creation()

