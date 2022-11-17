### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
user_library = [{
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "The Fellowship of the Ring",
    "author": "J R R Tolkien",
    "year": 1954,
    "rating": 4.98,
    "pages": 423
}]

# def create_new_book():
#     title = input("What is the title of the book you'd like to add? - ")
#     author = input("Who is the author of the book you'd like to add? - ")
#     year = input("In what year was the book published? - ")
#     rating = input("What rating from 0 to 5, 5 being best, would you give this book? - ")
#     rating = input("Please use numbers, can include decimals, from 0 to 5 to rate this book. - ")
#     pages = input("How many pages long is this book? - ")
#     pages = input("Please type in numbers how many pages long this book is. - ")

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary
### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():
#     title = input("What is the title of the book you'd like to add? - ")
#     author = input("Who is the author of the book you'd like to add? - ")
#     year = int(input("In what year was the book published? - "))
#     rating = float(input("What rating from 0 to 5, 5 being best, would you give this book? - "))
#     pages = int(input("How many pages long is this book? - "))

#     book_dictionary = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_dictionary


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book():
    title = input("What is the title of the book you'd like to add? - ")
    author = input("Who is the author of the book you'd like to add? - ")
    try:
        year = int(input("In what year was the book published? - "))
    except:
        year = int(input("Please type in numbers the year in which the book was published. - "))
    try:
        rating = float(input("What rating from 0 to 5, 5 being best, would you give this book? - "))
    except:
        rating = float(input("Please use numbers, can include decimals, from 0 to 5 to rate this book. - "))
    try:
        pages = int(input("How many pages long is this book? - "))
    except:
        pages = int(input("Please type in numbers how many pages long this book is. - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_dictionary


### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def all_books(books):
    for book in books:
        print(f"{book['title']}, by {book['author']}.")

# def main_menu():
#     user_input = input("What would you like to do?")

#     if user_input == "Add new book":
#         new_book = create_new_book()
#         user_library.append(new_book)
#         print(user_library)
#         return user_library
#     elif user_input == "See all books":
#         all_books(user_library)
#     else:
#         print("Sorry, that option is not available. Please type one of the following: Add new book, See all books")


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu():
    user_continue = True
    while user_continue == True:
        user_input = input("What would you like to do? Add new book, See all books or Exit - ")
        if user_input == "Add new book":
            new_book = create_new_book()
            user_library.append(new_book)
            print(user_library)
            return user_library
        elif user_input == "See all books":
            all_books(user_library)
        elif user_input == "Exit":
            user_continue = False
        else:
            print("Sorry, that option is not available. Please type one of the following: Add new book, See all books or Exit")

main_menu()