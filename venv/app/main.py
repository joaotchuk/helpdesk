from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models import user, ticket
from app.routes import user
from app.routes import ticket


app = FastAPI()

app.include_router(user.router)

app.include_router(ticket.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "API HelpDesk rodando 🚀"}