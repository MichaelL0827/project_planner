CreateNewUser = "INSERT INTO user (Username, Firstname, Lastname, Password) VALUES (%s, %s, %s, %s)"
CreateNewTask = "INSERT INTO task (Name, Description, CreatedAt, UserId) VALUES (%s, %s, %s, (SELECT Id FROM user WHERE Username = %s))"
CreateNewTodo = "INSERT INTO todo (Name, Description, Completed, Start, End, TaskId) VALUES (%s, %s, %s, %s, %s, %s)"

UserAuthentication = "SELECT Password FROM user WHERE Username = %s"

GetTasks = "SELECT Name, Description, CreatedAt FROM task WHERE UserId = (SELECT Id FROM user WHERE Username = %s)"

GetTasksTodos = """
SELECT task.Name AS Tasks,
JSON_ARRAYAGG(JSON_OBJECT('todo_name',todo.Name,'todo_description', todo.Description, 'todo_completed',todo.Completed)) AS Todos
FROM task 
INNER JOIN todo 
ON task.Id = todo.TaskId 
WHERE task.UserId = (SELECT Id FROM user WHERE Username = %s) 
GROUP BY task.Id"""
"""
SELECT task.Name AS Tasks,
GROUP_CONCAT(JSON_OBJECT('Name',todo.Name,'Description', todo.Description)) AS Todos
FROM task 
INNER JOIN todo 
ON task.Id = todo.TaskId 
WHERE task.UserId = (SELECT Id FROM user WHERE Username = 'jane_smith') 
GROUP BY task.Id;"""