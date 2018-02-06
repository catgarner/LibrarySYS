my_file = open("books.txt", "r+")

book_list = {}

def import_books():
    for line in my_file:
        line = line.split(',')
        book_id = line[0]
        title = line[1]
        author = line[2]
        price = line[3]

        book_info = [title,author,price]

        book_list.update({book_id: book_info})

def add_book():
    book_id = input("Please enter the book's unique ID: ")
    title = input("Please enter the title of the book: ")
    author = input("Please enter the author of the book: ")
    price = input("Please enter price of the book: ")

    #this adds a tuple to the dictionary and wont let it work with the discount.
    bookinfo = (title,author,price)
    book_list.update({book_id: bookinfo})

    #book_list[book_id] = [title, author, price]

def find_book():
    name = input("Please enter the title of the book you are looking for: ")

    for key in book_list.keys():
        value = book_list[key]
        if (name == value[0]):
            print("The author of {0} is {1}".format(name,value[1]))
            return
    print("Book title not found!")

def print_books():
    for key, value in book_list.items():
        print("{}, {}, {}, {}".format(key, value[0], value[1], value[2]))

def total_price():
    total = 0
    for key in book_list.keys():
        value = book_list[key]
        total = (total + float(value[2]))

    print("The total price of your shopping cart is €{0:.2f}".format(total))

def discount():
    for key in book_list:
        value = book_list[key]
        value[2] = (float(value[2])/100*(90))

def print_to_file():
    my_file = open("books1.txt", 'w')
    for key, value in book_list.items():
        my_file.write("{}, {}, {}, {:.2f}\n".format(key, value[0], value[1], value[2]))


import_books()
ex = 1
while (ex == 1):
    option = int(input("""\nWould you like to 
    1. Add a new book 
    2. Search for a book by the book title
    3. Print all books in the library
    4. Calculate total price of all books 
    5. Apply a 10% discount to all books
    6. Save the current list of books to a new file
    7. Exit the program
    \nYour option: """))

    if(option == 1):
        add_book()
    elif(option == 2):
        find_book()
    elif(option == 3):
        print_books()
    elif(option == 4):
        total_price()
    elif(option == 5):
        discount()
    elif(option == 6):
        print_to_file()
    elif(option == 7):
        ex = 0
        exec
    else:
        print("Not a valid option, please try again")
