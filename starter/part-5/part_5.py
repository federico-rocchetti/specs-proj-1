### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

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

    with open("library.txt", "a") as f:
        f.write(f"{title}, {author}, {year}, {rating}, {pages}\n")

# add_book("Book 2", "Author 2", "2009", "4.69", "694")
### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here



### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def main_menu():
    user_continue = True
    while user_continue == True:
        user_input = input("What would you like to do? 1- Add new book, 2- See all books, 3- Total pages or 0- Exit - ")
        if user_input == "1":
            create_new_book()
        elif user_input == "2":
            print(all_books())
        elif user_input == "3":
            print(total_pages())
        elif user_input == "0":
            print("See you later!")
            user_continue = False
        else:
            print("Sorry, that option is not available. Please type one of the following: Add new book, See all books or Exit")

def all_books():
    book_list = []

    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            book_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
             
    return(book_list)

def print_book(book):
        print(f"{book['title']}, by {book['author']}.")

def total_pages():
    page_total = 0
    with open("library.txt", "r") as f:
        file = f.readlines()

        for line in file:
            title, author, year, rating, pages = line.split(", ")

            page_total += int(pages)
    
    return page_total

if __name__ == '__main__':
    main_menu()