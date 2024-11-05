from sqlalchemy.orm import sessionmaker
from models import engine
from models.patient import Patient
from models.doctor import Doctor
from models.appointment import Appointment
from models.user import User
from models.role import Role
from datetime import datetime

Session = sessionmaker(bind=engine)


def add_patient(name, age, address, phone):
    session = Session()
    new_patient = Patient(name=name, age=age, address=address, phone=phone)
    session.add(new_patient)
    session.commit()


def delete_patient(patient_id):
    session = Session()
    patient = session.query(Patient).filter_by(id=patient_id).first()
    if patient:
        session.delete(patient)
        session.commit()


def update_patient(patient_id, name=None, age=None, address=None, phone=None):
    session = Session()
    patient = session.query(Patient).filter_by(id=patient_id).first()
    if patient:
        if name:
            patient.name = name
        if age:
            patient.age = age
        if address:
            patient.address = address
        if phone:
            patient.phone = phone
        session.commit()


def add_doctor(name, specialization, phone):
    session = Session()
    new_doctor = Doctor(name=name, specialization=specialization, phone=phone)
    session.add(new_doctor)
    session.commit()


def delete_doctor(doctor_id):
    session = Session()
    doctor = session.query(Doctor).filter_by(id=doctor_id).first()
    if doctor:
        session.delete(doctor)
        session.commit()


def update_doctor(doctor_id, name=None, specialization=None, phone=None):
    session = Session()
    doctor = session.query(Doctor).filter_by(id=doctor_id).first()
    if doctor:
        if name:
            doctor.name = name
        if specialization:
            doctor.specialization = specialization
        if phone:
            doctor.phone = phone
        session.commit()


def book_appointment(patient_id, doctor_id, appointment_time):
    session = Session()
    new_appointment = Appointment(
        patient_id=patient_id, doctor_id=doctor_id, appointment_time=appointment_time
    )
    session.add(new_appointment)
    session.commit()


def update_appointment(
    appointment_id, patient_id=None, doctor_id=None, appointment_time=None
):
    session = Session()
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if appointment:
        if patient_id:
            appointment.patient_id = patient_id
        if doctor_id:
            appointment.doctor_id = doctor_id
        if appointment_time:
            appointment.appointment_time = appointment_time
        session.commit()


def cancel_appointment(appointment_id):
    session = Session()
    appointment = session.query(Appointment).filter_by(id=appointment_id).first()
    if appointment:
        session.delete(appointment)
        session.commit()


def view_departments():
    departments = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Radiology"]
    for department in departments:
        print(department)


def view_doctors():
    session = Session()
    doctors = session.query(Doctor).all()
    for doctor in doctors:
        print(
            f"ID: {doctor.id}, Name: {doctor.name}, Specialization: {doctor.specialization}, Phone: {doctor.phone}"
        )


def view_patient_residents():
    session = Session()
    patients = session.query(Patient).all()
    for patient in patients:
        print(
            f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Address: {patient.address}, Phone: {patient.phone}"
        )


def view_patient_details(patient_id):
    session = Session()
    patient = session.query(Patient).filter_by(id=patient_id).first()
    if patient:
        print(
            f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Address: {patient.address}, Phone: {patient.phone}"
        )
    else:
        print("Patient not found.")


def view_doctor_appointments(doctor_id):
    session = Session()
    appointments = session.query(Appointment).filter_by(doctor_id=doctor_id).all()
    print("\nDoctor's Appointments")
    for appointment in appointments:
        print(
            f"Appointment ID: {appointment.id}, Patient ID: {appointment.patient_id}, Appointment Time: {appointment.appointment_time}"
        )


def add_user(username, password, role_id):
    session = Session()
    new_user = User(username=username, password=password, role_id=role_id)
    session.add(new_user)
    session.commit()


def delete_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()


def update_user(user_id, username=None, password=None, role_id=None):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        if username:
            user.username = username
        if password:
            user.password = password
        if role_id:
            user.role_id = role_id
        session.commit()


def search_patients(query):
    session = Session()
    return session.query(Patient).filter(Patient.name.like(f"%{query}%")).all()


def filter_appointments_by_date(start_date, end_date):
    session = Session()
    return (
        session.query(Appointment)
        .filter(Appointment.appointment_time.between(start_date, end_date))
        .all()
    )


def generate_patient_report():
    session = Session()
    patients = session.query(Patient).all()
    report = []
    for patient in patients:
        report.append(
            {
                "ID": patient.id,
                "Name": patient.name,
                "Age": patient.age,
                "Address": patient.address,
                "Phone": patient.phone,
            }
        )
    return report


def generate_appointment_statistics():
    session = Session()
    total_appointments = session.query(Appointment).count()
    upcoming_appointments = (
        session.query(Appointment)
        .filter(Appointment.appointment_time > datetime.now())
        .count()
    )
    return {
        "Total Appointments": total_appointments,
        "Upcoming Appointments": upcoming_appointments,
    }
