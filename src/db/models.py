from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from pytz import timezone as tz
import enum

Base = declarative_base()


class TicketStatus(enum.Enum):
    WAITING = "waiting"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class SenderType(enum.Enum):
    USER = "user"
    OPERATOR = "operator"
    SYSTEM = "system"


def get_moscow_time():
    """Возвращает текущее время по Москве"""
    msk_tz = tz('Europe/Moscow')
    return datetime.now(msk_tz)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=True)
    tg_id = Column(Integer, unique=True, index=True, nullable=False)
    created_at = Column(DateTime, default=get_moscow_time())

    # Relationships
    # tickets = relationship("Ticket", back_populates="user")
    # operator = relationship("Operator", back_populates="user", uselist=False)


class Operator(Base):
    __tablename__ = "operators"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=get_moscow_time())

    # Relationships
    #user = relationship("User", back_populates="operator")
    #tickets = relationship("Ticket", back_populates="operator")


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(TicketStatus), default=TicketStatus.WAITING, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    operator_id = Column(Integer, ForeignKey("operators.id"), nullable=True)
    created_at = Column(DateTime, default=get_moscow_time())
    closed_at = Column(DateTime, nullable=True)

    # Relationships
    #user = relationship("User", back_populates="tickets")
    #operator = relationship("Operator", back_populates="tickets")
    #messages = relationship("Message", back_populates="ticket")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    ticket_id = Column(Integer, ForeignKey("tickets.id"), nullable=False)
    sender_type = Column(Enum(SenderType), nullable=False)
    sender_id = Column(Integer, nullable=False)  # user_id или operator_id
    message_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=get_moscow_time())

    # Relationships
    #ticket = relationship("Ticket", back_populates="messages")