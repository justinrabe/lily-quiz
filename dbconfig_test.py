from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

qaTotal = {}
def fetch_sql():
    try:
      
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT question, name, isCorrect FROM questions q join answers a on q.id = a.questionID")

        row = cursor.fetchone()

        ##for each entry in questions, there is a list of answers. 
        while row is not None:
            if row[0] in qaTotal.keys():
                #question exists
                qaTotal[row[0]].append({row[1]: row[2]})
            else:
                #new question, insert new dictionary entry with answer as list of size 
                qaTotal[row[0]] = [{row[1]: row[2]}]
            row = cursor.fetchone()

       

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    fetch_sql()
    print(qaTotal)
    print('Hi Lily!')
    print('This is my Valentines present to you hehe')
    print('It''s a small little question app I built of a few questions from our relationship')
    input("Press Enter to start the quiz!!")
    for question in qaTotal:
        print(question)
        print(qaTotal[question])


