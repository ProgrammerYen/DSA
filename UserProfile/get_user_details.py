import re
from user_database import database_users

print(database_users.list_all())

def get_user_details():
    global user_database
    
    while True:
        username = input("Please enter the username you wish to have: ")
        
        find_user = database_users.find(username)

        if find_user == None:
            print("\nYour good to go!\n")
            break
   
        print("\nSorry, but that username is already taken.\n")
    
    names = []
    def get_name(word):
        while True:    
            name = input(f"Please enter your {word} name: ")
            names.append(name)
            
            number_in_name = False
            for i in range(10):
                if str(i) in name:
                    number_in_name = True
                    print(f"\nPlease enter a valid {word} name (which does not contain a number).\n")
                    break
                
            if number_in_name == False:
                break
            
        print()
    
    get_name("first")
    get_name("last")
    
    email_regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    
    while True:
        email = input("Please enter your email: ").strip()
        if re.fullmatch(email_regex, email):
            print("\nDetails are valid.\nAdded to user database.")
            break
            
        else:
            print("\nPlease enter a valid email.\n")
      
      
    with open("user_database.py", "a") as database_file:
        database_file.write("\ndatabase_users.insert(User('{}', '{}', '{}', '{}'))".format(username, names[0], names[1], email))
        database_file.close()
    
get_user_details()