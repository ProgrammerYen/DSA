class User:
    
    # Creating a constructor object
    def __init__(self, username, first_name, surname, email):
        self.username = username.strip()
        self.first_name = first_name.strip().title()
        self.surname = surname.strip().title()
        self.email = email.strip()
    
    def __repr__(self):
        return f"User(username={self.username}, first_name={self.first_name}, surname={self.surname}, email={self.email})"
    
    def __str__(self):
        """The message that is returned when the User class is printed"""
        return self.__repr__()