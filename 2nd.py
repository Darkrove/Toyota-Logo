from tkinter import *
toyota=Tk()
c=Canvas(toyota,bg="white",height=500,width=600)
oval=c.create_oval(150,100,450,300,width=15)
oval=c.create_oval(200,100,400,200,width=15)
oval=c.create_oval(270,100,330,300,width=15)
text=c.create_text(150,370,anchor=W,font=("Impact",74),text="TOYOTA",fill="red")
c.pack()
toyota.mainloop()