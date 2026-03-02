from pydantic import BaseModel
from typing import Literal
from uuid import UUID


class Status(BaseModel):
    state:Literal["running", "stopped", "error", "pending", "starting"]
    healthy:bool

class SessionInfo(BaseModel):
    sessionid: UUID
    image: str
    tag: str
    status: Status

class SessionList(BaseModel):
    sessions: list[SessionInfo]

class ListResponse(BaseModel):
    status: Status
    sessions: list[SessionInfo]

class GetResponse(BaseModel):
    status: Status
    session: SessionInfo

class CreateResponse(BaseModel):
    status: Status
    sessionid: UUID

class DestroyResponse(BaseModel):
    status: Status
    sessionid: UUID

