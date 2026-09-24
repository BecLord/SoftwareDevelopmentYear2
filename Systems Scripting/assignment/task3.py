#create and animal zoo
# one argument representing the name of a file to host the database
#Menu to manage zoo creation, user accounts & exiting the program.
# 1 - zoo creation menu if no account, create an admin
# 2. if account, username and password (authentcation)
# 3. setup zoo name (Admin only)
# 4. zoo created, 2 sub menus 'admin' 'view settings'
# 5. manage zoo 2 menu options 'update' 'delete' (Admin Only)

# Admin user account
# authenticate user, then 'add users', 'view users', 'delete users' 'return'
# when selected 'standard' 'admin user' accounts
# account has username and password 
# username is only characters
#password must have characters and numbers
# no encrptoin but validate the inputs
# ONLY Admin and mangage user accounts

# View users menu, show 'existing users' and 'return back to menu' option
# delte users menu, 'username delete', if on system delete then back to menu
# return menu 'return back to menu'
# exit menu 'at end of program'

#'Admin zoo', 4 menus 'add animal', 'querey', 'delete animal', exit' 
# user zoo, 2 menus 'query', 'exit'

# animal menu 'input animal name and tag number'
# animal name - characters
# tag number - characters and numbers
# validae and return to sub menu

# query menu - user enter the animal tag and print search resutl.
# subsequent searches until 'finish is entered' return to sub menu

#delete menu - return to sub menu

#sub menu - 'view settings' retunr to menu options

#Menu
#ZOO Creation
    #if no user - create an admin
        #else - admin authentication username and password 
    #setup Zoo Name (ADMIN ONLY)
        #'Admin zoo'
            #'update zoo'
            #'delete zoo'
            #'add animal'
                #'name' (characters only)
                #'tag' (characters and numbers)
            #'delete animal'
            #'query'
                #'enter animal tag' -then inform user of result
            #'delete animal'
                 #'enter animal tag' -then remove animal
            #'exit'
                #'return'
        #'view settings'
            #'return'
#USER ACCOUNTS
    #ADMIN
        #'add users'
            #'standard user account'
                #'username' (characters only)
                #'password' (numbres & characters)
            #'admin user account'
                #'username'
                #'password'
        #'view users'
            #'list of existing users'
            #'return'
        #'delete users'
            #'resquest username to be deleted'
            #'return'
        #'return'
            #'return'
    #USER
        #'query'
        #'exit'
#EXIT PROGRAM
    #'end the program'

users = []
animals = []
zoo_name = ""

filename = input("Please enter the name of your zoo database: ")

def save_data(filename, users): #open file to save data to
    with open(filename, "w") as file:
        file.write("Zoo name " + zoo_name + "\n") #add the zoo name to the file
        for user in users:
            file.write("Username: " + user[0] + " Password: " + user[1] + "Role: " + user[2] + "\n") #add username, password, rolse(admin or not)
        for animal in animals:
            file.write("Tag: " + animal[0] + " Name: " + animal[1] + "\n") #add annimal with tag and name

def user_accounts(users): #menu for admin managment
    while True:
        print("Admin Managemnet")
        print("1. Add User")
        print("2. View Users")
        print("3. Delete User")
        print("4. Return")
        option = input("What would you like to do? ")

        if option == "1":
            print("Add User")
            username = input("Username: ")
            user_password = input("Password: ")
            role = input("Enter role - Admin or User: ")

            if username_check(username) and password_check(user_password): #check that username is only characters and password has a number
                users.append([username, user_password, role]) #add new user to file
                print(username + "User added")
            else:
                print("Error")

        elif option == "2":
            print("Existing Users") #list out users and if they are admin or not
            for user in users:
                print(f"Username: {user[0]}, Role {user[2]}")
                
        elif option == "3":
            delete_user = input("Enter username to delete: ")
            found = False
            for user in users:
                if user[0] == delete_user:
                    users.remove(user) #remove user from file
                    print(delete_user + "User deleted")
                    found = True
                    break
            if found:
                print("User " + delete_user + "has been deleted")
            else:
                print("Username not found")
 
        elif option == "4":
            print("Exiting")
            break
                
def user_page(animals): #menu for user querys
    while True:
        print("User Page")
        print("1. Query")
        print("2. Exit")
        option = input("Select an option: ")

        if option == "1":
            print("Please enter the tag of the animal you want to query")
            animal_tag = input("Tag: ")
            found = False
            for animal in animals: #look for the animal by its tag
                if animal[0] == animal_tag:
                    print("Animal: ", animal[1])
                    found = True
                if not found:
                    print("Animal not found")

        elif option == "2":
            print("Exiting")
            break

