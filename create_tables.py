def create_tables(cursor):
    sql_create_employees_table = """CREATE TABLE Employees
    (
        EmployeeID int NOT NULL AUTO_INCREMENT,
        Name varchar(255) NOT NULL,
        PRIMARY KEY (EmployeeID)
    );"""

    sql_create_companies_table = """CREATE TABLE Companies
    (
        CompanyID int NOT NULL AUTO_INCREMENT,
        CompanyName varchar(255) NOT NULL,
        PRIMARY KEY (CompanyID)
    );"""

    sql_create_schools_table = """CREATE TABLE Schools
    (
        SchoolID int NOT NULL AUTO_INCREMENT,
        SchoolName varchar(255) NOT NULL,
        PRIMARY KEY (SchoolID)
    );"""

    sql_create_employee_schools_table = """CREATE TABLE Employee_Schools
    (
        EmployeeID int NOT NULL,
        SchoolID int NOT NULL
    );"""

    sql_create_employee_companies_table = """CREATE TABLE Employee_Companies
    (
        EmployeeID int NOT NULL,
        CompanyID int NOT NULL
    );"""

    cursor.execute(sql_create_employees_table)
    cursor.execute(sql_create_companies_table)
    cursor.execute(sql_create_schools_table)
    cursor.execute(sql_create_employee_schools_table)
    cursor.execute(sql_create_employee_companies_table)
