from mysql.connector import connect, Error

def mysql_out(db_query):
    database=[]
    try:
        with connect(
            host="shishkovniki.ru",
            #host
            user="root",
            password="0000",
            database="game"
        ) as connection:
            with connection.cursor() as cursor: #statement build java
                cursor.execute(db_query)
                for db in cursor:
                    database.append(db)
                # или вместо for
                # connection.commit()
    except Error as e:
        database.append("Не удалось выполнить соединение")
    return database

