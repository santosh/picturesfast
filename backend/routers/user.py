from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import JWTError, jwt
from backend import config

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    username: str
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.PICTURES_SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    return encoded_jwt

router = APIRouter()

# POST /user/login
@router.post("/login", tags=["users"], summary="Login an existing user")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Login a user given the username and password. A JWT token
    is sent on the success, or 401 response on failure.

    - **username**: username to login with
    - **password**: password for username
    """
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect surename or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}



# POST /user/register
# @router.post("/", tags=["users"], summary="Register a new user")
# async def login_user(request: Request, user: User):
#     """Register a new user. A username, password and email is required.

#     - **username**: username to login with
#     - **password**: password for username
#     - **email**: email of username
#     """
#     pass

# GET /user/profile/:id

