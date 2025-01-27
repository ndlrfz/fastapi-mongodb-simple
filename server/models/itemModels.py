from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str
    category: str
    stocks: int
    price: int = Field(gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Company Smart Watch",
                "category": "smartwatch",
                "stocks": 10,
                "price": 1000,
            }
        }

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    stocks: Optional[int] = None
    price: Optional[int] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "New Smart watch",
                "category": "new-smartwatch",
                "stocks": 5,
                "price": 500,
                }
            }
