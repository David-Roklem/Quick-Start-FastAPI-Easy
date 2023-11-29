from fastapi import FastAPI, HTTPException, status
import uvicorn

from app.api.schemas.user import User
from app.core.hash_password import get_password_hash, verify_password

app = FastAPI()

users = {}


@app.post('/auth/register/')
def register(user: User) -> dict:
    # First of all I need to make sure that there no user with the same
    # username as provided in my 'DB'
    user_exists = users.get(user.username)
    if user_exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='The user already exists in the DB'
        )

    # The next step is to hash the password provided
    hashed_password = get_password_hash(user.password)

    users['username'] = user.username
    users['password'] = hashed_password
    return {'message': 'The user was successfully registered'}


@app.post('/auth/login/')
def login(user: User) -> dict:
    if user.username == users['username'] and\
            user.password == users['password']:
        return {'message': 'The user was successfully logged in'}
    else:
        return {'message': 'The user was not logged in'}


if __name__ == '__main__':
    uvicorn.run('users:app', host='127.0.0.1', port=8000, reload=True)
