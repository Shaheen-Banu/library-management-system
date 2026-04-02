FILE_NAME = "books.txt"

def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id},{book_name},Available\n")

    print(" Book added successfully!")

def view_books():
    print("DEBUG: view_books called")   

    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
            print("DEBUG DATA:", data)  

            if not data:
                print("No books found.")
                return

            print("\n--- Book Records ---")
            for line in data:
                book_id, book_name, status = line.strip().split(",")
                print(f"ID: {book_id}, Name: {book_name}, Status: {status}")

    except FileNotFoundError:
        print("No data file found.")

def search_book():
    search_id = input("Enter Book ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                book_id, book_name, status = line.strip().split(",")

                if book_id == search_id:
                    print("\n Book Found:")
                    print(f"ID: {book_id}, Name: {book_name}, Status: {status}")
                    found = True
                    break

            if not found:
                print(" Book not found.")

    except FileNotFoundError:
        print("No data file found.")

def issue_book():
    issue_id = input("Enter Book ID to issue: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            found = False

            for line in lines:
                book_id, book_name, status = line.strip().split(",")

                if book_id == issue_id:
                    if status == "Available":
                        file.write(f"{book_id},{book_name},Issued\n")
                        print(" Book issued successfully!")
                    else:
                        file.write(line)
                        print(" Book already issued!")
                    found = True
                else:
                    file.write(line)

        if not found:
            print(" Book not found.")

    except FileNotFoundError:
        print("No data file found.")

def return_book():
    return_id = input("Enter Book ID to return: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            found = False

            for line in lines:
                book_id, book_name, status = line.strip().split(",")

                if book_id == return_id:
                    if status == "Issued":
                        file.write(f"{book_id},{book_name},Available\n")
                        print(" Book returned successfully!")
                    else:
                        file.write(line)
                        print(" Book was not issued!")
                    found = True
                else:
                    file.write(line)

        if not found:
            print(" Book not found.")

    except FileNotFoundError:
        print("No data file found.")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
