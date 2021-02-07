import PySimpleGUI as sg
from tkinter import *
from tkinter import messagebox
from file_function import write,read,deleteContent

fname = 'file1.txt'
dname='file2.txt'
pname='file3.txt'
cname='file4.txt'
sg.theme('DarkGrey2')
tasknameread = read(fname)
dateread=read(dname)
priorityread=read(pname)
completedread=read(cname)
completedtask=[]
completeddate=[]
                   

task=[]
date=[]
priority=[]
msg=''


def prioritise():
    dict1={"very_imp":3,"imp":2,"later":1}
    p_task = read(fname)
    p_date=read(dname)
    p_priority=read(pname)
    
    for i in range(0,len(p_task)):
        for j in range(0,len(p_task)):
            if i!=j:
                if dict1[p_priority[i]]>dict1[p_priority[j]]:
                    (p_priority[i],p_priority[j])=(p_priority[j],p_priority[i])
                    (p_date[i],p_date[j])=(p_date[j],p_date[i])
                    (p_task[i],p_task[j])= (p_task[j],p_task[i])
    window.FindElement('list_box').Update(values=p_task)
    window.FindElement('date_box').Update(values=p_date)
    
                    

            
def open_work(values):
  try:

   

   if tasknameread[0]!="":
      for i in tasknameread:
        task.append(i)  
        window.FindElement('list_box').Update(values=task)
      for j in dateread:
        date.append(j)
        window.FindElement('date_box').Update(values=date)
      for k in priorityread:
           priority.append(k)
 
      window.FindElement('open_work').Update("opened")
      window.FindElement('open_work').Update(disabled=True)
      prioritise()
      

  except:
         messagebox.showerror("Error","can't open an empty file:")

         window.FindElement('open_work').Update(disabled=True)




def add_work(values):
   try: 
     if values['taskname']!="":
        task.append(values['taskname'])
        date.append(values['dated'])
        priority.append(values['drop_down'])
        
        window.FindElement('list_box').Update(values=task)
        window.FindElement('date_box').Update(values=date)
        window.FindElement('add_work').Update("Add")
        window.FindElement('taskname').Update('')  
        window.FindElement('dated').Update('')
        window.FindElement('drop_down').Update('')

        write(fname, task)
        write(dname,date)
        write(pname,priority)
        prioritise()
    

   except:    
        messagebox.showerror("Error","Enter valid input")



def edit_work(values):
        edit_task=values["list_box"][0]
        edit_date=date[task.index(edit_task)]
        edit_priority=priority[task.index(edit_task)]
        task.remove(edit_task)
        date.remove(edit_date)
        priority.remove(edit_priority)
        

        window.FindElement('list_box').Update(values=task)
        window.FindElement('date_box').Update(values=date)

        window.FindElement('taskname').Update(value=edit_task)
        window.FindElement('dated').Update(value=edit_date)
        window.FindElement('drop_down').Update(value=edit_priority)

        window.FindElement('add_work').Update("Save")
        write(fname, task)
        write(dname,date)
        write(pname,priority)
        prioritise()
        
     

def delete_work(values):
        delete_task=values["list_box"][0]
        delete_date=date[task.index(delete_task)]
        delete_priority=priority[task.index(delete_task)]

                

        task.remove(delete_task)
        date.remove(delete_date)
        priority.remove(delete_priority)

        window.FindElement('list_box').Update(values=task)
        window.FindElement('date_box').Update(values=date)
        write(fname, task)
        write(dname,date)
        write(pname,priority)
        prioritise() 
  


def complete_work(values):
           comp_task=values["list_box"][0]
           comp_date=date[task.index(comp_task)]
           comp_priority=priority[task.index(comp_task)]

           completedtask.append(comp_task)
           completeddate.append(comp_date)
          
           task.remove(comp_task)
           date.remove(comp_date)
           priority.remove(comp_priority)
           window.FindElement('list_box').Update(values=task)
           window.FindElement('date_box').Update(values=date)
           write(fname, task)
           write(dname,date)
           write(pname,priority)
           

           write(cname,completedtask)
           prioritise() 
        

           


    

rowtask=[]                     

layout=[
    [sg.Text("Enter the task:",font=("Arial",14)),sg.InputText("",font=("Arial",14), size=(20,1),key="taskname"),
     sg.Button("Open",font=("Arial",12),key="open_work")],
     [sg.Button("Add",font=("Arial",12),key="add_work"),
      sg.Button("Edit",font=("Arial",12),key="edit_work"),
     sg.Button("Delete",font=("Arial",12),key="delete_work"), sg.Button("Completed",font=("Arial",12),key="complete_work")],
      [sg.Text("select the priority:",font=("Arial",14)),sg.InputCombo(['very_imp','imp','later'],size=(9,0),key="drop_down"),sg.Text("deadline date:",font=("Arial",12)),sg.InputText("",font=("Arial",12),size=(9,1),key="dated")],
     [sg.Listbox(values=[],font=("Arial",14),size=(30,10),select_mode='single',change_submits=True,key="list_box"),     
    sg.Listbox(values=[],font=("Arial",14),size=(10,10),select_mode='single',change_submits=True,key="date_box")],
    
    [sg.Button("Show completed tasks",font=("Arial",12),key="show_work")]]     
                                                               
window=sg.Window('Reminder',layout,finalize=True)


while True:
    try:

   
        event,values=window.Read()
        if event == None or event==window.close:
           window.Close()
           break
        elif event=="open_work":
            open_work(values)
            
            
        elif event=="add_work":
                add_work(values)
            
            
        elif event=="edit_work":
              edit_work(values)
            
           

                
        elif event=="delete_work":
            delete_work(values)
                           
        elif event=="complete_work":
            complete_work(values)
        elif event=="show_work":
             msg=read(cname)

             messagebox.showinfo("completed tasks",msg)  
     

    except:
            messagebox.showerror("Error","INVALID INPUT")

        
window.close()
