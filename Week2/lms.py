#  A fully functional Library Management System (lms.py) with features for book/user management, search, borrowing, and returning.
import json
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, List

DATA_FILE = "data.json"
DATE_FMT = "%Y-%m-%d"
class Book:
    def __init__(self,book_id:int, title: str, author: str, amount: int=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.amount = int(amount) 
        self.borrowed = 0
    def available(self) -> int:
        return self.amount - self.borrowed

    def to_dict(self) -> dict:
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "amount": self.amount,
            "borrowed": self.borrowed
        }
    @classmethod
    def from_dict(cls, d):
        book = cls(d["book_id"], d["title"], d["author"], d.get("amount", 1))
        book.borrowed = d.get("borrowed", 0)
        return book
class User:
    def __init__(self, user_id: int, name: str, email: str ='' ):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.borrowed_books: Dict[int, str] = {}
        
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, d):
        user = cls(d["user_id"], d["name"], d.get("email", ""))
        user.borrowed_books = {int(k): v for k, v in d.get("borrowed_books", {}).items()}
        return user
class Library:
    def __init__(self):
        self.books: Dict[int, Book] = {}
        self.users: Dict[int, User] = {}
        self.next_book_id = 1
        self.next_user_id = 1
        self.load() 

    def save(self, filename=DATA_FILE):
        data = {
            "books": {bid: book.to_dict() for bid, book in self.books.items()},
            "users": {uid: user.to_dict() for uid, user in self.users.items()},
            "next_book_id": self.next_book_id,
            "next_user_id": self.next_user_id
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[Saved] {filename}")

    def load(self, filename=DATA_FILE):
        if not os.path.exists(filename):
            return
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.books = {int(bid): Book.from_dict(bdict) for bid, bdict in data.get("books", {}).items()}
        self.users = {int(uid): User.from_dict(udict) for uid, udict in data.get("users", {}).items()}
        self.next_book_id = data.get("next_book_id", max(self.books.keys(), default=0) + 1)
        self.next_user_id = data.get("next_user_id", max(self.users.keys(), default=0) + 1)
        print(f"[Loaded] {filename} (books={len(self.books)}, users={len(self.users)})")

    # Book operations
    def add_book(self, title: str, author: str, amount: int = 1) -> Book:
        book = Book(self.next_book_id, title, author, amount)
        self.books[self.next_book_id] = book
        self.next_book_id += 1
        return book

    def list_books(self) -> List[Book]:
        return list(self.books.values())

    def find_books(self, query: str) -> List[Book]:
        q = query.lower()
        result = []
        for book in self.books.values():
            if q in book.title.lower() or q in book.author.lower():
                result.append(book)
        return result

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.books.get(book_id)

    # User operations
    def add_user(self, name: str, email: str = "") -> User:
        user = User(self.next_user_id, name, email)
        self.users[self.next_user_id] = user
        self.next_user_id += 1
        return user

    def list_users(self) -> List[User]:
        return list(self.users.values())

    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    # Borrow / Return
    def borrow_book(self, user_id: int, book_id: int, days=3) -> str:
        user = self.get_user(user_id)
        book = self.get_book(book_id)
        if user is None:
            return f"Error: user {user_id} not found."
        if book is None:
            return f"Error: book {book_id} not found."
        if book.available() <= 0:
            return f"Error: No copies available for '{book.title}'."
        # simple rule: one copy per user per book
        if book_id in user.borrowed_books:
            return f"Error: User already borrowed this book."
        due_date = (datetime.now() + timedelta(days=days)).strftime(DATE_FMT)
        user.borrowed_books[book_id] = due_date
        book.borrowed += 1
        return f"Success: Book '{book.title}' borrowed by {user.name}. Due: {due_date}"

    def return_book(self, user_id: int, book_id: int) -> str:
        user = self.get_user(user_id)
        book = self.get_book(book_id)
        if user is None:
            return f"Error: user {user_id} not found."
        if book is None:
            return f"Error: book {book_id} not found."
        if book_id not in user.borrowed_books:
            return f"Error: This user did not borrow this book."
        del user.borrowed_books[book_id]
        book.borrowed = max(0, book.borrowed - 1)
        return f"Success: Book '{book.title}' returned by {user.name}."
#---------- CLI helpers ----------

def print_book(b: Book):
    print(f"[{b.book_id}] '{b.title}' by {b.author}  amount: {b.amount} borrowed: {b.borrowed} available: {b.available()}")

def print_user(u: User):
    print(f"({u.user_id}) {u.name} <{u.email}> borrowed: {len(u.borrowed_books)}")
    for bid, due in u.borrowed_books.items():
        print(f"   - book_id {bid}, due {due}")

def help_text():
    print("""
Commands:
  1. add a book
  2. add a user
  3. list all books
  4. list all users
  5. search <q> (title/author)
  6. borrow <user_id> <book_id> [days] (default 3 days)
  7. return <user_id> <book_id>
  8. save data
  9. exit
  10.help
""")
def main():
    lib = Library()
    print(" Type '10' for commands.")
    while True:
        try:
            cmd = input("lms> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
            lib.save()
            break
        if not cmd:
            continue
        parts = cmd.split()
        action = parts[0]

        if action == '10':
            help_text()

        elif action == '1':
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            amount = input("Amount [1]: ").strip() or "1"
            try:
                amount_i = max(1, int(amount))
            except ValueError:
                amount_i = 1
            b = lib.add_book(title, author,amount_i)
            print("Added book: ")
            print(b)

        elif action == "2":
            name = input("Name: ").strip()
            email = input("Email: ").strip()
            u = lib.add_user(name, email)
            print("Added user:")
            print_user(u)

        elif action == "3":
            for b in lib.list_books():
                print_book(b)
            if not lib.books:
                print("(no books)")

        elif action == "4":
            for u in lib.list_users():
                print_user(u)
            if not lib.users:
                print("(no users)")

        elif action == "5":
            if len(parts) < 2:
                print("Usage: 5 <query>")
                continue
            q = " ".join(parts[1:])
            res = lib.find_books(q)
            if not res:
                print("No results.")
            else:
                for b in res:
                    print_book(b)

        elif action == "6":
            if len(parts) < 3:
                print("Usage: 6 <user_id> <book_id> [days]")
                continue
            try:
                uid = int(parts[1])
                bid = int(parts[2])
                days = int(parts[3]) if len(parts) > 3 else 3
            except ValueError:
                print("user_id, book_id and days must be integers.")
                continue
            print(lib.borrow_book(uid, bid, days))

        elif action == "7":
            if len(parts) < 3:
                print("Usage: 7 <user_id> <book_id>")
                continue
            try:
                uid = int(parts[1])
                bid = int(parts[2])
            except ValueError:
                print("user_id and book_id must be integers.")
                continue
            print(lib.return_book(uid, bid))

        elif action == "8":
            lib.save()

        elif action == "9":
            lib.save()
            print("Bye.")
            break

        else:
            print("Unknown command. Type '10' for help.")

if __name__ == "__main__":
    main()