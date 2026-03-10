from passlib.context import CryptContext
from datetime import timedelta,datetime
from src.config import config
import jwt as pyjwt
import uuid
import logging

passwd_context = CryptContext(
    schemes=['bcrypt']
)

ACCESS_TOKEN_EXPIRY = 3600

def genearte_passwd_hash(password:str)->str:
    hash = passwd_context.hash(password)

    return hash


def verify_password(password:str,hash:str)->bool:
    return passwd_context.verify(password,hash)


def create_access_token(user_data:dict, expiry:timedelta=None, refresh:bool=False):
    payload = {}
    payload['user'] = user_data
    payload['exp'] = datetime.now() + (expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY))
    payload['jti'] = str(uuid.uuid4())
    if refresh:
        payload['refresh'] = True
    token = pyjwt.encode(
        payload,
        config.JWT_SECRET,
        algorithm=config.JWT_ALGORITHM
    )
    return token
    

def decode_token(token:str)->dict:
    try:
        token_data = pyjwt.decode(
            token,
            config.JWT_SECRET,
            algorithms=[config.JWT_ALGORITHM]
        )
        return token_data
    except pyjwt.PyJWTError as e:
        logging.exception(e)
        return None
