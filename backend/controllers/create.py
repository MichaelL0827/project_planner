from utils.helper import QueryResult, MakeConnection

def UsernameExist(Username):
    ConnectionString = MakeConnection()
    Usernames = QueryResult(ConnectionString, 'SELECT Username FROM User', 'readall', None)
    Users = []
    for user in Usernames:
        Users.append(user['Username'])
    if(Username in Users):
        return False
    else: 
        return True
