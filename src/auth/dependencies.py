from fastapi.security import HTTPBearer
from fastapi import Request,status
from fastapi.security.http import HTTPAuthorizationCredentials
from .utils import decode_token
from fastapi.exceptions import HTTPException


class AccessTokenBearer(HTTPBearer):
    
    def __init__(self,auto_error=True):
        super().__init__(auto_error=auto_error)


    async def __call__(self, request:Request) -> HTTPAuthorizationCredentials|None:
        creds = await super().__call__(request)
        print(creds.scheme)
        print(creds.credentials)
        token = creds.credentials

        token_data = decode_token(token)
        if not token:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,
                                detail="Invalid or Expired Token" )
        if token_data['refresh']:
            raise HTTPException(status_code= status.HTTP_403_FORBIDDEN,
                                detail="Please provide an access token" )
        
        return token_data
    
    def token_valid(self,token:str)->bool:
        token_data = decode_token(token)
        if token is not None:
            return True
        else:
            return False



