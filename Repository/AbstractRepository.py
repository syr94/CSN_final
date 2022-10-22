
from abc import ABC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys
from typing import TypeVar, Generic
import os

T = TypeVar('T')


class AbstractRepository(ABC):
    
    table_name = ''
    item_obj = Generic[T]

    def __init__(self) -> None:
        try:
            db_connection_string = os.getenv('DB_CONNECTION_STRING')
            print("connecting to DB:", os.getenv('DB_CONNECTION_STRING'))
            self.engine = create_engine(db_connection_string)
            Base = declarative_base()
            Base.metadata.create_all(self.engine)
        except:
            pass

    def add_all(self, object_item_list: list) -> None:
        with Session(self.engine) as session:
            try:
                session.begin()
                session.add_all(object_item_list)
                session.commit()
            except Exception:
                session.rollback()
                e = sys.exc_info()[1]
                print(e.args[0])
    
    def add(self, object_item : Generic[T]) -> None:
        with Session(self.engine) as session:
            try:
                session.begin()
                session.add(object_item)
                session.commit()
            except Exception:
                session.rollback()
                e = sys.exc_info()[1]
                print(e.args[0])

    def find_all_by(self, by = "id", value = "") -> list:
        with Session(self.engine) as session:
            try:
                if isinstance(value, list): 
                    return session.query(self.item_obj).filter(getattr(self.item_obj, by).in_(value)).all()
                else:
                    return session.query(self.item_obj).filter(getattr(self.item_obj, by) == value).all()
            except:
                e = sys.exc_info()[1]
                print(e.args[0])

    def find_one_by(self, by = "id", value = "") -> list:
        with Session(self.engine) as session:
            try:
                session.begin()
                a = getattr(self.item_obj, by)
                return session.query(self.item_obj).filter(getattr(self.item_obj, by) == value).first()
            except:
                session.rollback()
                e = sys.exc_info()[1]
                print(e.args[0])
    
    def update(self, object_item : Generic[T]) -> None:
         with Session(self.engine) as session:
            try:
                session.begin()
                session.merge(object_item)
                session.commit()
            except:
                session.rollback()
                e = sys.exc_info()[1]
                print(e.args[0])

    def delete_by(self, by = "name", value = "") -> None:
        with Session(self.engine) as session:
            try:
                session.begin()
                session.query(self.item_obj).filter(getattr(self.item_obj, by) == value).delete()
                session.commit()
            except:
                session.rollback()
                e = sys.exc_info()[1]
                print(e.args[0])


