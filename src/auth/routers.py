from fastapi import APIRouter , Depends,status
from .schemas import UserCreateModel,UserModel
from .service import UserService
from src.db.main import get_session
from sqlalchemy.ext.asyncio.session import AsyncSession
from fastapi.exceptions import HTTPException

auth_router = APIRouter()
user_service = UserService()


@auth_router.post('/signup',status_code=status.HTTP_201_CREATED,response_model=UserModel)
async def create_user_account(user_data:UserCreateModel,session:AsyncSession=Depends(get_session)):
    email = user_data.email

    user_exists = await user_service.get_user_by_email(email,session)

    if user_exists:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,detail="user with email already exists")
    
    new_useer = await user_service.create_user(user_data,session)

    return new_useer







