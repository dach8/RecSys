from typing import List, Optional
from sqlmodel import Session
from app.models.ml import MLModel, MLTask

# Для MLModel
def create_ml_model(session: Session, model: MLModel) -> MLModel:
    session.add(model)
    session.commit()
    session.refresh(model)
    return model

def get_all_models(session: Session) -> List[MLModel]:
    return session.query(MLModel).all()

def get_model_by_name(session: Session, name: str) -> Optional[MLModel]:
    return session.query(MLModel).filter(MLModel.name == name).first()

# Для MLTask
def create_ml_task(session: Session, task: MLTask) -> MLTask:
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def get_task_by_id(session: Session, task_id: int) -> Optional[MLTask]:
    return session.get(MLTask, task_id)