from typing_extensions import Annotated
from pydantic import BaseModel, Field


class User(BaseModel):
    username: Annotated[str, Field(max_length=50)]
    password: Annotated[str, Field(min_length=8, max_length=50)]
