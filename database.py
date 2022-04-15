import sqlite3

def create_connection():
    connection = sqlite3.connect("memory.db")
    return connection

def get_qna():
    con = create_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM qna")

    return cur.fetchall()

def get_answer_from_memory(question):
    rows = get_qna()

    query = ""
    for row in rows:
        if row[0].lower() in question.lower():
            query = row[1]
            break
    return query


#print(get_answer_from_memory("whats your name"))