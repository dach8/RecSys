from sqlmodel import Session
from app.database import init_db, engine
from app.models.user import User
from app.models.account import Account
from app.models.item import Item
from app.models.ml import MLModel


def init_demo_data():
    init_db()
    with Session(engine) as session:
        # Демо-пользователь
        user = User(
            name="Demo User",
            email="demo@example.com",
            male=True,
            password_hash="hashed_password"
        )
        session.add(user)

        # Демо-аккаунт
        account = Account(user_id=user.user_id, balance=100.0)
        session.add(account)

        # Базовые модели ML
        model1 = MLModel(name="Style Recommender v1")
        model2 = MLModel(name="Color Matcher v2")
        session.add_all([model1, model2])

        session.commit()


if __name__ == "__main__":
    init_demo_data()