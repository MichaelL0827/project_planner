CreateNewUser = "INSERT INTO user (Username, Firstname, Lastname, Password) VALUES (%s, %s, %s, %s)"
CreateNewTask = "INSERT INTO task (Name, Description, CreatedAt, UserId) VALUES (%s, %s, %s, (SELECT Id FROM user WHERE Username = %s))"
UserAuthentication = "SELECT Password FROM user WHERE Username = %s"