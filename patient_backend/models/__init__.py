__version__ = "0.1.0"

from patient_backend.db.connection import DBConnection
from patient_backend.db.common_models import BaseModel


# get declarative base
Base = DBConnection.get_base()

from patient_backend.models.main_models import Patient
