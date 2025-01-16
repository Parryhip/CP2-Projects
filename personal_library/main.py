#Samuel Andelin, Personal Library Program

#list containing all books
books = []

#list containing all authors
authors = {}

#list containing corresponding values of books to authors
nums = []

#add book function
def add_book():
    book_name = input("What is the name of the book you want to add?\n-->")
    author = input("What is the name of the author of the book?\n-->")
    books.append(book_name.lower())
    if author in authors:
        nums.append(authors.index(author))
    authors.add(author)

#remove book function
def remove_book():
    while True:
        print("These are the names of all of the books that you have: ")
        num = 1
        for book in books:
            print(f"{num}. {book}")
            num += 1
        book_name = input("What is the name of the book you want to remove? (Or type 1 for exit)\n-->")
        if book_name in books:
            books.remove(book_name.lower())
            print(f"Removed {book_name}.")
            break
        elif book_name == "1":
            break
        else:
            print("That is not an item in your library!")

#search library function
def search():
    while True:
        type_of_search = input("Type 1 to search by book name, type 2 to search by author.\n-->")
        if type_of_search == "1":
            book_search = input("What is the name of the book you want to search for?\n-->")
            num = 0
            searched_books = []
            for book in books:
                if book_search.lower() in book:
                    num += 1
                    searched_books.append(book)
            print(f"{num} results for {book_search}:")
            print("\n".join(searched_books))
            break
        elif type_of_search == "2":
            author_search = input("What is the name of the author?\n--> ")
            num2 = 0
            searched_authors = []
            for author in authors:
                if author_search in author:
                    num2 += 1
                    searched_authors.append(author)
            print(f"{num2} results for {author_search}:")
            print("\n".join(searched_authors))
            which_author = input("Type the number that is by the author whose books you want to look at.\n-->")
            
#User Interface function
def main():
    print("Welcome to the Online Personal Libary for Books!")
    while True:
        print("What do you want to do?")
        #asks user for what they want to do
        choice = input("Type 1 to add a book to the library,\nType 2 to remove a book from the library\nType 3 to search for a book,\n And type 4 to exit.\n-->")
        #if the user wants to add a book
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()

main()