                           
import PySimpleGUI as sg
from sqlcommandd import insert_into_tasks_table,select_all_records,mark_task_as_complete
tasks=select_all_records()
layout=[
    [sg.Text('todolist',font=('Arial',14))],
    [sg.InputText('',size=(40,2),font=('Arial',14),key='todo_item',enable_events=True),
     sg.Button(button_text='ADD',bind_return_key=True,font=('Arial',14),key='add_save')],
    [sg.Listbox(values=tasks,size=(40,10),font=('Arial',14),key='items',enable_events=True),
     sg.Button(button_text='DELETE',font=('Arial',14),key='delete'),
     sg.Button(button_text='EDIT',font=('Arial',14),key='edit')],
    ]

def add_tasks(values):
    print(values['todo_item'])
    if window.FindElement('add_save').GetText()=='Add':
        insert_into_tasks_table(values['todo_item'])
    update_ui()    



def delete_tasks(values):
    mark_task_as_complete(values['tasks'][0])
    update_ui()
    
def update_ui():
    tasks=select_all_records()
    window.FindElement('items').Update(values=tasks)
    window.FindElement('todo_item').Update(value="")
    


if __name__=='__main__' :
    window=sg.Window('TODOlist app',layout)
    while True:
        event,values=window.Read()
        if event==sg.WINDOW_CLOSED:
            break
        if event=="add_save":
           add_tasks(values)
        elif event==" delete":
           delete_tasks(values)
     #   elif event== " edit":
    #        edit_tasks(values)''' 
    
