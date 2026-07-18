from sqlalchemy.orm import Session
from app.models import URL


def create_url(db: Session, original_url: str):
    url = URL(original_url=original_url)

    db.add(url)
    db.commit()
    db.refresh(url)

    return url