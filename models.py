class Book:
    """Класс, представляющий модель книги."""
    def __init__(self, author: str, title: str, rating: int, read_date: str):
        self.author = author.strip()
        self.title = title.strip()
        self.rating = int(rating)
        self.read_date = read_date.strip()

    def to_dict(self) -> dict:
        """Преобразование объекта книги в словарь для сохранения в JSON."""
        return {
            "author": self.author,
            "title": self.title,
            "rating": self.rating,
            "read_date": self.read_date
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Создание объекта книги из словаря."""
        return cls(data["author"], data["title"], data["rating"], data["read_date"])
