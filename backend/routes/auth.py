from fastapi import APIRouter, Body, Response, status, HTTPException
from utils.helper import MakeConnection, QueryResult, HashPassword
from models.body import GetUserDetails
from models.queries import UserAuthentication
from controllers.auth import CheckPassword
from datetime import datetime, timedelta

Router = APIRouter()

@Router.post('/user')
async def UserAuthenticate(User: GetUserDetails = Body(...)):
    try:
        ConnectionString = MakeConnection()
        try:
            UserPass = QueryResult(ConnectionString, UserAuthentication,'read', (User.Username,))
            if UserPass is None:
                print("It works")
                return Response(status_code=status.HTTP_400_BAD_REQUEST), {"details":"User does not exist"}
            if not CheckPassword(UserPass['Password'], User.Password):
                return Response(status_code=status.HTTP_401_UNAUTHORIZED), {"details":"Wrong Password"}
            else:
                CreatedAt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ExpiredAt = (datetime.now() + timedelta(hours=5)).strftime("%Y-%m-%d %H:%M:%S")
                
                return {"authentication": True, "created_at": CreatedAt, "expired_at": ExpiredAt, "username": User.Username}
        except:
            raise HTTPException(status_code=status.HTTP_100_CONTINUE)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)