from datetime import date, datetime

from pydantic import BaseModel
from typing import Optional, List, Dict


class PatientCreate(BaseModel):
    externalId: Optional[str]
    firstName: str
    lastName: str
    dateOfBirth: Optional[date]
    verified: bool = False
    notes: Optional[str]
    isActive: bool = True
    anticoagulation: bool = False
    anticoagulationDate: Optional[datetime]
    pacingDependent: bool = False
    address: Optional[str]
    mobile: Optional[str]
    landline: Optional[str]
    email: Optional[str]
    gpName: Optional[str]
    gpAddress: Optional[str]
    gpPhone: Optional[str]
    gpEmail: Optional[str]
    otherNotes: Optional[str]
    nextTm = Optional[datetime]
    tmSchedule: Optional[str]
    clinicId: int
    statusComment: Optional[str]
    lockedAt: Optional[datetime]
    lockedByEmail: Optional[str]
    lockedByName: Optional[str]


class PatientDetails(BaseModel):
    externalId: Optional[str]
    firstName: str
    lastName: str
    dateOfBirth: Optional[date]
    verified: bool = False
    notes: Optional[str]
    isActive: bool = True
    anticoagulation: bool = False
    anticoagulationDate: Optional[datetime]
    pacingDependent: bool = False
    address: Optional[str]
    mobile: Optional[str]
    landline: Optional[str]
    email: Optional[str]
    gpName: Optional[str]
    gpAddress: Optional[str]
    gpPhone: Optional[str]
    gpEmail: Optional[str]
    otherNotes: Optional[str]
    nextTm = Optional[datetime]
    tmSchedule: Optional[str]
    clinicId: int
    statusComment: Optional[str]
    lockedAt: Optional[datetime]
    lockedByEmail: Optional[str]
    lockedByName: Optional[str]




