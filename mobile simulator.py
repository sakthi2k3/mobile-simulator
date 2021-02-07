from tkinter import *
from PIL import ImageTk, Image
import time
from pathlib import *
import subprocess


root=Tk()
root.title('mobile simulator')
i1=PhotoImage(file="icons/game1.png")
i2=PhotoImage(file="icons/gallery icon.png")
i3=PhotoImage(file="icons/music.png")
i4=PhotoImage(file="icons/notepad.png")
i5=PhotoImage(file="icons/calculator icon.png")
i6=PhotoImage(file="icons/remainder2.png")
i7=PhotoImage(file="icons/Dictionary-icon.png")
i8=PhotoImage(file="icons/game2.png")
statusbar=PhotoImage(file="icons/s.png")
app_height=525
app_width=300
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)


root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


status_bar=Label(image=statusbar)

root.resizable(width=False,height=False)



a=[]

List_images=[]
entries=Path('gallery')
for entry in entries.iterdir():
        a.insert(1,entry)
for x in a:
    
    image= Image.open(x)
    
    resized=image.resize((300,525),Image.ANTIALIAS)
    final=ImageTk.PhotoImage(resized)
    List_images.append(final)



def game():
       root. withdraw()
       subprocess.call("CowBoy game\Game.py" , shell = True)
       root. deiconify()


def gallery():
        global t
        root. withdraw()
        global wall_paper
        subprocess.call("gallery app/gallery.py" , shell = True)
        my_canvas.delete(wall_paper)
        f=open("img","r")
        n=f.read()
        f.close()
        bg=List_images[int(n)]
        wall_paper=my_canvas.create_image(0,0,image=bg,anchor="nw")
        root. deiconify()

def music():
        root. withdraw()
        subprocess.call("music app\music player.py" , shell = True)
        root. deiconify()



def notepad():
        root. withdraw()
        subprocess.call("notepad app/np.py" , shell = True)
        root. deiconify()
   
    
    
def dict():
        root. withdraw()
        subprocess.call("dictinory app/dictonary.py" , shell = True)
        root. deiconify()
      

def game2():
        root. withdraw()
        subprocess.call("tetris game/tetris.py" , shell = True)
        root. deiconify()

        
def remainder():
        root. withdraw()
        subprocess.call("remainder app/remainder.py" , shell = True)
        root. deiconify()

        

def calculator():
        root. withdraw()
        subprocess.call("Calculator\Calculator.py" , shell = True)
        root. deiconify()
   
    
def clock():
        global t

        sec=time.strftime("%S")
        hour=time.strftime("%I")
        minute=time.strftime("%M")
        am_pm=time.strftime("%p")
        day=time.strftime("%a")
        date=time.strftime("%e")
        mon=time.strftime("%b")
        my_canvas.delete(t)
        t=my_canvas.create_text(153,180,fill="white",font=("ds-digital",40,"bold"),text=hour+":"+ minute +' '+am_pm)
        d=my_canvas.create_text(153,220,fill="white",font=("bold",20),text=day+","+ date +' '+mon)
        my_canvas.update()
   


 


my_canvas=Canvas(root,width=300,height=535)
my_canvas.pack(fill='both',expand=True)

wall_paper=my_canvas.create_image(0,0,image=List_images[0],anchor="nw")

b1=Button(root,image=i1,command=game,bg="dark orange",borderwidth=0)
b2=Button(root,image=i2,command=gallery,bg='dodger blue',borderwidth=0)
b3=Button(root,image=i3,command=music,bg='navy',borderwidth=0)
b4=Button(root,image=i4,command=notepad,borderwidth=0)
b5=Button(root,image=i5,command=calculator,bg='grey85',borderwidth=0)
b6=Button(root,image=i6,command=remainder,borderwidth=0)
b7=Button(root,image=i7,command=dict,bg='orangered4',borderwidth=0)
b8=Button(root,image=i8,command=game2,borderwidth=0)
b9=Button(root,image=statusbar,borderwidth=0)

t=my_canvas.create_text(65,120,fill="black",font=("bold",30),text="")

b_1=my_canvas.create_window(26,350,anchor="nw",window=b1)

b_2=my_canvas.create_window(91,350,anchor="nw",window=b2)

b_3=my_canvas.create_window(156,350,anchor="nw",window=b3)

b_4=my_canvas.create_window(221,350,anchor="nw",window=b4)

b_5=my_canvas.create_window(26,430,anchor="nw",window=b5)

b_6=my_canvas.create_window(91,430,anchor="nw",window=b6)

b_7=my_canvas.create_window(156,430,anchor="nw",window=b7)

b_8=my_canvas.create_window(221,430,anchor="nw",window=b8)

b_9=my_canvas.create_window(2,2,anchor="nw",window=b9)


status=my_canvas.create_window(221,410,anchor="nw",window=status_bar)
root.iconbitmap('icons/mobile.ico')

while True:
        try:
            clock()
        except:
               break


root.mainloop()


