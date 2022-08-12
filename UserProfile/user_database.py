from user_details import User

class UserDatabase:
    def __init__(self):
        self.users = []      
    
    def insert(self, user):
        if user.username not in self.users:
            self.users.append(user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
            
        return None
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email      
        
    def list_all(self):
        return self.users


database_users = UserDatabase()
database_users.insert(User("YenDeaPro", "Yenula", "De Alwis", "dealwisyenula@gmail.com"))
database_users.insert(User('DDA', 'Dinal', 'De Alwis', 'dinaldealwis@gmail.com'))