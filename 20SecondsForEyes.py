import time
from tkinter import Tk,StringVar,Entry,Toplevel,Label,IntVar,Checkbutton
from winsound import Beep

try:
    TIME_TO_WAIT = 10000
    root = Tk()
    root['background']='#D6F6DD'
    root.geometry("300x160")
    root.resizable(False, False)
    root.title("20 seconds for your eyes")
    hour=StringVar()
    minute=StringVar()
    second=StringVar()
    hour.set("00")
    minute.set("00")
    second.set("10")
    hourEntry= Entry(root, width=3, font=("Arial",58,""),
    textvariable=hour)
    hourEntry.place(x=10,y=20,width=90,height=100)
    minuteEntry= Entry(root, width=4, font=("Arial",58,""),
    textvariable=minute)
    minuteEntry.place(x=105,y=20,width=90,height=100)
    secondEntry= Entry(root, width=3, font=("Arial",58,""),
    textvariable=second)
    secondEntry.place(x=200,y=20,width=90,height=100)

    v = IntVar()
    

  
    Button1 = Checkbutton(root, text = "Silent", 
                      variable = v,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = 9,
                      background="#D6F6DD")
    Button1.place(x=115,y=120)
    def start():
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        while temp >-1:
            mins,secs = divmod(temp,60)
            hours=0
            if mins >60:
                hours, mins = divmod(mins, 60)
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
            root.update()
            time.sleep(1)
            if (temp == 0):
                if(v.get() ==0):
                    Beep(2000,300)
                    newWindow = Toplevel(root) 
                    newWindow.title("Message")
                    newWindow.geometry("360x80")
                    newWindow.resizable(False, False)
                    Label(newWindow,text ="Look at something 20 feets away\n for 20 seconds",font=("Arial",18,"")).pack()            
                    hour.set("00")
                    minute.set("00")
                    second.set("20")
                    newWindow.after(TIME_TO_WAIT, newWindow.destroy)
                    start()
                else:
                    hour.set("00")
                    minute.set("00")
                    second.set("10")
                    start()
            if(mins==20 and secs == 1 and v.get()==0) :
                Beep(1500,100)
                Beep(2000,100)
            temp -= 1


    start()


    root.mainloop()
except:
    pass