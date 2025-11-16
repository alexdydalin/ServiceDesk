from .models import Base, User, Operator, Ticket, Message
from engine import engine, create_tables
from session import get_db, SessionLocal

# Определяем что импортировать при from db import *
__all__ = [
    "Base", "get_db", "engine", "create_tables", "SessionLocal",
    "User", "Operator", "Ticket", "Message"
]