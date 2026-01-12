from app.db import SessionLocal

def get_deb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
