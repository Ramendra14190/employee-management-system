<<<<<<< HEAD

import psycopg

#database connection

conn = psycopg.connect(
    host="localhost",
    dbname="employee_db",
    user="postgres",
    password="rsc123",
    port=5432
)

cur = conn.cursor()

print("PROGRAM STARTED")


#creating table

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees_new (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(100),
        salary NUMERIC(10, 2)
    )
""")

conn.commit()


#1. To add employee

def add_employee():

    print("\n--- ADD EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID: "))

        name = input("Enter employee name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))

        cur.execute("""
            INSERT INTO employees_new (id, name, department, salary)
            VALUES (%s, %s, %s, %s)
        """, (emp_id, name, department, salary))

        conn.commit()

        print("Employee added successfully.")

    except ValueError:
        print("Please enter a valid numeric ID and salary.")

    except psycopg.errors.UniqueViolation:
        conn.rollback()
        print("This employee ID already exists.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)


#2. To veiw employee

def view_employees():

    print("\n--- ALL EMPLOYEES ---")

    cur.execute("""
        SELECT id, name, department, salary
        FROM employees_new
        ORDER BY id
    """)

    employees = cur.fetchall()

    if not employees:
        print("No employees found.")
        return

    print("\nID | Name | Department | Salary")
    print("-" * 55)

    for employee in employees:
        print(
            employee[0],
            "|",
            employee[1],
            "|",
            employee[2],
            "|",
            employee[3]
        )


#3. To search employee

def search_employee():

    print("\n--- SEARCH EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID: "))

        cur.execute("""
            SELECT id, name, department, salary
            FROM employees_new
            WHERE id = %s
        """, (emp_id,))

        employee = cur.fetchone()

        if employee:

            print("\nEmployee Found")
            print("ID:", employee[0])
            print("Name:", employee[1])
            print("Department:", employee[2])
            print("Salary:", employee[3])

        else:
            print("Employee not found.")

    except ValueError:
        print("Please enter a valid numeric employee ID.")


#4. to update details of employee

def update_employee():

    print("\n--- UPDATE EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID to update: "))

        cur.execute("""
            SELECT id
            FROM employees_new
            WHERE id = %s
        """, (emp_id,))

        employee = cur.fetchone()

        if not employee:
            print("Employee not found.")
            return

        name = input("Enter new name: ")
        department = input("Enter new department: ")
        salary = float(input("Enter new salary: "))

        cur.execute("""
            UPDATE employees_new
            SET name = %s,
                department = %s,
                salary = %s
            WHERE id = %s
        """, (name, department, salary, emp_id))

        conn.commit()

        print("Employee updated successfully.")

    except ValueError:
        print("Please enter a valid numeric ID and salary.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)


#5. To delete employee details

def delete_employee():

    print("\n--- DELETE EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID to delete: "))

        cur.execute("""
            SELECT id
            FROM employees_new
            WHERE id = %s
        """, (emp_id,))

        employee = cur.fetchone()

        if not employee:
            print("Employee not found.")
            return

        confirmation = input(
            "Are you sure you want to delete this employee? (yes/no): "
        )

        if confirmation.lower() == "yes":

            cur.execute("""
                DELETE FROM employees_new
                WHERE id = %s
            """, (emp_id,))

            conn.commit()

            print("Employee deleted successfully.")

        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Please enter a valid numeric employee ID.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)


# To find options of the details

while True:

    print("\n")
    print("========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")


#close database

cur.close()
conn.close()

print("DATABASE CONNECTION CLOSED")

=======

import psycopg


#database connection

conn = psycopg.connect(
    host="localhost",
    dbname="employee_db",
    user="postgres",
    password="rsc123",
    port=5432
)

cur = conn.cursor()

print("PROGRAM STARTED")


#creating table

cur.execute("""
    CREATE TABLE IF NOT EXISTS employees_new (
        id INTEGER PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        department VARCHAR(100),
        salary NUMERIC(10, 2)
    )
""")

conn.commit()


#1. To add employee

def add_employee():

    print("\n--- ADD EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID: "))

        name = input("Enter employee name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))

        cur.execute("""
            INSERT INTO employees_new (id, name, department, salary)
            VALUES (%s, %s, %s, %s)
        """, (emp_id, name, department, salary))

        conn.commit()

        print("Employee added successfully.")

    except ValueError:
        print("Please enter a valid numeric ID and salary.")

    except psycopg.errors.UniqueViolation:
        conn.rollback()
        print("This employee ID already exists.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)


#2. To veiw employee

def view_employees():

    print("\n--- ALL EMPLOYEES ---")

    cur.execute("""
        SELECT id, name, department, salary
        FROM employees_new
        ORDER BY id
    """)

    employees = cur.fetchall()

    if not employees:
        print("No employees found.")
        return

    print("\nID | Name | Department | Salary")
    print("-" * 55)

    for employee in employees:
        print(
            employee[0],
            "|",
            employee[1],
            "|",
            employee[2],
            "|",
            employee[3]
        )


#3. To search employee

def search_employee():

    print("\n--- SEARCH EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID: "))

        cur.execute("""
            SELECT id, name, department, salary
            FROM employees_new
            WHERE id = %s
        """, (emp_id,))

        employee = cur.fetchone()

        if employee:

            print("\nEmployee Found")
            print("ID:", employee[0])
            print("Name:", employee[1])
            print("Department:", employee[2])
            print("Salary:", employee[3])

        else:
            print("Employee not found.")

    except ValueError:
        print("Please enter a valid numeric employee ID.")


#4. to update details of employee

def update_employee():

    print("\n--- UPDATE EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID to update: "))

        cur.execute("""
            SELECT id
            FROM employees_new
            WHERE id = %s
        """, (emp_id,))

        employee = cur.fetchone()

        if not employee:
            print("Employee not found.")
            return

        name = input("Enter new name: ")
        department = input("Enter new department: ")
        salary = float(input("Enter new salary: "))

        cur.execute("""
            UPDATE employees_new
            SET name = %s,
                department = %s,
                salary = %s
            WHERE id = %s
        """, (name, department, salary, emp_id))

        conn.commit()

        print("Employee updated successfully.")

    except ValueError:
        print("Please enter a valid numeric ID and salary.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)


#5. To delete employee details

def delete_employee():

    print("\n--- DELETE EMPLOYEE ---")

    try:
        emp_id = int(input("Enter employee ID to delete: "))

        cur.execute("""
            SELECT id
            FROM employees_new
            WHERE id = %s
        """, (emp_id,))

        employee = cur.fetchone()

        if not employee:
            print("Employee not found.")
            return

        confirmation = input(
            "Are you sure you want to delete this employee? (yes/no): "
        )

        if confirmation.lower() == "yes":

            cur.execute("""
                DELETE FROM employees_new
                WHERE id = %s
            """, (emp_id,))

            conn.commit()

            print("Employee deleted successfully.")

        else:
            print("Delete operation cancelled.")

    except ValueError:
        print("Please enter a valid numeric employee ID.")

    except Exception as e:
        conn.rollback()
        print("Error:", e)


# To find options of the details

while True:

    print("\n")
    print("========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please enter 1 to 6.")


#close database

cur.close()
conn.close()

print("DATABASE CONNECTION CLOSED")

>>>>>>> 9e45a3feac087fc0a00924733465065efba67363
# Employee Management System - Search and validation updated