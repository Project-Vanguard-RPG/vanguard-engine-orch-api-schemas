from pydantic import BaseModel, Field
from uuid import UUID

class Create(BaseModel):
    image:str
    tag:str
    sessionid: UUID

class Destroy(BaseModel):
    sessionid: UUID

class Get(BaseModel):
    sessionid: UUID

class List(BaseModel):
    pass