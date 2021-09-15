import psycopg2
def connect():
    return psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="localhost",
                                  port="5432",
                                  database="olap_day_2_assignement"
                                  )


    