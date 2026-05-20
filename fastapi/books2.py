
from datetime import date
from typing import Optional
from fastapi import FastAPI, HTTPException,Path, Query
from pydantic import BaseModel, Field

app=FastAPI()


#real objects

class Book:
    id: int
    title: str
    author: str
    description: str
    ratting: int
    date_published: int


    def __init__(self, id, title, author, description, ratting, date_published):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.ratting = ratting
        self.date_published = date_published

class Bookvalidate(BaseModel):
    id: Optional[int]= Field(description="The ID of the book, it will be auto generated", default=None)
    title: str = Field(max_length=100)
    author: str = Field(max_length=100)
    description: str = Field(min_length=10, max_length=200)
    ratting: int = Field(ge=-1, le=6)
    date_published: int = Field(ge=0, le=2026)

    model_config={
        "json_schema_extra":{
            "example":{
                "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald",
                "description": "A novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.",
                "ratting": 4,
                "date_published": 1925
            }
        }
    }


BOOKS=[
    Book(1,"The Great Gatsby","F. Scott Fitzgerald","A novel set in the Roaring Twenties, exploring themes of wealth, love, and the American Dream.", 4, 1925),
    Book(2,"To Kill a Mockingbird","Harper Lee","A powerful story of racial injustice and moral growth in the American South.", 5, 1960),
    Book(3,"1984","George Orwell","A dystopian novel that delves into themes of totalitarianism, surveillance, and the loss of individuality.", 4, 1948),
    Book(4,"Pride and Prejudice","Jane Austen","A classic romance novel that explores themes of love, class, and societal expectations.", 5, 1813)
    
]


@app.get("/books")
async def get_books():
    return BOOKS

@app.post("/create_book")
async def create_book(new_book:Bookvalidate):
    new_book_object = Book(**new_book.model_dump())   #paydentic v2
    new_book_object = find_book_id(new_book_object)
    BOOKS.append(new_book_object)
    return new_book_object


def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1
    else:
        book.id=1
    return book

@app.get("/books/id")
async def get_book_by_id(id:int = Query(description="The ID of the book to retrieve", ge=0)):
    for book in BOOKS:
        if book.id==id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books/{date_published}")
async def get_book_by_date_published(date_published:int =Path(ge=0, le=2026)):
    book_to_return =[]
    for book in BOOKS:
        if book.date_published==date_published:
            book_to_return.append(book)
    return book_to_return   



