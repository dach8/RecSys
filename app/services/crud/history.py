from sqlmodel import Session
from app.models.prediction import PredictionHistory


def add_history(session: Session, history: PredictionHistory) -> PredictionHistory:
    session.add(history)
    session.commit()
    session.refresh(history)
    return history


def get_user_history(session: Session, user_id: int) -> list[PredictionHistory]:
    return session.query(PredictionHistory).filter(PredictionHistory.user_id == user_id).all()
