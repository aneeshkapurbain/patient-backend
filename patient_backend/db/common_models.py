from sqlalchemy import (
    String,
    Column,
    Integer,
    DateTime
)
from datetime import datetime


class BaseModel:
    """Base Model Containing Columns common to all models"""

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False)
