import psycopg2

def update(CustomerName,NationalCode):
     try:
         connection=psycopg2.connect(
             user="postgres",
             password="13931397",
             host="localhost",
             port="5432",
             database='shahrzadDb'
         )
         cursor=connection.cursor()

         print("customer table befor updating")
         pg_select="""SELECT * FROM public."Costomer" WHERE "NationalCode"=%s"""
         cursor.execute(pg_select,(NationalCode, ))
         book_record=cursor.fetchone()
         print(book_record)

         pg_update="""Update public."Customer" set "CustomerName"=%s where "NationalCode"=%s"""
         cursor.execute(pg_update, (CustomerName,NationalCode,))
         connection.commit()
         count=cursor.rowcount
         print(count,"successfully updated")

         print("customer table after updating")
         pg_select = """SELECT * FROM public."Costomer" WHERE "NationalCode"=%s"""
         cursor.execute(pg_select, (NationalCode,))
         book_record = cursor.fetchone()
         print(book_record)


     except(Exception,psycopg2.Error)as error:
         print("kkkkkkkkkkeeeeeeee")
         connection=None

     finally:
         if connection !=None:
             cursor.close()
             connection.close()
             print("connection is now closed")


