from datetime import datetime
from colorama import init, Fore, Style
from tabulate import tabulate
from helpers import (
    add_patient,
    delete_patient,
    update_patient,
    add_doctor,
    delete_doctor,
    update_doctor,
    book_appointment,
    update_appointment,
    cancel_appointment,
    view_departments,
    view_doctors,
    view_patient_residents,
    view_patient_details,
    view_doctor_appointments,
    add_user,
    delete_user,
    update_user,
    search_patients,
    filter_appointments_by_date,
    generate_patient_report,
    generate_appointment_statistics,
)
from models import init_db

# Initialize colorama
init(autoreset=True)


# Define the new view functions here or import them if defined elsewhere
def view_doctors_tabulated():
    session = session()
    doctors = session.query(doctor).all()
    data = []
    for doctor in doctors:
        data.append([doctor.id, doctor.name, doctor.specialization, doctor.phone])
    print(
        tabulate(
            data, headers=["ID", "Name", "Specialization", "Phone"], tablefmt="pretty"
        )
    )


def view_patient_residents_tabulated():
    session = session()
    patients = session.query(patient).all()
    data = []
    for patient in patients:
        data.append(
            [patient.id, patient.name, patient.age, patient.address, patient.phone]
        )
    print(
        tabulate(
            data, headers=["ID", "Name", "Age", "Address", "Phone"], tablefmt="pretty"
        )
    )


def view_patient_details_tabulated(patient_id):
    session = session()
    patient = session.query(patient).filter_by(id=patient_id).first()
    if patient:
        data = [[patient.id, patient.name, patient.age, patient.address, patient.phone]]
        print(
            tabulate(
                data,
                headers=["ID", "Name", "Age", "Address", "Phone"],
                tablefmt="pretty",
            )
        )
    else:
        print("Patient not found.")


def view_doctor_appointments_tabulated(doctor_id):
    session = session()
    appointments = session.query(appointment).filter_by(doctor_id=doctor_id).all()
    data = []
    for appointment in appointments:
        data.append(
            [appointment.id, appointment.patient_id, appointment.appointment_time]
        )
    print(
        tabulate(
            data,
            headers=["Appointment ID", "Patient ID", "Appointment Time"],
            tablefmt="pretty",
        )
    )


def display_welcome_message():
    print(Fore.BLUE + "Hii👋 Welcome to SDF_FT-09 Hospital.")
    print(
        Fore.YELLOW
        + "Where it's vibes and insha allah until we start standing on Business! 😅"
    )
    print(Fore.CYAN + "Don't worry, we've got you.")


def is_valid(name):
    if not name.isalpha() or name.strip() == "":
        raise ValueError("Patient name must contain only characters and cannot be empty.")
    return name
def is_valid_age(age):
    age = int(age)
    if age < 0 or age > 110:
        raise ValueError("Age must be a number between 0 and 110.")
    return age
def is_valid_phone_number(phone):
    if not phone.isnumeric() or len(phone)!= 10:
        raise ValueError("Phone number must be 10 digits.")
    return phone

