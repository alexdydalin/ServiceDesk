from sqlalchemy import create_engine
from models import Base

# SQLite база
SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./servicedesk.db"

# Синхронный engine для миграций и создания таблиц
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},
    pool_size=5,
    echo=True  # Логирование SQL запросов
)

def create_tables():
    """Создание всех таблиц в БД"""
    Base.metadata.create_all(bind=engine)
    print("INFO все таблицы созданы")