from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config


def query_with_fetchone():
    try:
        qaTotal = {}
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT question, name FROM questions q join answers a on q.id = a.questionID")

        row = cursor.fetchone()

        while row is not None:
            if row[0] in qaTotal.keys():
                #question exists
                qaTotal[row[0]].append(row[1])
            else:
                #new question, insert new dictionary entry with answer as list of size 1
                qaTotal[row[0]] = [row[1]]
            row = cursor.fetchone()
        print(qaTotal)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    query_with_fetchone()