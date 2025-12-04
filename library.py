# ...existing code...
import os

if not os.path.exists("users.txt"):
    with open("users.txt", "w") as f:
        pass

if not os.path.exists("books.txt"):
    with open("books.txt", "w") as f:
        pass

def load_users():
    user_dict = {}
    try:
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    username, password = line.split(",")
                    user_dict[username] = password
    except FileNotFoundError:
       print(" File not found!")
    return user_dict

def load_books():
    books_list = []
    try:
        with open("books.txt", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                   book_id,title,author,quantity = line.split()
                   books = {
                         'id': book_id,
                         'author': author,
                            'title': title,
                            'quantity': int(quantity)
                     }
                   books_list.append(books)
    except FileNotFoundError:
         print(" File not found!")
    return books_list  
def get_exisiitng_books_id(books_list):
    book_ids = set()
    for books in books_list:
       book_ids.add(books['id'])
    return book_ids
def register_user(user_dict):
    print("\n--- User Registration ---")
    username = input("Enter a username: ").strip()
    password = input("Enter a password: ").strip()
    if username in user_dict:
        print("Username already exists. Please choose a different username.")
        return False
    if not username or not password:
        print("Username and password cannot be empty.")
        return False
    user_dict[username] = password
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("User registered successfully!")
    return True
users_dict = load_users()
register_user(users_dict)

def login_user(user_dict):
    print("\n--- User Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in user_dict and user_dict[username] == password:
        print(f"Welcome! {username.capitalize()}")
        return username
    else:
        print("Invalid username or password.")
        return None
login_user(users_dict)
def main_menu():
    print("="*55)
    print(" Library Management System ")
    print(" 1. Add Books")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
main_menu() #call the function    

def add_book(books_list,book_ids):
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ").strip()
    if book_id in book_ids:
        print("Book ID already exists.")
        return 
    title = input("Enter Book Title: ").strip()
    author = input("Enter Book Author: ").strip()
    try:
        quantity = int(input("Enter Quantity: ").strip())
    except ValueError:
        print("Quantity must be an integer.")
        return

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'quantity': quantity
    }

    books_list.append(new_book)
    book_ids.add(book_id)

    with open("books.txt", "a") as f:
        f.write(f"{book_id} {title} {author} {quantity}\n")
    print("Book added successfully!")    
books_list = load_books()
book_ids = get_exisiitng_books_id(books_list)
# print(books_list)
add_book(books_list,book_ids)



###FUNCTION TO VIEW ALL THE BOOKS
def view_books(books_list):
    '''Display all the books in the library'''
    print("\n--- Available Books ---")
    if not books_list:
        print("No books available in the library.")
        return
    for book in books_list:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
view_books(books_list)
   