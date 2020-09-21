import pyodbc
from db import conexion

def insert_movie(cursor: pyodbc.Cursor, title: str, years: int):
    """Funcion para insertar datos"""
    query_insert = "INSERT INTO [dbo].[testTable](title, years) VALUES(?, ?);"
    cursor.execute(query_insert, (title, years))

def select_all_movies(cursor:  pyodbc.Cursor):
    cursor.execute("SELECT * FROM [dbo].[testTable];")
    movies = cursor.fetchall()
    for movie in movies:
        print(movie)

def select_all_movie_year(cursor:  pyodbc.Cursor, year: int):
    # Crear consulta
    query = "SELECT * FROM [dbo].[testTable] WHERE years > ?;"
    # Hacer la peticion
    cursor.execute(query, (year))
    # Traemos todos los datos
    movies = cursor.fetchall()
    # imprimir los datos
    for movie in movies:
        print(movie)

def select_movie_with_like(cursor: pyodbc.Cursor, slug: str):
    query = "SELECT * FROM [dbo].[testTable] WHERE title like ?;"

    cursor.execute(query, (f"%{slug}%"))

    movies = cursor.fetchall()

    for movie in movies:
        print(movie)

def update_movie(cursor: pyodbc.Cursor, title: str, id: int):
    query = "UPDATE [dbo].[testTable] SET title = ? WHERE id = ?;"

    cursor.execute(query, (title, id))

    cursor.commit()

def delete_movie(cursor: pyodbc.Cursor, id: int):
    query = "DELETE FROM [dbo].[testTable] WHERE id = ?;"
    
    cursor.execute(query, (id))

    cursor.commit()

try:
    with conexion.cursor() as cursor:
        # Ingresar datos
        insert_movie(cursor, "Avengers: Endgame", 2019)

        # Pedir todos los datos
        ##select_all_movies(cursor)

        # Pedir datos con WHERE
        ##select_all_movie_year(cursor, 2000)

        # Pedir datos con LIKE
        ##select_movie_with_like(cursor, "endg")

        # Actualizar datos
        ##update_movie(cursor, "It(nueva)", 2)
        
        # Eliminar datos
        ##delete_movie(cursor, 2)
        
except Exception as e:
    print("Ocurrio un error en la consulta: ", e)
finally:
    conexion.close()
