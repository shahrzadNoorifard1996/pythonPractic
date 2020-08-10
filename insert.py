import psycopg2

def insert(CustomerName,CustomerFamily,NationalCode):
     try:
         connection=psycopg2.connect(
             user="postgres",
             password="13931397",
             host="localhost",
             port="5432",
             database='shahrzadDb'
         )
         cursor=connection.cursor()
         pg_insert="""INSERT INTO public."Customer"( "CustomerName","CustomerFamily",
         "NationalCode") VAlUES (%s,%s,%s)"""

         inserted_Values=(
             CustomerName,
             CustomerFamily,
             NationalCode,
         )

         cursor.execute(pg_insert,inserted_Values)
         connection.commit()
         count=cursor.rowcount
         print("sucessfully inserted",count,"records")

     except(Exception,psycopg2.Error)as error:
         print("oooooooooooooo")
         connection=None

     finally:
         if connection != None:
             cursor.close()
             connection.close()
             print("connection is now closed")


