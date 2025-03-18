from fastapi import FastAPI, Depends, HTTPException, status, Response, Cookie
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from typing import List, Optional
import os, sys
from datetime import datetime
import secrets
import base64

from database.database import init_db, get_session
from services.crud.user import register_user, get_user_by_id, get_user_by_email
from services.crud.account import get_account_by_user_id, update_account_balance
from models.types import UserCreate, UserLogin, UserResponse, AccountResponse, PredictionRequest

app = FastAPI(title="Fashion Recommendation Service")
security = HTTPBasic()

active_sessions = {}

@app.on_event("startup")
async def startup_event():
    init_db()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return secrets.compare_digest(plain_password.encode(), hashed_password.encode())

def get_current_user(session_id: Optional[str] = Cookie(None), session: Session = Depends(get_session)):
    if not session_id or session_id not in active_sessions:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    user_email = active_sessions[session_id]
    user = get_user_by_email(session, user_email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user

# Эндпоинты аутентификации
@app.post("/register", response_model=UserResponse)
def create_user(user: UserCreate, session: Session = Depends(get_session)):
    db_user = get_user_by_email(session, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return register_user(session=session, **user.dict())

@app.post("/login")
def login(credentials: HTTPBasicCredentials = Depends(security), session: Session = Depends(get_session)):
    user = get_user_by_email(session, credentials.username)
    if not user or not user.check_password(credentials.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    
    # Создаем сессию
    session_id = base64.b64encode(os.urandom(32)).decode('utf-8')
    active_sessions[session_id] = user.email
    
    response = Response(content="Login successful")
    response.set_cookie(key="session_id", value=session_id)
    return response

@app.post("/logout")
def logout(response: Response, session_id: Optional[str] = Cookie(None)):
    if session_id and session_id in active_sessions:
        del active_sessions[session_id]
    response.delete_cookie(key="session_id")
    return {"message": "Logout successful"}

# Эндпоинты для работы с аккаунтом
@app.get("/account", response_model=AccountResponse)
def get_account(current_user = Depends(get_current_user), session: Session = Depends(get_session)):
    account = get_account_by_user_id(session, current_user.user_id)
    return account

@app.post("/account/deposit")
def deposit_money(amount: float, current_user = Depends(get_current_user), session: Session = Depends(get_session)):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")
    account = get_account_by_user_id(session, current_user.user_id)
    update_account_balance(session, account, account.balance + amount)
    return {"message": "Deposit successful", "new_balance": account.balance + amount}

# Эндпоинт для создания демо-пользователя
@app.post("/demo-user", response_model=UserResponse)
def create_demo_user(session: Session = Depends(get_session)):
    demo_email = f"demo_{datetime.now().timestamp()}@example.com"
    demo_user = UserCreate(
        email=demo_email,
        password="demo123",
        name="Demo User",
        male=True
    )
    return register_user(session=session, **demo_user.dict())

# Эндпоинты для работы с предсказаниями
@app.post("/predictions")
def create_prediction(
    request: PredictionRequest,
    current_user = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    account = get_account_by_user_id(session, current_user.user_id)
    if account.balance < 10.0:  # Предположим, что одно предсказание стоит 10 единиц
        raise HTTPException(status_code=402, detail="Insufficient funds")
    
    # Здесь будет логика создания предсказания
    # prediction = create_prediction_service(session, current_user.user_id, request)
    
    # Списание средств
    update_account_balance(session, account, account.balance - 10.0)
    
    return {"message": "Prediction created successfully"}

@app.get("/predictions/history")
def get_prediction_history(
    current_user = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Здесь будет логика получения истории предсказаний
    # predictions = get_user_predictions(session, current_user.user_id)
    return {"predictions": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
