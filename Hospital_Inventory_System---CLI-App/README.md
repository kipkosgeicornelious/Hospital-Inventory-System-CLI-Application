# Hospital Inventory Management System

## Overview

The Hospital Inventory Management System is a command-line interface (CLI) application designed to help hospitals manage their inventory efficiently. This application allows users to manage and view information related to patients, doctors, and appointments. It also provides functionalities to manage users, search patients, and generate reports.
The Hospital Inventory Management System is a command-line interface (CLI) application designed to help hospitals manage their inventory efficiently. This application allows users to manage and view information related to patients, doctors, and appointments. It also provides functionalities to manage users, search patients, and generate reports.

## Features

### Admin Side

- **Manage Patients**: Add, delete, and update patient information.
- **Manage Doctors**: Add, delete, and update doctor information.
- **Manage Appointments**: Book, update, and cancel appointments.
- **Manage Users**: Add and manage user accounts.
- **Generate Reports**: Create reports based on the hospital's data.

### User Side

- **View Departments**: Display a list of available hospital departments.
- **View Doctors**: Display a list of available doctors.
- **View Patient Residents**: Display a list of all patient residents.
- **View Patient Details**: Display detailed information of a specific patient.
- **View Doctor's Appointments**: Check available appointments for doctors.
- **Search Patients**: Search for patients by different attributes.

## Installation

### Prerequisites

- Python 3.x
- Pipenv

### Steps

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/hospital-system-cli.git
    ```

2. **Change into the project directory**:

    ```sh
    cd hospital-system-cli
    ```

3. **Install dependencies**:

    ```sh
    pipenv install
    ```

4. **Activate the virtual environment**:

    ```sh
    pipenv shell
    ```

5. **Initialize the database**:

    ```sh
    python lib/init_db.py
    ```

## Usage

To run the main application, execute the following command:

```sh
python lib/cli.py
```

## Development

For development purposes, you can use ipython for an interactive shell. This is useful for testing and debugging.

## Database Initialization

To reset the database, run:

```sh
python lib/init_db.py
```

This will recreate the database and initialize it with the required tables.

## Project Structure

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── patient.py
    │   ├── doctor.py
    │   ├── appointment.py
    │   ├── user.py
    │   └── role.py
    ├── cli.py
    ├── debug.py
    ├── helpers.py
    └── init_db.py
```

## Models

- **Patient**: Contains information about patients.
- **Doctor**: Contains information about doctors.
- **Appointment**: Contains information about appointments.
- **User**: Contains information about users who can access the system.
- **Role**: Defines roles for users.

## Scripts

- **cli.py**: Main entry point for the application.
- **debug.py**: Script for debugging purposes.
- **helpers.py**: Contains helper functions for database operations.
- **init_db.py**: Initializes and sets up the database.

## Dependencies

- Python 3.x
- **SQLAlchemy**: ORM for database operations.
- **Pipenv**: For managing dependencies and virtual environments.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
