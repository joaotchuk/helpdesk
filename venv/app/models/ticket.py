from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.connection import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="open")
    user_id = Column(Integer, ForeignKey("users.id"))