# class Account:
#     def __init__(self, user_id: int, balance: float = 0.0):
#         self.__user_id = user_id
#         self.__balance = balance
#
#     @property
#     def user_id(self) -> int:
#         return self.__user_id
#
#     @property
#     def balance(self) -> float:
#         return self.__balance
#
#     @balance.setter
#     def balance(self, amount: float):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             raise ValueError("Баланс не может быть отрицательным")
#


from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from sqlmodel import Session


class Account(SQLModel, table=True):
    account_id: Optional[int] = Field(default=None, primary_key=True)
    balance: float = Field(default=0.0)
    user_id: int = Field(foreign_key="user.user_id")

    user: Optional["User"] = Relationship(back_populates="account")

    def deduct_balance(self, session: Session, amount: float):
        if self.balance >= amount:
            self.balance -= amount
            session.add(self)
            session.commit()
            session.refresh(self)
        else:
            raise ValueError("Недостаточно средств на балансе")

    def add_balance(self, session: Session, amount: float):
        if amount > 0:
            self.balance += amount
            session.add(self)
            session.commit()
            session.refresh(self)
        else:
            raise ValueError("Сумма пополнения должна быть положительной")