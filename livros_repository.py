from mongo import books_collection
from bson import ObjectId

def create_book(book_dict):
    return books_collection.insert_one(book_dict)

def get_all_books():
    return list(books_collection.find())

def get_book_by_id(book_id):
    return books_collection.find_one({"_id": ObjectId(book_id)})

def update_book(book_id, book_dict):
    return books_collection.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": book_dict}
    )

def delete_book(book_id):
    return books_collection.delete_one({"_id": ObjectId(book_id)})