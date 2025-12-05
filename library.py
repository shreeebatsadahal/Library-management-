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
# users_dict = load_users()
# register_user(users_dict)

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
# login_user(users_dict)
def main_menu():
    print("="*55)
    print(" Library Management System ")
    print(" 1. Add Books")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")
# main_menu() #call the function    

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
# book_ids = get_exisiitng_books_id(books_list)
# print(books_list)
# add_book(books_list,book_ids)



###FUNCTION TO VIEW ALL THE BOOKS
def view_books(books_list):
    '''Display all the books in the library'''
    print("\n--- Available Books ---")
    if not books_list:
        print("No books available in the library.")
        return
    for book in books_list:
        print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
# view_books(books_list)


###search a book using title or author
def search_books(books_list):
    found_items = []
    ''''Search for books by title or author'''
    search_term= input("Enter book title or author to search: ").strip().lower()
    for book in books_list:
        if search_term in book['title'] or search_term in book['author']:
            found_items.append(book)
    if found_items:
        print("\n--- Search Results ---")
        for book in found_items:
            if search_term in book['title'] or search_term in book['author']:
                found_items.append(book)
        if found_items:
            print(f"Found {len(found_items)}books:") 
            view_books(found_items)
        else:
            print("No books found matching the search criteria.")           
                
# search_books(books_list)


#save books to the file
'''Write all books back to books.txt'''
def save_books(books_list):
    with open("books.txt", "w") as f:
        for book in books_list:
            f.write(f"{book['id']} {book['title']} {book['author']} {book['quantity']}\n")
###issue book function
def issue_book(books_list):
    print("\n--- Issue Book ---")
    book_id = input("Enter Book ID to issue: ").strip()
    for book in books_list:
        if book['id'] == book_id:
            if book['quantity'] > 0:
                book['quantity'] -= 1
                save_books(books_list)
                print(f"Book '{book['title']}' issued successfully!")
                return
            else:
                print("Sorry, this book is currently out of stock.")
                return
    print("Book ID not found.")
def return_book(books_list):
    '''Return a book to the library''' 
    book_id = input("Enter Book ID to return: ").strip()
    for book in books_list:
        if book['id'] == book_id:
            book['quantity'] += 1
            save_books(books_list)
            print(f"Book '{book['title']}' returned successfully!")
            print(f"CURRRENT QUANTITY IS {book['quantity']}")
            return
    print("Book ID not found.")
# issue_book(books_list)
# add_book(books_list,get_exisiitng_books_id(books_list))
# return_book(books_list)


 ###MAIN FUNCTION TO RUN THE LIBRARY MANAGEMENT SYSTEM

def main():
    '''Main program loop'''
    users_dict = load_users()
    print("="*50)
    print(" Welcome to the Library Management System ")
    print("="*50)
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            register_user(users_dict)
        elif choice == '2':
            username = login_user(users_dict)
            if username:
                books_list = load_books()
                book_ids = get_exisiitng_books_id(books_list)
                while True:
                    main_menu()
                    user_choice = input("Enter your choice: ").strip()
                    if user_choice == '1':
                        add_book(books_list, book_ids)
                    elif user_choice == '2':
                        view_books(books_list)
                    elif user_choice == '3':
                        search_books(books_list)
                    elif user_choice == '4':
                        issue_book(books_list)
                    elif user_choice == '5':
                        return_book(books_list)
                    elif user_choice == '6':
                        print("Exiting the system. Goodbye!")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()            