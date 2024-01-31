from typing import Optional, Union, Annotated
from pydantic import BaseModel, Field, HttpUrl

class Main_User(BaseModel):
    name: Optional[str] = None
    id: Annotated[Optional[int], Field(default=100, ge=1, lt=200)] = None
    
class Main_UserDB(Main_User):
    password: Annotated[Union[str,None], Field(min_length=8, max_length=200)] = None
    
class New_Response(BaseModel):
    message: str
    
    
    