from sqlalchemy.orm import sessionmaker
from engine import engine

# Создание фабрики сессий
SessionLocal = sessionmaker(
    autoflush=False, # при False требуется прописывать session.commit()
    bind=engine
)

def get_db():
    """
    Dependency для FastAPI, предоставляет сессию БД.
    Автоматически закрывает сессию после завершения запроса.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()