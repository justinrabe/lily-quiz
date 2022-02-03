from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

qaTotal = {}
score = 0
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


def game_loop():
    print('Hi Lily!')
    print('This is my Valentines present to you hehe')
    print('It''s a small little question app I built of a few questions from our relationship')
    input("Press Enter to start the quiz!!")
    correct = ''
    for question in qaTotal:
        print(question)
        for answer in qaTotal[question]:
            for l in answer:
                print(l) 
                if answer[l] == 1:
                    correct = l
        ##print(*qaTotal[question], sep = "\n")
        guess = input('Enter your answer: ')
        if guess == correct:
            print ("Correct!!")
            score = score + 1
            input('Press Enter for next question')
        else:
            print ("Wrong xD")
            input('Press Enter for next question')
    print("Score = ", score)

if __name__ == '__main__':
    fetch_sql()
    game_loop()
    

