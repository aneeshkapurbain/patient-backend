from typing import List

import patient_backend.models
from patient_backend import schemas, dao
from patient_backend.db.connection import DBConnection
from patient_backend.models.main_models import Patients, Clinics
from patient_backend.urls import PatientUrls
from patient_backend.utils.status_codes import HTTP_STATUS_CODE
from fastapi import Request, Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

conn = DBConnection()
get_db = conn.get_db

# Initialize sqlalchemy and Fast api aegi app
patient_backend.models.Base.metadata.create_all(bind=conn.engine)

app = FastAPI()


@app.get("/health_check")
def app_health_check():
    return {"message": "Health Check, App is working fine"}


# Create a patient
@app.post("/{clinic_id}/patients/", response_model=Patients)
def create_patient(clinic_id: int, patient: Patients, db: Session = Depends(get_db)):
    clinic = db.query(Clinics).filter(Clinics.id == clinic_id).first()
    if clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


# Get a list of patients
@app.get("/patients/", response_model=List[Patients])
def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    patients = db.query(Patients).offset(skip).limit(limit).all()
    return patients


# Get a single patient by ID
@app.get("/patients/{patient_id}", response_model=Patients)
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patients).filter(Patients.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


# Update a patient by ID
@app.put("/patients/{patient_id}", response_model=Patients)
def update_patient(patient_id: int, patient: Patients, db: Session = Depends(get_db)):
    db_patient = db.query(Patients).filter(Patients.id == patient_id).first()
    if db_patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    for key, value in patient.dict().items():
        if key == 'clinicId':
            if value is None or value == '':
                raise HTTPException(status_code=404, detail="Please provide clinic id")
            else:
                clinic = db.query(Clinics).filter(Clinics.id == int(value)).first()
                if clinic is None:
                    raise HTTPException(status_code=404, detail="Clinic not found")
        setattr(db_patient, key, value)
    db.commit()
    db.refresh(db_patient)
    return db_patient


# Delete a patient by ID
@app.delete("/patients/{patient_id}", response_model=Patients)
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patients).filter(Patients.id == patient_id).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return patient
