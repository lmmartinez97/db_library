# Library Management System

This project is focused on creating a Library Management System using Flask and SQLAlchemy. Initially, the focus will be on the database, including writing the code to create and populate the necessary tables. Once the database is set up, the project will eventually expand to include a web interface.

## Features

- Add, update, delete, and view books.
- Manage library members and their details.
- Record and track book loans and returns.
- Generate reports on overdue books.
- Search and filter functionality for books and members.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/library_management.git
   cd library_management
   ```

2. **Create and activate the Conda environment:**

   ```bash
   conda create -n library_management python=3.10
   conda activate library_management
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   - **Create the database and tables:**

     ```bash
     python scripts/create_db.py
     ```

   - **Populate the database with sample data:**

     ```bash
     python app/populate.py
     ```

5. **Run the application (later when the web interface is added):**

   ```bash
   python run.py
   ```

## Project Structure

The project is organized as follows:

- **`app/` Directory:**
  - **`__init__.py`:** This file initializes the Flask application and sets up the database connection.
  - **`models.py`:** Contains the database models (tables) defined using SQLAlchemy. This includes classes like `Book`, `Member`, and `Loan`.
  - **`populate.py`:** A script to populate the database with sample data, making use of libraries like Faker.
  - **`db_operations.py`:** Contains utility functions for interacting with the database, such as querying for data or performing CRUD operations.

- **`migrations/` Directory:**
  - This directory will store database migrations once you start using Flask-Migrate. Migrations allow you to manage changes to the database schema over time.

- **`scripts/` Directory:**
  - **`create_db.py`:** A script to create the database and all necessary tables based on the models defined in `models.py`.
  - **`drop_db.py`:** A script to drop all tables in the database. This is useful for resetting the database during development.

- **`tests/` Directory:**
  - **`test_models.py`:** Contains unit tests for the models to ensure they are correctly defined and functioning.
  - **`test_populate.py`:** Contains tests for the data population script, ensuring data is correctly inserted into the database.
  - **`test_db_operations.py`:** Contains tests for the utility functions in `db_operations.py`.

- **`config.py`:**
  - The configuration file for the Flask app, including settings for the database URI and other Flask extensions.

- **`requirements.txt`:**
  - A list of all Python packages required for the project. Use this file to install dependencies with `pip`.

- **`run.py`:**
  - The main entry point for running the Flask app. This file will become more relevant once the web interface is developed.

- **`README.md`:**
  - This file contains the documentation and an overview of the project. It provides details on the project structure, setup instructions, and progress notes.

## Project Workflow

1. **Database Focus:** Start by defining models in `models.py`, create the database with `create_db.py`, and populate it with sample data using `populate.py`.
2. **Terminal Operations:** Use terminal scripts for database operations until the web interface is implemented.
3. **Web Interface Transition:** Once the database is set up, development will shift towards creating a web interface using Flask.
4. **Testing:** As development progresses, unit tests will be added to ensure the integrity of the models, scripts, and database operations.

## Usage

- **Creating the Database:** Use `python scripts/create_db.py` to create the database and all necessary tables.
- **Populating the Database:** Run `python app/populate.py` to add sample data to the database.
- **Interacting with the Database:** Use `python app/db_operations.py` for various database operations via the terminal.
- **Running the Application:** Once the web interface is implemented, run the app with `python run.py` and navigate to `http://localhost:5000`.

## Dependencies

- Flask
- SQLAlchemy
- Flask-Migrate
- Faker (for generating sample data)

## License

This project is licensed under the MIT License.