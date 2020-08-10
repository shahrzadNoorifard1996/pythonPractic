import psycopg2

def delete(NationalCode):
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="13931397",
            host="localhost",
            port="5432",
            database='shahrzadDb'
        )
        cursor = connection.cursor()
        pg_delete = """DELETE from public."Customer" where "NationalCode"=%s"""
        cursor.execute(pg_delete,(NationalCode))
        connection.commit()
        count = cursor.rowcount
        print("sucessfully deleted", count, "rows")

    except(Exception, psycopg2.Error)as error:
        print("eeaaaaaaaaaaaaaaaaa")
        connection = None

    finally:
        if connection != None:
            cursor.close()
            connection.close()
            print("connection is now closed")

