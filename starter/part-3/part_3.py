my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

my_books = [{
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
},
{
    "title": "Then Hunger Games 2",
    "author": "Suzanne Collins 2",
    "year": 2008,
    "rating": 4.32,
    "pages": 174
}]

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def book_parser(book):
    title = book['title']
    author = book['author']
    year = book['year']
    rating = book['rating']
    pages = book['pages']
    book_string = f"The book title is {title}, written by {author}, published in {year}, contains {pages} pages and has a rating of {rating}."
    return book_string

# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def book_title(book):
    title = book['title']
    return f"The title of the book is {title}."

def book_author(book):
    author = book['author']
    return f"The author of the book is {author}."

def book_year(book):
    year = book['year']
    return f"The book was published in {year}."

def book_rating(book):
    rating = book['rating']
    return f"The book has a rating of {rating}."

def book_pages(book):
    pages = book['pages']
    return f"The book has {pages} pages."

# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def all_books(books):
    for book in books:
        print(f"{book['title']}, by {book['author']}.")

def shortest_book(books):
    shortest_book = ""
    page_num = 10000
    for book in books:
        if book['pages'] < page_num:
            page_num = book['pages']
            shortest_book = book['title']
        else:
            pass
    return f"The shortest book available is {shortest_book} with {page_num} pages."

def longest_book(books):
    longest_book = ""
    page_num = 0
    for book in books:
        if book['pages'] > page_num:
            page_num = book['pages']
            longest_book = book['title']
        else:
            pass
    return f"The longest book available is {longest_book} with {page_num} pages."


print(longest_book(my_books))