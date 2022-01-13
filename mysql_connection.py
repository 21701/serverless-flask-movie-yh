import mysql.connector

def get_connection():
    connection =  mysql.connector.connect(
        host = 'yh-db.c7guy9txcxzu.ap-northeast-2.rds.amazonaws.com',
        database = 'Movie',
        user = 'movie_user',
        password = '4444'
    )
    return connection