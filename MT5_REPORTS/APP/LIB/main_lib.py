def get_sql_result(_sql):
    import pymysql
    from configparser import ConfigParser

    # Загрузка конфигурации
    DB_HOST = '89.108.65.107'
    DB_PORT = '3306'
    DB_USER = 'mt5_tass_user'
    DB_PASSWORD = 'der#18DF$=12'
    DB_NAME = 'mt5'
    result = ''
    try:
        connection = pymysql.connect(host=DB_HOST, port=int(DB_PORT), user=DB_USER, password=DB_PASSWORD,
                                     database=DB_NAME, cursorclass=pymysql.cursors.DictCursor)
        try:
            with connection.cursor() as cursor:
                cursor.execute(_sql)
                result = cursor.fetchall()
        except Exception as _ex:
            print(f"{_ex}\nSQL syntax error!")
        finally:
            connection.close()
            return result
    except Exception as _ex:
        print(f"{_ex}\nDB connection error!")

