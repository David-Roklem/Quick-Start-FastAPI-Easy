from fastapi import FastAPI
import uvicorn

from app.api.schemas.user import User

app = FastAPI()

users = {}


@app.post('/auth/register/')
def register(user: User):
    users['username'] = user.username
    users['password'] = user.password
    return {"message": "The user was successfully registered"}


if __name__ == '__main__':
    uvicorn.run('users:app', host='127.0.0.1', port=8000, reload=True)
