from fastapi import HTTPException
from fastapi import FastAPI,Body

app=FastAPI()



BOOKS = [
    {'title': 'Title One', 'author': 'Author One', 'category': 'science'},
    {'title': 'Title Two', 'author': 'Author Two', 'category': 'science'},
    {'title': 'Title Three', 'author': 'Author Three', 'category': 'history'},
    {'title': 'Title Four', 'author': 'Author Four', 'category': 'math'},
    {'title': 'Title Five', 'author': 'Author Five', 'category': 'math'},
    {'title': 'Title Six', 'author': 'Author Two', 'category': 'math'}
]



@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/books")
async def get_books():
    return BOOKS


#giving dynamic param

# @app.get("/books/{dynamic_param}")
# async def get_books(dynamic_param:str):  # :str means it must be a string
#     return {"dynamic param": dynamic_param}


@app.get("/books/{book_title}")

async def get_book(book_title:str):
    for book in BOOKS:
        if book.get('title').casefold()==book_title.casefold():
            return book
        

#query parameter

@app.get("/books/catergory/")

async def book_by_category(category:str):
    book_to_return=[]
    for book in BOOKS:
        if book.get('category').casefold()==category.casefold():
         book_to_return.append(book)
    
    return book_to_return


#query plus dynamic 

@app.get("/books/{author_book}/")
async def book_by_author_category(author_book:str, category:str):
    books_to_return =[]
    for book in BOOKS:
        if book.get('author').casefold()== author_book.casefold() and book.get('category').casefold()==category.casefold():
            books_to_return.append(book)

    return books_to_return




    #post request 
@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)
    return new_book


#update put request

@app.put("/books/update_book/{book_title}")
async def update_book_by_title(book_title:str, updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS[i]=updated_book
            return updated_book
        
    raise HTTPException(status_code=404, detail="Book not found")


#delete request

@app.delete("/books/delete_book/{book_title}")
async def delete_book_by_title(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold()==book_title.casefold():
            BOOKS.pop(i)
            return {"message": "Book deleted successfully"}
        
    raise HTTPException(status_code=404, detail="Book not found")
