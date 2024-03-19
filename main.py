import psycopg2

# These two lines are comments indicating commands that might be used in the command line
# to initialize the table and data from SQL files before running this script.
# psql -d student_db -f ini_table.sql
# psql -d student_db -f ini_data.sql

# Database connection details
DB_NAME = "student_db"        # The name of the database to connect to
DB_USER = "postgres"          # The username used to authenticate
DB_PASSWORD = ""              # The password for the database user
DB_HOST = "localhost"         # The host where the database server is running (localhost indicates the same machine)
DB_PORT = 5432                # The port on which the PostgreSQL server is listening (5432 is the default)

def connect_db():
    # Attempts to connect to the PostgreSQL database using the provided credentials and returns a connection object if successful, otherwise prints an error and returns None.
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
        )
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

def get_all_students():
    # Retrieves all student records from the 'students' table in the database and prints them. If connection fails, prints an error.
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM students")  # SQL query to select all records from 'students' table
            students = cursor.fetchall()  # Fetches all rows of a query result, returning a list
            for student in students:
                print(student)  # Prints each student record
        except Exception as e:
            print(f"Error retrieving students: {e}")
        finally:
            connection.close()  # Always close the connection

def add_student(first_name, last_name, email, enrollment_date):
    # Inserts a new student record into the 'students' table with the provided information. Commits the transaction if successful, prints an error if not.
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, enrollment_date),
            )
            connection.commit()  # Commits the current transaction
            print(f"Student added successfully!")
        except Exception as e:
            print(f"Error adding student: {e}")
        finally:
            connection.close()

def update_student_email(student_id, new_email):
    # Updates the email address of the student with the specified 'student_id'. Commits the change if successful, prints an error if not.
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                "UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id)
            )
            connection.commit()
            print(f"Student email updated successfully!")
        except Exception as e:
            print(f"Error updating student email: {e}")
        finally:
            connection.close()

def delete_student(student_id):
    # Deletes the record of the student with the specified 'student_id' from the 'students' table. Commits the transaction if successful, prints an error if not.
    connection = connect_db()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
            connection.commit()
            print("Student deleted successfully!")
        except Exception as e:
            print(f"Error deleting student: {e}")
        finally:
            connection.close()

# For Testing:

# get_all_students()

# add_student("Alice", "Wonderland", "alice@example.com", "2023-10-26")

# get_all_students()

# update_student_email(2, "jane.doe.updated@example.com")

# get_all_students()

# delete_student(1)

# get_all_students()