def patient_menu():
    
    while True:
        print("\nPatient Menu")
        print("1. Add New Patient")
        print("2. Delete Patient")
        print("3. Update Patient Details")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter patient name: ")
            name=is_valid(name)
            age = input("Enter patient age: ")
            age=is_valid_age(age)
            address = input("Enter patient address: ")
            phone = input("Enter patient phone:(07xxxxxxxx)")
            phone=is_valid_phone_number(phone)
            add_patient(name, age, address, phone)
            print("Patient added successfully.")

        elif choice == "2":
            patient_id = input("Enter patient ID to delete: ")
            delete_patient(patient_id)
            print("Patient deleted successfully.")

        elif choice == "3":
            patient_id = input("Enter patient ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            age = input("Enter new age (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            phone = input("Enter new phone (leave blank to skip): ")
            update_patient(patient_id, name, age, address, phone)
            print("Patient details updated successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")

    
def doctor_menu():
    while True:
        print("\nDoctor Menu")
        print("1. Add New Doctor")
        print("2. Delete Doctor")
        print("3. Update Doctor Details")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter doctor name: ")
            is_valid(name)
            specialization = input("Enter doctor specialization: ")
            phone = input("Enter doctor phone: ")
            is_valid_phone_number(phone)
            add_doctor(name, specialization, phone)
            print("Doctor added successfully.")

        elif choice == "2":
            doctor_id = input("Enter doctor ID to delete: ")
            delete_doctor(doctor_id)
            print("Doctor deleted successfully.")

        elif choice == "3":
            doctor_id = input("Enter doctor ID to update: ")
            name = input("Enter new name (leave blank to skip): ")
            specialization = input("Enter new specialization (leave blank to skip): ")
            phone = input("Enter new phone (leave blank to skip): ")
            update_doctor(doctor_id, name, specialization, phone)
            print("Doctor details updated successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def appointment_menu():
    while True:
        print("\nAppointment Menu")
        print("1. Book Appointment")
        print("2. Update Appointment")
        print("3. Cancel Appointment")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = input("Enter patient ID: ")
            doctor_id = input("Enter doctor ID: ")
            appointment_time_str = input("Enter appointment time (YYYY-MM-DD HH:MM): ")
            try:
                appointment_time = datetime.strptime(
                    appointment_time_str, "%Y-%m-%d %H:%M"
                )
                book_appointment(patient_id, doctor_id, appointment_time)
            except ValueError:
                print("Invalid date/time format. Please try again.")
            else:
                print("Appointment booked successfully.")

        elif choice == "2":
            appointment_id = input("Enter appointment ID to update: ")
            patient_id = input("Enter new patient ID (leave blank to skip): ")
            doctor_id = input("Enter new doctor ID (leave blank to skip): ")
            appointment_time = input(
                "Enter new appointment time (YYYY-MM-DD HH:MM, leave blank to skip): "
            )
            update_appointment(appointment_id, patient_id, doctor_id, appointment_time)
            print("Appointment updated successfully.")

        elif choice == "3":
            appointment_id = input("Enter appointment ID to cancel: ")
            cancel_appointment(appointment_id)
            print("Appointment canceled successfully.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


def view_menu():
    while True:
        print("\nView Menu")
        print("1. View Departments")
        print("2. View Doctors")
        print("3. View Patient Residents")
        print("4. View Patient Details")
        print("5. View Doctor Appointments")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_departments()

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            view_patient_residents()

        elif choice == "4":
            patient_id = input("Enter patient ID: ")
            view_patient_details(patient_id)

        elif choice == "5":
            doctor_id = input("Enter doctor ID: ")
            view_doctor_appointments(doctor_id)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add User")
        print("2. Delete User")
        print("3. Update User")
        print("4. Search Patients")
        print("5. Filter Appointments by Date")
        print("6. Generate Patient Report")
        print("7. Generate Appointment Statistics")
        print("8. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            role_id = input("Enter role ID: ")
            add_user(username, password, role_id)
            print("User added successfully.")

        elif choice == "2":
            user_id = input("Enter user ID to delete: ")
            delete_user(user_id)
            print("User deleted successfully.")

        elif choice == "3":
            user_id = input("Enter user ID to update: ")
            username = input("Enter new username (leave blank to skip): ")
            password = input("Enter new password (leave blank to skip): ")
            role_id = input("Enter new role ID (leave blank to skip): ")
            update_user(user_id, username, password, role_id)
            print("User details updated successfully.")

        elif choice == "4":
            query = input("Enter search query: ")
            patients = search_patients(query)
            for patient in patients:
                print(
                    f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, Address: {patient.address}, Phone: {patient.phone}"
                )

        elif choice == "5":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            appointments = filter_appointments_by_date(start_date, end_date)
            for appointment in appointments:
                print(
                    f"ID: {appointment.id}, Patient ID: {appointment.patient_id}, Doctor ID: {appointment.doctor_id}, Appointment Time: {appointment.appointment_time}"
                )

        elif choice == "6":
            report = generate_patient_report()
            for patient in report:
                print(patient)

        elif choice == "7":
            stats = generate_appointment_statistics()
            print(stats)

        elif choice == "8":
            break

        else:
            print("Invalid choice. Please try again.")


def main_menu():
    init_db()
    display_welcome_message()  # Call the welcome message here
    while True:
        print("\nMain Menu")
        print("1. Patient Menu")
        print("2. Doctor Menu")
        print("3. Appointment Menu")
        print("4. View Menu")
        print("5. Admin Menu")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            appointment_menu()

        elif choice == "4":
            view_menu()

        elif choice == "5":
            admin_menu()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
