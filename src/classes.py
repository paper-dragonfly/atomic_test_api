from pydantic import BaseModel

# object that is returned in json format to front end 
class Response(BaseModel):
    status_code: int = 200 
    error_message: str = None
    body: dict = None