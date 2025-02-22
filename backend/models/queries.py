CreateNewUser = "INSERT INTO user (Username, Firstname, Lastname, Password) VALUES (%s, %s, %s, %s)"
CreateNewTask = "INSERT INTO task (Name, Description, CreatedAt, UserId) VALUES (%s, %s, %s, (SELECT Id FROM user WHERE Username = %s))"
CreateNewTodo = "INSERT INTO todo (Name, Description, Completed, Start, End, TaskId) VALUES (%s, %s, %s, %s, %s, %s)"

UserAuthentication = "SELECT Password FROM user WHERE Username = %s"

GetTasks = "SELECT Name, Description, CreatedAt FROM task WHERE UserId = (SELECT Id FROM user WHERE Username = %s)"