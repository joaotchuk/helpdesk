from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.models.ticket import Ticket
from app.models.user import User
from app.schemas.ticket import TicketCreate
router = APIRouter()

@router.post("/tickets")
def create_ticket(ticket: TicketCreate):
    db: Session = SessionLocal()

    new_ticket = Ticket(
        title=ticket.title,
        description=ticket.description,
        user_id=ticket.user_id
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    db.close()

    return {"message": "Chamado criado com sucesso"}

@router.put("/tickets/{ticket_id}")
def update_ticket(ticket_id: int, status: str):
    db: Session = SessionLocal()

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        db.close()
        return {"error": "Chamado não encontrado"}

    if status not in ["open", "in_progress", "closed"]:
        db.close()
        return {"error": "Status inválido"}

    ticket.status = status

    db.commit()
    db.close()

    return {"message": "Status atualizado com sucesso"}

@router.get("/dashboard")
def dashboard():
    db: Session = SessionLocal()

    total_users = db.query(User).count()
    total_tickets = db.query(Ticket).count()
    open_tickets = db.query(Ticket).filter(Ticket.status == "open").count()
    closed_tickets = db.query(Ticket).filter(Ticket.status == "closed").count()

    db.close()

    return {
        "total_users": total_users,
        "total_tickets": total_tickets,
        "open_tickets": open_tickets,
        "closed_tickets": closed_tickets
    }

@router.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: int):
    db: Session = SessionLocal()

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    db.close()

    if not ticket:
        return {"error": "Chamado não encontrado"}

    return ticket

@router.delete("/tickets/{ticket_id}")
def delete_ticket(ticket_id: int):
    db: Session = SessionLocal()

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        db.close()
        return {"error": "Chamado não encontrado"}

    db.delete(ticket)
    db.commit()

    db.close()

    return {"message": "Chamado removido com sucesso"}