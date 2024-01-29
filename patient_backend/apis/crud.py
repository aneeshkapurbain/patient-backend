from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from patient_backend.models.main_models import Item

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_item(db, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def get_items(db, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()

def create_item(db, item: dict):
    db_item = Item(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db, item_id: int, item: dict):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    for key, value in item.items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(db, item_id: int):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    db.delete(db_item)
    db.commit()
    return {"message": f"Item {item_id} deleted"}