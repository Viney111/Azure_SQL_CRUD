import pymssql
import os
print("Welcome to Azure SQL Connection in Python")

server = os.getenv('server_azureSql')
db = os.getenv('database_azureSql')
username = os.getenv('username_azureSql')
password = os.getenv('password_azureSql')

# Connection String for connecting Azure SQL
try:
    connection_str = pymssql.connect(server=server, user=username, password=password, database=db)
    mycursor = connection_str.cursor()
    print("Connection is establshed")
except Exception as ex:
    print(ex)


def dict_input_from_Console():
    """
        Description: Function is to taking input from Console and storing in Dictionary for Sql.
        Parameter: None
        Return: Just returns input data in form of Dictionary
    """  
    try:
        employee_name = input("Enter Employee Name: ")
        gender = input("Enter gender: ")
        salary = int(input( "Enter salary: "))
        date = input("Enter Start Date in format (yyyy/mm/dd): ")
    except Exception as ex:
        print(ex)
    else:
        return {'employee_name':employee_name,'gender':gender,'salary':salary,'date':date}


def adding_Console_data_in_Db():
    """
        Description: Function is to enter data in Db from Console
        Parameter: None
        Return: Just prints a successful message.
    """
    try:
        input_dict = dict_input_from_Console()
        mycursor.execute(f"INSERT INTO tbl_employee_Payroll (EmployeeName,Gender,Salary,StartDate) VALUES ('{input_dict['employee_name']}','{input_dict['gender']}',{input_dict['salary']},'{input_dict['date']}')")
    except Exception as ex:
        print(ex)
    else:
        connection_str.commit()
        print("Data Added Successfully")


def show_data():
    try:
        sql_query = "SELECT * FROM tbl_employee_Payroll"
        mycursor.execute(sql_query)
        data = mycursor.fetchall()
        for i in data:
            print(i)
    except Exception as ex:
        print(ex)
    

def create_table():
    """
        Description: Function is to create a new table
        Parameter: None 
        Return: Just prints a successful message
    """
    try:
        sql_query = "CREATE TABLE tbl_employee_Payroll(EmployeeId INT IDENTITY(1,1),EmployeeName VARCHAR(30) NOT NULL,Gender CHAR(1),Salary MONEY,StartDate DATETIME NOT NULL);"
        mycursor.execute(sql_query)
    except Exception as ex:
        print(ex)
    else:
        connection_str.commit()
        print("Table is created Successfully in Azure SQL")


def adding_hardcoded_data__in_tbl():
    """
        Description: Function is to add data into the tbl_employee_Payroll
        Parameter: None
        Return: Just prints a successful message
    """
    try:
        sql_query = "INSERT INTO tbl_employee_Payroll (EmployeeName,Gender,Salary,StartDate) VALUES ('Viney','M',200000,'2022/7/17'),('Ishita','F',300000,'2022/8/10');"
        mycursor.execute(sql_query)
    except Exception as ex:
        print(ex)
    else:
        connection_str.commit()
        print("Data Added Successfully in Azure SQL")       


if __name__=="__main__":
    # create_table()
    # adding_hardcoded_data__in_tbl()
    adding_Console_data_in_Db()
    show_data() 
    connection_str.close()