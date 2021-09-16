import psycopg2

def connect(database_name):
    return psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database=database_name
                                  )