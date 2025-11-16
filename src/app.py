from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import uvicorn

# Импорты из нашей структуры
from db import *

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

@app.get("/")
async def root():
    return {"message": "ServiceDesk API"}

@app.get("/users/")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {"users": users}

@app.get("/tickets/")
async def get_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return {"tickets": tickets}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)