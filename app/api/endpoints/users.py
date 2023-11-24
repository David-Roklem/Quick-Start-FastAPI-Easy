from fastapi import FastAPI
import uvicorn

from app.api.schemas.user import User

app = FastAPI()

users = {}


@app.post('/auth/register/')
def register(user: User):
    users['username'] = user.username
    users['password'] = user.password
    print(users)
    return {'message': 'The user was successfully registered'}


@app.post('/auth/login/')
def login(user: User):
    if user.username == users['username'] and\
            user.password == users['password']:
        return {'message': 'The user was successfully logged in'}
    else:
        return {'message': 'The user was not logged in'}


if __name__ == '__main__':
    uvicorn.run('users:app', host='127.0.0.1', port=8000, reload=True)
