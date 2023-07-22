from pydantic import BaseModel
from datetime import datetime
from typing import List, Union

class Program(BaseModel):
    channel: int
    title: str
    description: Union[str, None]
    category: Union[str, None]
    start_time: datetime
    stop_time: datetime
     
class Channel(BaseModel):
    id: int
    name: str
    icon: Union[str, None]
    programs: List[Program] = []
