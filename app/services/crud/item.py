from typing import List, Optional
from sqlmodel import Session
from app.models.item import Item


def get_all_items(session: Session) -> List[Item]:
    return session.query(Item).all()


def get_item_by_id(session: Session, item_id: int) -> Optional[Item]:
    return session.get(Item, item_id)


def create_item(session: Session, item: Item) -> Item:
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


def update_item(session: Session, item_id: int, new_data: dict) -> Optional[Item]:
    item = session.get(Item, item_id)
    if item:
        for key, value in new_data.items():
            setattr(item, key, value)
        session.add(item)
        session.commit()
        session.refresh(item)
    return item


def delete_item(session: Session, item_id: int) -> None:
    item = session.get(Item, item_id)
    if item:
        session.delete(item)
        session.commit()
