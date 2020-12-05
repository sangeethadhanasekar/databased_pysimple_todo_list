import sqlite3
def  insert_into_tasks_table(task):
    
    sql_insert_query="""INSERT INTO tasks (taskname,complete) VALUES('%s',%s)"""%(task,0)
    execute_query(sql_insert_query)

def select_all_records():
    sql_select_query="""SELECT taskname FROM tasks WHERE complete=0"""
    result= execute_query(sql_select_query).fetchall()
    result_new=[x[0] for x in result]
    print(result_new )
    
    return  result_new 


def execute_query(sql_query):
        with sqlite3.connect("to_do.db") as conn:
              cursor=conn.cursor()
              result=cursor.execute(sql_query)
              conn.commit()
        return result
        
def mark_task_as_complete(task):
    sql_update_query="""UPDATE tasks SET complete=1 WHERE taskname='%s' AND complete=0"""%(task)
    execute_query(sql_update_query)


if __name__=="__main__" :
          select_all_records()
