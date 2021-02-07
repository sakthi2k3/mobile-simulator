import json
from tkinter import *
from difflib import *

from tkinter import messagebox
data=json.load(open("data.json"))
root=Tk()
root.title("dict")

app_height=600
app_width=630

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)


root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


bg=PhotoImage(file="icons/bg.png")


root.iconbitmap('icons/Dictionary-icon.ico')
global b
b=0

def get_meaning(word):

    if word in data:
         if len(data[word])>1:
             for i in data[word]:
            
                 return i 
         else:
         
              return data[word][0]


    elif word.lower() in data:
         if len(data[word.lower()])>1:
             for i in data[word.lower()]:
         
                 return i
         else:
        
             return data[word][0]


    elif word.upper() in data:
        if len(data[word.upper()])>1:
            for i in data[word.upper()]:
                 return i 
             
            else:
            
                return data[word][0]
     
    elif word.title() in data:
        if len(data[word.title()])>1:
            for i in data[word.title()]:
          
                return i
            else:
         
                return data[word][0]

    else:
      close_match=get_close_matches(word,data.keys())
      if len(close_match)>0:
          decide=messagebox.askquestion("askquestion","want closest word?")
          if decide=='yes':
              for i in data[close_match[0]]:
              
                  global b
                  b=close_match[0]
                  return i
          else:
               a="word not found"
               return a 
      else:
          a="cant find this word"
          return a 
          

          
def get_bt():
 try:   
   inputvalue=word.get()
   words=get_meaning(inputvalue)
   if b!=0:
        a.insert(END, "THE CLOSEST WORD IS : "+"'"+b+"'"+"\n")
        a.insert(END,words)
        if bt1["text"]=='search':
           bt1.configure(state=DISABLED)

   elif b==0:     
       a.insert(END,words)
       if bt1["text"]=='search':
           bt1.configure(state=DISABLED)
           a.configure(state=DISABLED)
 except:
     
     error=messagebox.showerror("error","invalid input! Try Again!")
     clr_bt()
     


      

def clr_bt():
    a.configure(state=NORMAL)
    word.delete(0,'end')
    a.delete('1.0','end')
    bt1.configure(state=NORMAL)
    
my_canvas=Canvas(root,width=630,height=600)
my_canvas.pack(fill='both',expand=True)
my_canvas.create_image(0,0,image=bg,anchor="nw")
    
text1=Label(root,text="Enter a word :",width=10,height=2,font=("Arial",10),bg='white',fg='black')
word=Entry(root,width=30,font=("Arial",15),textvariable="entry_word",bg='white',fg='black',cursor='hand2')
bt1=Button(root,text='search',width=10,height=1,font=("helvetica",10),bg='white',fg='black',command=get_bt,state=NORMAL)
a=Text(root,width=40,height=20,font=("Arial",15),cursor='dot',wrap='word')
clr_button=Button(root,text="clear_all",width=10,height=1,bg='white',fg='black',command=clr_bt)
 
c_text=my_canvas.create_window(10,25,anchor="nw",window=text1)
c_word=my_canvas.create_window(120,31,anchor="nw",window=word)
c_bt1=my_canvas.create_window(475,31,anchor="nw",window=bt1)
c_a=my_canvas.create_window(95,90,anchor="nw",window=a)
c_clr_button=my_canvas.create_window(280,560,anchor="nw",window=clr_button)


root.mainloop()
