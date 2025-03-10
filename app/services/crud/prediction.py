from typing import List, Optional
from sqlmodel import Session
from app.models.prediction import PredictionRequest, PredictionHistory

# Для PredictionRequest
def create_prediction_request(session: Session, request: PredictionRequest) -> PredictionRequest:
    session.add(request)
    session.commit()
    session.refresh(request)
    return request

def get_prediction_request(session: Session, request_id: int) -> Optional[PredictionRequest]:
    return session.get(PredictionRequest, request_id)

# Для PredictionHistory
def create_prediction_history(session: Session, history: PredictionHistory) -> PredictionHistory:
    session.add(history)
    session.commit()
    session.refresh(history)
    return history

def get_user_prediction_history(session: Session, user_id: int) -> List[PredictionHistory]:
    return session.query(PredictionHistory).filter(PredictionHistory.user_id == user_id).all()