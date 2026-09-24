#create empty list for users and animals - []
#create a variable called zoo to store the zoo information
#check if username is only letters and passwords have both letters and numbers - isalpha
#if no user exists, then create admin account - create_admin_user()
#admins can add new users, view all users or delete users
#Admin can create a zoo
#anyone can view the animals but only admin can add animals
#main menu is where you pick between manageing the zoo, managing users or exiting.
#you pick a number 1,2 or 3 and then get more options depending
#this repeats unless you picked 3 exit
#if a user trys to do something only an admin can do it wont let them.
#Lecture notes, GeeksforGeek - python string isalpha()

users = []
zoo = None
animals = []

def valid_username(username):
    return username.isalpha()

def valid_password(password):
    return any(c.isalpha() for c in password) and any(c.isdigit() for c in password)

def find_user(username):
    for user in users:
        if user["username"] == username:
            return user
    return None

def create_admin_user():
    print('Create admin')
    while True:
        username = input('Enter username ')
        if not valid_username(username):
            print("Not a valid username")
            continue
        if find_user(username):
            print("Username has been taken")
            continue
        break
    while True:
        password = input('Enter admin password ')
        if not valid_password(password):
            print("Password not valid")
            continue
        break
    users.append({"username": username, "password": password, "role": "admin"})
    print(f"Admin '{username}' has been created.")

def authenticate():
    username = input('Username ')
    password = input('Password ')
    user = find_user(username)
    if user and user["password"] == password:
        print("Authentication successful")
        return user
    else:
        print("Authentication failed")
        return None

def add_user():
    print("Add a new user")
    while True:
        username = input("Username ")
        if not valid_username(username):
            print("Not a valid username")
            continue
        if find_user(username):
            print("Username has been taken")
            continue
        break
    while True:
        password = input("Password ")
        if not valid_password(password):
            print("Not a valid password")
            continue
        break
    while True:
        role = input("Role ('admin' or 'user') ").lower()
        if role not in ("admin", "user"):
            print("Role must be 'admin' or 'user'")
            continue
        break
    users.append({"username": username, "password": password, "role": role})
    print(f"User '{username}' ({role}) created")

def view_users():
    if not users:
        print("No users found")
    else:
        print("Current users")
        for user in users:
            print(f"- {user['username']} ({user['role']})")

def delete_user():
    username = input("who do you want to delete?")
    user = find_user(username)
    if user:
        users.remove(user)
    else:
        print("User not found")

def create_zoo(current_user):
    zoo_name = input("Name of Zoo ")
    zoo_info = {"name": zoo_name, "created_by": current_user["username"]}
    print(f"Zoo '{zoo_name}' created.")

def add_animal():
    name = input("Name of the Animal")
    tag = input("Animal tag ")
    animals.append({"name": name, "tag": tag})
    print(f"Animal '{name}' with tag '{tag}' added.")

def view_animals():
    if not animals:
        print("No animals in the zoo")
    else:
        print("Current animals in the zoo")
        for animal in animals:
            print(f"- {animal['name']} (tag: {animal['tag']})")

def main_menu():
    if not users:
        print("No users found, create an admin user.")
        create_admin_user()

    while True:
        print('\nMain Menu')
        print('1. Manage zoo')
        print('2. Manage user account')
        print('3. Exit')
        choice = input('Enter choice ')
        if choice == '1':
            user = authenticate()
            if user:
                if not zoo:
                    if user["role"] == "admin":
                        create_zoo(user)
                    else:
                        print("Only admin can create a zoo.")
                else:
                    print(f"Zoo: {zoo['name']}")
                    if user["role"] == "admin":
                        print("1. Add animal")
                        print("2. View animals")
                        print("3. Return")
                        
                        sub_choice = input("Choose an option ")
                        if sub_choice == "1":
                            add_animal()
                        elif sub_choice == "2":
                            view_animals()
                        elif sub_choice == "3":
                            continue
                        else:
                            print("Invalid choice.")
                    else:
                        print("1. View animals")
                        print("2. Return")
                        sub_choice = input("Choose an option ")
                        if sub_choice == "1":
                            view_animals()
                        elif sub_choice == "2":
                            continue
                        else:
                            print("Invalid choice.")
                            
        elif choice == "2":
            user = authenticate()
            if user and user["role"] == "admin":
                print("1. Add user")
                print("2. View users")
                print("3. Delete user")
                print("4. Return")
                
                sub_choice = input("Choose an option ")
                if sub_choice == "1":
                    add_user()
                elif sub_choice == "2":
                    view_users()
                elif sub_choice == "3":
                    delete_user()
                elif sub_choice == "4":
                    continue
                else:
                    print("Invalid choice.")
            else:
                print("Only admin can manage users.")
                
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

main_menu()
