#backend
from pydantic import BaseModel
from uuid import UUID


#activity class
class ActivitySchema(BaseModel):
    id: UUID
    name: str
    color: str
    #config class to work with ORMS
    class Config:
        from_attributes = True