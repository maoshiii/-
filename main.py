import storage
import stats

def print_menu():
    print("\n=== ТРЕКЕР ПРОЧИТАННЫХ КНИГ ===")
    print("1. Добавить книгу")
    print("2. Показать все книги")
    print("3. Показать среднюю оценку")
    print("4. Статистика по авторам")
    print("5. Удалить книгу")
    print("6. Выход")

def main():
    while True:
        print_menu()
        choice = input("\nВыберите действие (1-6): ").strip()
        
        if choice == "1":
            author = input("Введите автора: ")
            title = input("Введите название книги: ")
            try:
                rating = int(input("Введите оценку (1-5): "))
                if not (1 <= rating <= 5):
                    print("Ошибка: Оценка должна быть от 1 до 5!")
                    continue
            except ValueError:
                print("Ошибка: Оценка должна быть целым числом!")
                continue
            read_date = input("Введите дату прочтения (например, YYYY-MM-DD): ")
            
            success, message = storage.add_book(author, title, rating, read_date)
            print(message)
            
        elif choice == "2":
            books = storage.load_books()
            if not books:
                print("\nВаш трекер пока пуст.")
            else:
                print("\n--- Список прочитанных книг ---")
                for idx, book in enumerate(books, 1):
                    print(f"{idx}. {book.author} — «{book.title}» | Оценка: {book.rating} | Дата: {book.read_date}")
                    
        elif choice == "3":
            books = storage.load_books()
            avg = stats.get_average_rating(books)
            print(f"\nСредняя оценка всех прочитанных книг: {avg} / 5")
            
        elif choice == "4":
            books = storage.load_books()
            author_data = stats.get_author_stats(books)
            if not author_data:
                print("\nНет данных для статистики.")
            else:
                print("\n--- Статистика по авторам ---")
                for author, info in author_data.items():
                    titles = ", ".join(f"«{t}»" for t in info["books"])
                    print(f"• {author}: прочитано книг — {info['count']} ({titles})")
                    
        elif choice == "5":
            author = input("Введите автора книги для удаления: ")
            title = input("Введите название книги для удаления: ")
            if storage.delete_book(author, title):
                print("Книга успешно удалена!")
            else:
                print("Книга с такими данными не найдена.")
                
        elif choice == "6":
            print("Выход из программы. Приятного чтения!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите пункт от 1 до 6.")

if __name__ == "__main__":
    main()