def username_check(name):
    return name.isalpha() #check for characters only

def password_check(password):
    return any(c.isalpha() for c in password) and any(c.isdigit() for c in password) #check for charcater and digit

def tag_check(tag):
    return any(c.isalpha() for c in tag) and any(c.isdigit() for c in tag) #check for character and digit

def menu():
    #create admin if there is no users
    if not users:
        print("Create Admin: ")
        while True:
            username = input("Username: ")
            user_password = input("Password: ")
            if username_check(username) and password_check(user_password): #check password and username
                users.append([username, user_password, "admin"])
                break
            else:
                print("Please try again")

#Menu
menu() #check if user is empty

#start menu
while True:
    print("MENU")
    print("1. Zoo Creation")
    print("2. User Accounts")
    print("3. Exit Program")
    choice = input("Choice: ")

    #Zoo Creating menu
    if choice == "1": 
        while True:
            print("1. Update Zoo")
            print("2. Delete Zoo")
            print("3. Add Animal")
            print("4. Delete Animal")
            print("5. Query")
            print("6. Retrun")
            option = input("What would you like to view? ")

            if option == "1": #update zoo name
                zoo_name = input("Update the zoo name to: ")
                print("Zoo renamed to " + zoo_name)

            elif option == "2": #delete zoo
                zoo_name = ""
                animals.clear()
                print("Zoo has been deleted")

            elif option == "3": #add new animal
                print("Please enter Animal's name and tag, to add them to the zoo")
                animal_name = input("Name: ")
                animal_tag = input("Tag: ")

                if animal_name.isalpha() and tag_check(animal_tag):
                    animals.append([animal_tag, animal_name])
                    print("Animal " + animal_name + " with tag " + animal_tag + " has been added")
                else:
                    print("Error must have characters and numbers.")

            elif option == "4": #remove animal
                print("Please enter the tag of the animal you want to delete")
                animal_tag = input("Tag: ")
                new_animals = []

                for animal in animals:
                    if animal[0] != animal_tag:
                        new_animals.append(animal)

                if len(new_animals) < len(animals):
                    animals = new_animals 
                    print("Animal tag " + animal_tag + " is deleted" )
                else:
                    print("No animal found")

            elif option == "5": #query animal
                print("Please enter the tag of the animal you want to query")
                animal_tag = input("Tag: ")
                found = False

                for animal in animals:
                    if animal[0] == animal_tag:
                        print("Animal: ", animal[1])
                        found = True

                if not found:
                    print("Animal not found")

            elif option == "6":
                print("Exiting")
                break
    
    #User accounts
    elif choice == "2":
        username_input = input("Username")
        user_password_input = input("Password: ")
        found_user = None

        for user in users:
            if user[0] == username_input and user[1] == user_password_input:
                found_user = user
            
        if found_user and found_user[2] == "admin":
            print("Logged in as admin")
            user_accounts(users) #admin go to manage users
        elif found_user:
            print("logged in as user")
            user_page(animals) #users go to query
        else:
            print("Error")        

    #Exit Program
    elif choice == "3":
        save_data(filename, users)
        print("Exiting")
        break

#I started by laying out how i wanted the menu to look.
#I then created the 3 lists to store the data (users, animals and zoo name)
#to create the filename i asked the user to enter the name of the database.
#I created the main menu which gives the user 3 options (create zoo, user accounts and exit program)
#then i added in what the user would go to when they pick each option.
#I added in option 1 to update the zoo name, option 2 to delete the zoo and option 6 to exit. I just put comments in option 3-5 to start with.
#I then filled in the exit option and created te menu function to create an admin account at the start if no users existed already.
#After that I created the user_accounts function for users to query animals by tags.
#In the main option for choice 2 (user accounts) I asked the user for username and password. 
#then i checked the list to see if they were an admin or not
#I then filled in the animal options int he zoo creation menu, options 3,4 and 5 where you can add animals, delete animals and query the animals by their tag.
#the query lets the users enter a animal tag then search the list and print the name of the animal if its there.
#I then realised i had to check if the usersname only had letters so i added in the username_check.
#and the same to check the password and tag had letters and numbers (password_check and tag_check)
#i went over my code and added called these functions where needed.
#I then created the save_data functin to write the zoo name, users and animals into a file.

#References
#BroCode - Python Full Course (Youtube)
#GeeksforGeeks - list.append(), list.remove() (python lists)
#GeeksforGeeks - python file handling
#GeeksforGeeks - python File Write
#GeeksforGeeks - python string isalpha, isdigit
#pythonguides - file handling in python