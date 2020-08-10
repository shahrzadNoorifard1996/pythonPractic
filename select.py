import psycopg2

def select():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="13931397",
            host="localhost",
            port="5432",
            database='shahrzadDb'
        )
        cursor=connection.cursor()
        pg_select = """SELECT * FROM public."Costomer" """
        cursor.execute(pg_select)

        print("selected row from book table")
        customer_records=cursor.fetchall()
        print("records of books in the table")

        for row in customer_records:
            print("id= ",row[0])
            print("CustomerName= ",row[1])
            print("CustomerFamily= ",row[2])
            print("NationalCode= ",row[3])

    except(Exception, psycopg2.Error)as error:
        print("eeeeeeeeeeeeeeeeeeeeee")
        connection = None

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("connection is now closed")

