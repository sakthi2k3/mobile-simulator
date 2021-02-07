from pathlib import *
from tkinter import *
import pygame
pygame.init()
pygame.mixer.init()
root=Tk()
root.title("MINI PLAYER")
app_height=510
app_width=580
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)
root.iconbitmap('icons/music.ico')
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

root.resizable(width=False,height=False)
name_var=StringVar()
global lisr


def music_names_load():
    entries=Path('sounds')
    global lisr
    for entry in entries.iterdir():
            lisr=str(entry)
            entrys=lisr.replace(lisr[0:7], "")
            entrys=entrys.replace(".wav", "")
            entrys=entrys.replace(".mp3", "")
            a.insert(2,entrys)

def pause_pressed():
    pygame.mixer.music.pause()
    

def unpause_pressed():
    pygame.mixer.music.unpause()
    

def stop_pressed():
         pygame.mixer.music.stop() 
         button2.configure(text="stopped!")
         button.configure(state=DISABLED)
  
            
def music_name_out(event):
             name_entry.delete(0,END)
             button.configure(text="pause")
             w=event.widget
             idx=int(w.curselection()[0])
             value=w.get(idx)
             values=lisr[0:7]+value
             
             name_entry.insert(2,value)
             button.configure(state=NORMAL)
             button2.configure(state=NORMAL)
             button2.configure(text="stop")

             
             try:
                 pygame.mixer.music.load(values+'.mp3')
                 pygame.mixer.music.play()
             except:
                 pygame.mixer.music.load(values+'.wav')
                 pygame.mixer.music.play()    
           
                 
def update_fn():
    if (button["text"]=="pause") :
        button2.configure(text="stop")
        pause_pressed()
        button2.configure(state=DISABLED)
        button.configure(text="unpause")
        button.configure(image=play)
        
    elif (button["text"]=="unpause") :
            unpause_pressed()
            button.configure(text="pause")
            button.configure(image=pause)
            button2.configure(state=NORMAL)
   
    


#img background & canvas creation

bg=PhotoImage(file="images\music1.png")
play=PhotoImage(file="images\play.png")
pause=PhotoImage(file="images\pause.png")
stop=PhotoImage(file="images\stop.png")
my_canvas=Canvas(root,width=580,height=500)
my_canvas.pack(fill='both',expand=True)
my_canvas.create_image(0,0,image=bg,anchor="nw")








#assigning the layout of mini player    


label1=Label(root,text="Music track:",font=("arieal",13))
name_entry=Entry(root,width=50,textvariable=name_var,cursor='hand2',font=("BOLD",14))
label2=Label(root,text="select the music from the below list:",font=("Helvetica",12))
lb=my_canvas.create_window(10,60,anchor="nw",window=label1)
ne=my_canvas.create_window(110,60,anchor="nw",window=name_entry)
lb2=my_canvas.create_window(7,120,anchor="nw",window=label2)
a=Listbox(root,height=10,width=30,font=("BOLD",16),selectbackground="grey",cursor='dot',selectmode='SINGLE')
lb=my_canvas.create_window(5,150,anchor="nw",window=a)
a. bind('<<ListboxSelect>>',music_name_out)


#assigning buttons

button=Button(root,image=pause,text="pause",bg='black',command=update_fn,borderwidth=0)
button2=Button(root,image=stop,text="stop",bg='black',command=stop_pressed,borderwidth=0)
b_1=my_canvas.create_window(180,410,anchor="nw",window=button)
b_2=my_canvas.create_window(80,410,anchor="nw",window=button2)




music_names_load()
root.mainloop()
