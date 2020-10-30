def signup(users):
    new_username = str(input("Enter your new username: "))
    new_password = str(input("Enter your new password: "))
    users[new_username] = new_password
    return users

def login(users, username, password):
    if username in users and password == users[username]:
        return True
    return False

if __name__ == "__main__":
    users = {}
    signup(users)
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    print(login(users,username,password))
