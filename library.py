import os

if not os.path.exists("users.txt"): # checking if file exist
    with open("users.txt", "w") as f: # creating file
        pass

if not os.path.exists("books.txt"): # checking if file exist
    with open("books.txt", "w") as f: # creating file
        pass

###load data from the file
def load_users():
    """load all the users from users.txt into a dictionary"""

    user_dict = {}

    try:
        with open("users.txt", "r") as f:
            for line in f:
                line = line.strip() # remove any leading/trailing whitespace
                if line:
                    username, password = line.split(",") # split by comma
                    user_dict[username] = password

    except FileNotFoundError:
       print(" File not found!")

    return user_dict
 #book_id,title,author,quantity
  
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
    '''create a set to store all the ids of the books'''  
    book_ids = set()
    for books in books_list:
        #dictionary
       book_ids.add(books['id'])  
       return book_ids
#user reg(
def register_user(user_dict):
    '''register a new user''' 
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
    #save the register user to the file 'users.txt
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("User registered successfully!")
    return True
users_dict = load_users()
register_user(users_dict)

#OPTIONAL NO NEED TO DISPLAY ALL USERS TO CUSTOMERS
user_dict = load_users() #load users from file
print(user_dict)


def login_user(user_dict):
    '''login an existing user'''
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

                 