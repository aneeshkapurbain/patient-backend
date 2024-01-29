from sqlalchemy.orm import Session
from patient_backend.models.main_models import Patient


def list_patients(db: Session, skip, limit):
    patients = db.query(Patient).offset(skip).limit(limit).all()
    print("##########", patients)
    return patients

