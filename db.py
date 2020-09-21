import pyodbc

host_db = "localhost"
name_db = "Test"
user_db = "Sa"
pass_db = "Password123"

try:
    conexion = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + host_db + ";DATABASE=" + name_db + ";UID=" + user_db + ";PWD=" + pass_db)
except Exception as e:
    print("Ha ocurrido un error al conectarce en la base de datos: ", e)