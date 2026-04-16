from fastapi import APIRouter
from schemas import Book
from services import *

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/")
def list_books():
    return get_all_books_service()

@router.post("/")
def create_book(book: Book):
    return create_book_service(book)

@router.get("/{book_id}")
def get_book(book_id: str):
    return get_book_by_id_service(book_id)

@router.put("/{book_id}")
def update_book(book_id: str, book: Book):
    return update_book_service(book_id, book)

@router.delete("/{book_id}")
def delete_book(book_id: str):
    return delete_book_service(book_id)