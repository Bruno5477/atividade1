from livros_repository import *
from bson import ObjectId

def format_book(book):
    book["_id"] = str(book["_id"])
    return book

def get_all_books_service():
    books = get_all_books()
    return [format_book(book) for book in books]

def create_book_service(book):
    result = create_book(book.model_dump())
    return {"message": "Book created", "id": str(result.inserted_id)}

def get_book_by_id_service(book_id):
    try:
        book = get_book_by_id(book_id)
    except:
        return {"error": "Invalid ID"}
    if not book:
        return {"error": "Book not found"}
    return format_book(book)

def update_book_service(book_id, book):
    try:
        result = update_book(book_id, book.model_dump())
    except:
        return {"error": "Invalid ID"}
    if result.matched_count == 0:
        return {"error": "Book not found"}
    return {"message": "Book updated"}

def delete_book_service(book_id):
    try:
        result = delete_book(book_id)
    except:
        return {"error": "Invalid ID"}
    if result.deleted_count == 0:
        return {"error": "Book not found"}
    return {"message": "Book deleted"}