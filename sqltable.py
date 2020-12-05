import sqlite3

def create_table():
    sql_query="""
           CREATE TABLE tasks(
           id INTEGER PRIMARY KEY,
           taskname TEXT,
           complete BOOLEAN);
           """
        
    with sqlite3.connect("to_do.db") as conn:
        cursor=conn.cursor()
        cursor.execute(sql_query)
        conn.commit()
        
if __name__=="__main__":
    create_table()
        
