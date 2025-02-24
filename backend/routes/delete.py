from fastapi import APIRouter, Body, Response, HTTPException, status
from utils.helper import MakeConnection, QueryResult

Router = APIRouter()

@Router.delete('/user/{UserId}')
async def DeleteUser(UserId: int):
    try:
        ConnectionString = MakeConnection()
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Cannot connect to the database")