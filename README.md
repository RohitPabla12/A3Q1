Video: https://drive.google.com/file/d/180XtB-6VWp887Ah5OynD_bkSKNthzY_8/view?usp=drive_link

Step 1: Create the `student_db` Database

1. Launch pgAdmin

2. Create Database: 
    - Right-click on 'Databases', select 'Create', then 'Database…'.
    - Name the database `student_db` and click 'Save'.

----------------------------------------------------

Step 2: Clone the Repository

1. Open Terminal or Command Prompt where you want to clone the repository.

2. Clone the Repository: Run the following command: git clone https://github.com/RohitPabla12/A3Q1.git

If that is not an option, Go to: https://github.com/RohitPabla12/A3Q1
   
------------------------------------------------------------

Step 3: Initialize

Method 1:

1. Run the following command to create the students table: psql -d student_db -f ini_table.sql

If prompted, enter your password for the PostgreSQL user account.


2. Run the following command to populate the students table with initial data: psql -d student_db -f ini_data.sql


Method 2:

1. Open Query Tool: Navigate to `student_db`, right-click it, and select 'Query Tool'.

2. Create Table:
    - Open `ini_table.sql` (located in the cloned repository) with a text editor.
    - Copy the SQL commands and paste them into the Query Tool in pgAdmin.
    - Execute the script to create the `students` table.

3. Insert Data:
    - Open `ini_data.sql` in a text editor.
    - Copy and paste the SQL commands into the Query Tool in pgAdmin.
    - Execute the script to insert initial data into the `students` table.

Both these files can be opened and executed via the GUI.

----------------------------------

Step 4: Run the Python Code

1. Install psycopg2: If not already installed, open a terminal or command prompt, in the project directory, and run: pip install psycopg2
   
2. Ensure the database connection details (`DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`) in the script match your PostgreSQL setup.

3. Execute the Script: In the terminal or command prompt, ensure you are in the project directory and run: python main.py

The code at the bottom must be uncommented for testing purposes.
