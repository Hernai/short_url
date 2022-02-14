from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ShortUrl(BaseModel):
    long_url: str
    code: str
    created_at: Optional[datetime]