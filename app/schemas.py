from pydantic import BaseModel

class UserEvent(BaseModel):
    message: str
    user_id: int | None = None
