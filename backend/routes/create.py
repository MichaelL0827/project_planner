from fastapi import APIRouter, Body, Response, status, HTTPException
from utils.helper import MakeConnection, QueryResult, HashPassword
from models.body import CreateUser, CreateTask
from models.queries import CreateNewUser, CreateNewTask
from controllers.create import UsernameExist
from datetime import datetime

Router = APIRouter()

@Router.post("/user")
async def CreateUser(User: CreateUser = Body(...)):
    try:
        ConnectionString = MakeConnection()
        try:
            if(UsernameExist(User.Username)):
                User = QueryResult(ConnectionString, CreateNewUser, 'create', (User.Username, (User.Firstname).capitalize(), (User.Lastname).capitalize(), HashPassword(User.Password),))
                return Response(status_code=status.HTTP_201_CREATED)
            else:
                return Response(status_code=status.HTTP_400_BAD_REQUEST)
        except:
            return {"Status":"Cannot Create the User"}
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Unable to connect to the database")

@Router.post("/task")
async def CreateTask(Task: CreateTask = Body(...)):
    try: 
        ConnectionString = MakeConnection()
        try:
            Now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(Now)
            Task = QueryResult(ConnectionString, CreateNewTask, 'create', (Task.Name, Task.Description, Now, Task.Username))
            return Response(status_code=status.HTTP_201_CREATED)
        except Exception as Err:
            return {"Status":"Cannot Create the"}
    except:
        return {"Status":"Cannot Connect to the Database"}