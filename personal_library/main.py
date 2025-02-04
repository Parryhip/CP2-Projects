#Samuel Andelin, Personal Library Program

#list containing all books corrresponding to their authors
library = []

#list containing corresponding values of books to authors
nums = []

#add book function
def add_book():
    book_name = input("What is the name of the book you want to add?\n-->")
    author = input("What is the name of the author of the book?\n-->")
    while True:
        pages = input("How many pages are in this book?\n-->")
        try:
            test = int(pages)
            break
        except:
            print("Not a valid number of pages!")
    genre = input("What genre is this book?\n-->")
    library.append({"name" : book_name,  
                    "author" : author,
                    "pages" : pages,
                    "genre" : genre,
                    })

#remove book function
def remove_book():
    while True:
        print("These are the names of all of the books that you have: ")
        num = 1
        for book in library:
            print(f"{num}.'{book["name"]}' by the author '{book["author"]}'")
            num += 1
        book_name = input("What is the name of the book you want to remove? (Or type 1 for exit)\n-->")
        for book in library:
            if book_name in book["name"]:
                library.remove(book)
                print(f"Removed {book_name}.")
                return
            elif book_name == "1":
                return
            else:
                pass
        print("Not a valid book name!")
        

#search library function
def search():
    while True:
        type_of_search = input("Type 1 to search by book name, type 2 to search by author, type 3 to exit.\n-->")
        if type_of_search == "1":
            book_search = input("What is the name of the book you want to search for?\n-->")
            num = 0
            searched_books = []
            for book in library:
                for item in book:
                    if book_search in item[0]:
                        num += 1
                        searched_books.append(book)
            print(f"{num} results for {book_search}:")
            num2 = 1
            for i in searched_books:
                print(f"{num2}.'{i[0]}' by the author '{i[1]}'")
                num2 += 1
            
        elif type_of_search == "2":
            author_search = input("What is the name of the author?\n--> ")
            num3 = 0
            searched_authors = []
            for book in library:
                if author_search in book[1]:
                    num3 += 1
                    searched_authors.append(book[1])
            print(f"{num3} results for {author_search}:")
            if num3 == 0:
                return
            num3 = 1
            for item in searched_authors:
                print(f"{num3}.{item}")
                num3 += 1
            while True:
                which_author = input("Type the number that is by the author whose books you want to look at.\n-->")
                try:
                    test = int(which_author)
                    test2 = searched_authors[int(which_author)-1]
                    break
                except:
                    print("Not a valid input!")
            bookstoprint = []
            
            for book in library:
                if searched_authors[int(which_author)-1] == book[1]:
                    bookstoprint.append(book[0])
            print(f"Here are the books made by the author {searched_authors[int(which_author)-1]}")
            num4 = 1
            for book in bookstoprint:
                print(f"{num4}.{book}")
                num4 += 1
        elif type_of_search == "3":
            break

#view library function
def view():
    print("Here is your library: ")
    num = 1
    for book in library:
        print(f"{num}. \nname: {book["name"]}\nauthor: {book["author"]}\npages: {book["pages"]}\ngenre: {book["genre"]}")
        num += 1       
        
#User Interface function
def main():
    print("Welcome to the Online Personal Libary for Books!")
    while True:
        print("What do you want to do?")
        #asks user for what they want to do
        choice = input("Type 1 to add a book to the library,\nType 2 to remove a book from the library\nType 3 to search for a book,\nType 4 to view your whole library,\nAnd type 5 to exit.\n-->")
        #if the user wants to add a book
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search()
        elif choice == "4":
            view()
        elif choice == "5":
            print("Ok, bye!")
            break
        else:
            print("Not a valid input!")


main()
