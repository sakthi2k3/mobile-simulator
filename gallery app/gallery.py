from tkinter import *
from PIL import ImageTk, Image
from pathlib import *


root = Tk()
root.resizable(width=False,height=False)
wp=0  
root.title("gallery") 
i=0  

app_height=680
app_width=655
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2)-(app_width/2)
y=(screen_height/2)-(app_height/2)


root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

a=[]
images=[]
List_images=[]
entries=Path('gallery')
for entry in entries.iterdir():
        a.insert(1,entry)
for x in a:
    
    image= Image.open(x)
    images.append(image)
    resized=image.resize((650,650),Image.ANTIALIAS)
    final=ImageTk.PhotoImage(resized)
    List_images.append(final)
    
          





  
label = Label(image=List_images[0]) 
  

label.grid(row=1, column=0, columnspan=3) 
  
  
def wallpaper():
        global i
        global wp
        wp=i
        
        
        
        
def forward(img_no): 
  
    global i
    global label 
    global button_forward 
    global button_back 
    i+=1
    label.grid_forget() 
  
  
    label = Label(image=List_images[img_no-1]) 
  
    button_forward = Button(root, text=">>",bg='white',fg='black', command=lambda: forward(img_no+1))
    button_exit = Button(root, text="set wallpaper",bg='white',fg='black',command=wallpaper) 
    button_back = Button(root, text="<<",bg='white',fg='black', command=lambda: back(img_no-1))

    

    if img_no == len(List_images): 
        button_forward = Button(root, text=">>", state=DISABLED) 
  
    label.grid(row=1, column=0, columnspan=3) 
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1) 
    button_forward.grid(row=5, column=2) 
  
  
def back(img_no): 
  
    global i
    global label 
    global button_forward 
    global button_back 
    global button_exit
    i-=1
    label.grid_forget() 
  

    label = Label(image=List_images[img_no - 1]) 
    
    button_forward = Button(root, text=">>",bg='white',fg='black', command=lambda: forward(img_no + 1))
    button_exit = Button(root, text="set wallpaper",bg='white',fg='black',command=wallpaper) 
    button_back = Button(root, text="<<",bg='white',fg='black', command=lambda: back(img_no - 1))
    

    if img_no == 1: 
        button_back = Button(root, text="<<", state=DISABLED) 
    label.grid(row=1, column=0, columnspan=3)
    button_back.grid(row=5, column=0)
    button_exit.grid(row=5, column=1) 
    button_forward.grid(row=5, column=2) 
  
  




button_back = Button(root, text="<<",command=back,bg='white',fg='black', state=DISABLED) 
  
button_exit = Button(root, text="set wallpaper",bg='white',fg='black',command=wallpaper) 
  
button_forward = Button(root, text=">>",bg='white',fg='black',command=lambda: forward(2)) 
  

button_back.grid(row=5, column=0) 
button_exit.grid(row=5, column=1) 
button_forward.grid(row=5, column=2) 

   
root.iconbitmap('icons/gallery icon.ico')

root.mainloop()


f=open("img","w")
f.write(str(wp))
f.close()
       
      
       
        


      
