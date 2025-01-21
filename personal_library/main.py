#Samuel Andelin, Personal Library Program

#list containing all books corrresponding to their authors
library = set({})

#list containing corresponding values of books to authors
nums = []

#add book function
def add_book():
    book_name = input("What is the name of the book you want to add?\n-->")
    author = input("What is the name of the author of the book?\n-->")
    library.add((book_name, author))

#remove book function
def remove_book():
    while True:
        print("These are the names of all of the books that you have: ")
        num = 1
        for book in library:
            for item in book:
                print(f"{num}. {book}")
                num += 1
        book_name = input("What is the name of the book you want to remove? (Or type 1 for exit)\n-->")
        for book in library:
            if book_name in book:
                library.remove(book)
                print(f"Removed {book_name}.")
                break
            elif book_name == "1":
                break
            else:
                print("That is not an item in your library!")

#search library function
def search():
    while True:
        type_of_search = input("Type 1 to search by book name, type 2 to search by author, type 3 to exit.\n-->")
        if type_of_search == "1":
            book_search = input("What is the name of the book you want to search for?\n-->")
            num = 0
            searched_books = []
            string_stuff = []
            for book in library:
                for item in book:
                    if book_search.lower() in item:
                        num += 1
                        searched_books.append(book)
            print(f"{num} results for {book_search}:")
            for book in library:
                string_stuff.append(book[1])
                
            string_stuff = "".join(book[0])
            print(string_stuff)
            break
        elif type_of_search == "2":
            author_search = input("What is the name of the author?\n--> ")
            num2 = 0
            searched_authors = []
            for book in library:
                for author in book:
                    if author_search in author:
                        num2 += 1
                        searched_authors.append(author)
            print(f"{num2} results for {author_search}:")
            print("\n".join(searched_authors))
            which_author = input("Type the number that is by the author whose books you want to look at.\n-->")

        elif type_of_search == "3":
            break
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
        elif choice == "3":
            search()
        elif choice == "4":
            print("Ok, bye!")
            break
        else:
            print("Not a valid input!")


main()