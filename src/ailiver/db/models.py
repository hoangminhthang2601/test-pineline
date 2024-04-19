"""
Define all the database models.
"""

from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


from .database import Base


class Ogranization(Base):
    """Define organization info."""

    __tablename__ = "organizations"

    org_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255))
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())

    # relationships
    license = relationship("License", back_populates="organization")
    payment = relationship("Payment", back_populates="organization")
    patient = relationship("Patient", back_populates="organization")
    doctor = relationship("Doctor", back_populates="organization")


class Payment(Base):
    """Define payment table."""

    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    license_id = Column(Integer, ForeignKey("licenses.license_id"))
    payment_detail_id = Column(
        Integer,
        ForeignKey("payment_details.payment_detail_id"),
        primary_key=True,
    )
    org_id = Column(Integer, ForeignKey("organizations.org_id"))
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    # relationships
    organization = relationship("Organization", back_populates="payment")
    license = relationship("License", uselist=False, back_populates="payment")
    payment_detail = relationship(
        "PaymentDetail",
        uselist=False,
        back_populates="payment",
    )


class PaymentDetail(Base):
    """Define payment detail table."""

    __tablename__ = "payment_details"

    payment_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey("payments.payment_id"))
    payment_method = Column(String(length=255))
    amount = Column(Integer)
    name = Column(String(255))
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    # relationships
    payment = relationship("Payment", back_populates="payment_detail")


class License(Base):
    """Define license table."""

    __tablename__ = "licenses"

    license_id = Column(Integer, primary_key=True, autoincrement=True)
    org_id = Column(Integer, ForeignKey("organizations.org_id"))
    payment_id = Column(Integer, ForeignKey("payments.payment_id"))
    is_activate = Column(Boolean, default=True)
    start_date = Column(DateTime(timezone=True), server_default=func.now())
    end_date = Column(DateTime(timezone=True))
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())

    # relationship
    payment = relationship("Payment", back_populates="license")
    organization = relationship("Organization", back_populates="license")


class Patient(Base):
    """Define patient inforation table."""

    __tablename__ = "patients"

    pid = Column(Integer, primary_key=True, autoincrement=True)
    org_id = Column(Integer, ForeignKey("organizations.org_id"))
    name = Column(String(length=255))
    dob = Column(DateTime)
    gender = Column(Boolean)
    others = Column(String)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())

    # relationships
    organization = relationship("Organization", back_populates="patient")
    diagnose = relationship("Diagnose", uselist=False, back_populates="patient")


class Doctors(Base):
    """Define doctor infomation table."""

    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, autoincrement=True)
    org_id = Column(Integer, ForeignKey("organizations.org_id"))
    name = Column(String(length=255))
    title = Column(String(length=255))
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())

    # relationships
    organization = relationship("Organization", back_populates="doctor")
    diagnose = relationship("Diagnose", back_populates="doctor")


class Diagnoses(Base):
    """Define diagnose result table."""

    __tablename__ = "diagnoses"

    dia_id = Column(Integer, primary_key=True, autoincrement=True)
    dia_detail_id = Column(Integer, ForeignKey("diagnose_details.dia_detail_id"))
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"))
    pid = Column(Integer, ForeignKey("patients.pid"))
    ai_lr = Column(String(length=255))
    doctor_lr = Column(String(length=255))
    created_date = Column(DateTime(timezone=True), server_default=func.now())

    # relationship
    doctor = relationship("Doctor", back_populates="diagnose")
    patient = relationship("Patient", back_populates="diagnose")
    diagose_detail = relationship(
        "DiagnoseDetail",
        uselist=False,
        back_populates="diagnose",
    )


class DiagnoseDetails(Base):
    """Define diagnose detail table."""

    __tablename__ = "diagnose_details"
    dia_detail_id = Column(Integer, primary_key=True, autoincrement=True)
    dia_id = Column(Integer, ForeignKey("diagnoses.dia_id"))
    tumor_number = Column(Integer)
    tumor_size = Column(Float)
    washout = Column(Boolean)
    capsule = Column(Boolean)
    threshold_growth = Column(Boolean)
    APHE = Column(Boolean)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
    updated_date = Column(DateTime(timezone=True), onupdate=func.now())

    # relationships
    diagose = relationship("Diagnose", back_populates="diagose_detail")
