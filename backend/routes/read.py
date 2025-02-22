from fastapi import APIRouter, Response, status, HTTPException
from utils.helper import MakeConnection, QueryResult
from models.queries import GetTasks

Router = APIRouter()

@Router.get("/task-todo/{Username}")
async def GetTaskTodos(Username: str):
    try:
        ConnectionString = MakeConnection()
        try:
            TaskTodos = QueryResult(ConnectionString, GetTasks, 'readall', (Username,))
            return TaskTodos
        except:
            return None
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to the database")