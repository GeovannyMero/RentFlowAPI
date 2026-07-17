from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Apartment(BaseModel):
    id: Optional[UUID] = None
    number: str
    name: str
    description: Optional[str] = None
    monthly_rent: Decimal
    status: str
    bedrooms: int
    bathrooms: Decimal
    area: Decimal
    floor: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    user_id: UUID

    model_config = {
        "from_attributes": True
    }
