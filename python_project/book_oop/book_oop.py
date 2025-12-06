class Meta_manager(type):
    __required_methods = ['add_book', 'search_book', 'show_books']

    def __new__(cls, name, bases, dct):
        new_class = super().__new__(cls, name, bases, dct)
        for required in cls.__required_methods:
            if required not in dct:
                raise Exception(f"Class {name} must implement {required} method")
        return new_class


class Book:
    @staticmethod
    def validate_book(title, author, release):
        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(release, int):
            return False
        if not title.strip() or not author.strip():
            return False
        if release <= 0 or release > 2100:  
            return False
        return True

    def __init__(self, title, author, release):
        if Book.validate_book(title, author, release):
            self.title = title.strip()
            self.author = author.strip()
            self.release = release
        else:
            raise ValueError("Invalid book data")

    def __str__(self):
        return f"{self.title} by {self.author} ({self.release})"


class Book_manager(metaclass=Meta_manager):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def show_books(self):
        if not self.books:
            print("წიგნების სია ცარიელია.")
        else:
            print("\nყველა წიგნი:")
            for idx, b in enumerate(self.books, start=1):
                print(f"{idx}. {b}")

    def search_book(self, title: str):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None


def main():
    manager = Book_manager()

    while True:
        print("\n--- წიგნების მართვის სისტემა ---")
        print("1. ახალი წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სათაურით")
        print("4. გამოსვლა")

        choice = input("აირჩიეთ ოპცია (1-4): ").strip()

        if choice == "1":
            title = input("წიგნის სათაური: ").strip()
            author = input("ავტორი: ").strip()
            try:
                release = int(input("გამოცემის წელი: ").strip())
            except ValueError:
                print("წელი უნდა იყოს რიცხვი")
                continue

            try:
                book = Book(title, author, release)
                manager.add_book(book)
                print("წიგნი წარმატებით დაემატა!")
            except ValueError as e:
                print(f"შეცდომა: {e}")

        elif choice == "2":
            manager.show_books()

        elif choice == "3":
            title = input("შეიყვანეთ სათაური: ").strip()
            found = manager.search_book(title)
            if found:
                print(f"მოიძებნა: {found}")
            else:
                print("ასეთი წიგნი ვერ მოიძებნა.")

        elif choice == "4":
            print("პროგრამა დასრულდა.")
            break

        else:
            print("არასწორი არჩევანი, სცადეთ თავიდან.")


if __name__ == "__main__":
    main()
