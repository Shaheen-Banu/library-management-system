FILE_NAME = "students.txt"

def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    id = input("Enter Student ID: ")
    name = input("Enter Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{id},{name}\n")

    print(" Student added successfully!")

def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No records found.")
                return

            print("\n--- Student Records ---")
            for line in data:
                id, name = line.strip().split(",")
                print(f"ID: {id}, Name: {name}")

    except FileNotFoundError:
        print("No data file found.")

def search_student():
    search_id = input("Enter Student ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            found = False

            for line in file:
                id, name = line.strip().split(",")

                if id == search_id:
                    print("\n Student Found:")
                    print(f"ID: {id}, Name: {name}")
                    found = True
                    break

            if not found:
                print(" Student not found.")

    except FileNotFoundError:
        print("No data file found.")

def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(FILE_NAME, "w") as file:
            found = False

            for line in lines:
                id, name = line.strip().split(",")

                if id != delete_id:
                    file.write(line)
                else:
                    found = True

        if found:
            print(" Student deleted successfully!")
        else:
            print(" Student not found.")

    except FileNotFoundError:
        print("No data file found.")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
