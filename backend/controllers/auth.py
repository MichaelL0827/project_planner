from utils.helper import HashPassword

def CheckPassword(Password, UserInput):
    if((Password == HashPassword(UserInput)) or (Password == UserInput)):
        return True
    else: 
        return False
