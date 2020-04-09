
from tkinter import *
root = Tk()
root.title('TV Show Recomendation System') 
root.geometry("900x700") 
root.config(background = "white")
w = Label(root, text ='Welcome to TV Show Analysis',bg = "white", font = "100").grid(row=0,column=1) 
#w.pack() 
Label(root, text='Enter the title of TV shows',bg = "white").grid(row=1)
e1 = Entry(root)
e1.grid(row=1, column=1)
button = Button(root, text='Search', width=25).grid(row=1,column=2)
def topTen():
    a=10
button1 = Button(root, text='Top 10 TV show',command=topTen, width=25).grid(row=2,column=0)
button2 = Button(root, text='Top 10 Movies', width=25).grid(row=2,column=1)
button3 = Button(root, text='Comapre Two Shows', width=25).grid(row=2,column=2)
button4 = Button(root, text='View Sentiment analysis data distributions', width=35).grid(row=2,column=3,padx = 5, pady = 10)
button10 = Button(root, text='Exit', width=25, command=root.destroy).grid(row=10,column=1)
#button.pack()

  
root.mainloop()
