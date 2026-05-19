def get_average_rating(books: list) -> float:
    """Подсчет средней оценки по всем книгам."""
    if not books:
        return 0.0
    total = sum(book.rating for book in books)
    return round(total / len(books), 2)

def get_author_stats(books: list) -> dict:
    """Формирование статистики по авторам (количество книг и их список)."""
    stats = {}
    for book in books:
        if book.author not in stats:
            stats[book.author] = {"count": 0, "books": []}
        stats[book.author]["count"] += 1
        stats[book.author]["books"].append(book.title)
    return stats
