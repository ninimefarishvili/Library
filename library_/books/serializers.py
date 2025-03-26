from ninja import Schema
from datetime import datetime
from typing import List, Optional

class GenreSchema(Schema):
    id: int
    name: str
    description: str

class BookSchema(Schema):
    id: int
    title: str
    author: str
    published_date: Optional[datetime]
    genres: List[GenreSchema] = []
    borrowed_by: Optional[str]
    borrow_date: Optional[datetime]


    class Config:
        orm_mode = True