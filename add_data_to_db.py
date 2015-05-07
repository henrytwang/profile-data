def insert_data(cursor, json_data):
    sql_add_name = "INSERT INTO Employees (Name) VALUES (\'{0}\')"
    sql_add_school = "INSERT INTO Schools (SchoolName) VALUES (\'{0}\')"
    sql_add_company = "INSERT INTO Companies (CompanyName) VALUES (\'{0}\')"
    sql_add_employee_school = "INSERT INTO Employee_Schools (EmployeeID, SchoolID) VALUES ({0},{1})"
    sql_add_employee_company = "INSERT INTO Employee_Companies (EmployeeID, CompanyID) VALUES ({0}, {1})"

    cursor.execute(sql_add_name.format(json_data["name"]))
    cursor.execute("SET @employee_id = LAST_INSERT_ID()")

    for school_name in json_data["schools"]:
        cursor.execute(sql_add_school.format(school_name))
        cursor.execute("SET @school_id = LAST_INSERT_ID()")
        cursor.execute(sql_add_employee_school.format("@employee_id", "@school_id"))

    for company_name in json_data["companies"]:
        cursor.execute(sql_add_company.format(company_name))
        cursor.execute("SET @company_id = LAST_INSERT_ID()")
        cursor.execute(sql_add_employee_company.format("@employee_id", "@company_id"))
