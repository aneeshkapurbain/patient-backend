from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from patient_backend.db.common_models import BaseModel
from patient_backend.models import Base


class Clinics(Base, BaseModel):
	__tablename__ = "clinics"

	name = Column(String(200), nullable=False)
	address = Column(String(200), nullable=False)
	email = Column(String(200), nullable=True)
	phoneNumber = Column(String(200), nullable=True)
	isActive = Column(Boolean, nullable=False, default=True)
	# todo
	# region = Column()
	patients = relationship('Patients', back_populates='clinics')
	# headClinicId = Column(Integer, index=True)


class Patients(Base, BaseModel):
	__tablename__ = "patients"

	externalId = Column(String(200), nullable=True)
	firstName = Column(String(200), nullable=False)
	lastName = Column(String(200), nullable=False)
	dateOfBirth = Column(Date, nullable=True)
	# todo
	sex = Column()
	verified = Column(Boolean, nullable=False, default=False)
	notes = Column(String(200), nullable=True)
	isActive = Column(Boolean, nullable=False, default=True)
	anticoagulation = Column(Boolean, nullable=False, default=False)
	anticoagulationDate = Column(DateTime, nullable=True)
	pacingDependent = Column(Boolean, nullable=False, default=False)
	# todo
	# medication = Column()
	address = Column(String(200), nullable=True)
	mobile = Column(String(200), nullable=True)
	landline = Column(String(200), nullable=True)
	email = Column(String(200), nullable=True)
	gpName = Column(String(200), nullable=True)
	gpAddress = Column(String(200), nullable=True)
	gpPhone = Column(String(200), nullable=True)
	gpEmail = Column(String(200), nullable=True)
	otherNotes = Column(String(200), nullable=True)
	nextTm = Column(DateTime, nullable=True)
	tmSchedule = Column(String(200), nullable=True)
	clinicId = Column(Integer, ForeignKey("clinics.id"), index=True)
	# todo
	# followupPhysicianId = Column(Integer, nullable=True)
	# todo
	# status = Column()
	statusComment = Column(String(200), nullable=True)
	lockedAt = Column(DateTime, nullable=True)
	lockedByEmail = Column(String(200), nullable=True)
	lockedByName = Column(String(200), nullable=True)

	clinics = relationship('Clinics', back_populates='patients')

