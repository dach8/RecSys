from user import User
from prediction import PredictionHistory
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


