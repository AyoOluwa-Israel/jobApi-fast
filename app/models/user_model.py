from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field


class User(Document):
  user_id: UUID = Field(default_factory=uuid4)
  username: str = Indexed(str, unique=True)
  email: str = Indexed(str, unique=True)
  hashed_password= str
  first_name: str 
  last_name: str
  disabled: bool