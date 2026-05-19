import json
import os
from models import Book

FILE_PATH = "books.json"

def load_books() -> list:
    """Загрузка списка книг из файла JSON."""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Book.from_dict(book) for book in data]
    except (json.JSONDecodeError, KeyError):
        return []

def save_books(books: list) -> None:
    """Сохранение списка книг в файл JSON."""
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump([book.to_dict() for book in books], f, ensure_ascii=False, indent=4)

def add_book(author: str, title: str, rating: int, read_date: str) -> tuple[bool, str]:
    """
    Добавление новой книги с проверкой на дубликаты.
    Реализовано в рамках Issue #1.
    """
    books = load_books()
    
    # Проверка на дубликаты (регистронезависимая)
    for book in books:
        if book.author.lower() == author.strip().lower() and book.title.lower() == title.strip().lower():
            return False, "Ошибка: Такая книга этого автора уже есть в трекере!"
            
    try:
        new_book = Book(author, title, rating, read_date)
        books.append(new_book)
        save_books(books)
        return True, "Книга успешно добавлена!"
    except ValueError:
        return False, "Ошибка: Некорректные данные книги."

def delete_book(author: str, title: str) -> bool:
    """Удаление книги по автору и названию."""
    books = load_books()
    initial_count = len(books)
    
    books = [b for b in books if not (b.author.lower() == author.strip().lower() and b.title.lower() == title.strip().lower())]
    
    if len(books) < initial_count:
        save_books(books)
        return True
    return False
