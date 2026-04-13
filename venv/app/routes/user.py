from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate
from app.models.ticket import Ticket


router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):
    db: Session = SessionLocal()

    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    db.close()

    return {"message": "Usuário criado com sucesso"}


@router.get("/users")
def list_users():
    db: Session = SessionLocal()

    users = db.query(User).all()

    db.close()

    return users

@router.get("/tickets")
def list_tickets():
    db: Session = SessionLocal()

    tickets = db.query(Ticket).all()

    db.close()

    return tickets