#Implemented on Jupyter
from tkinter import *
window = Tk()
#window.geometry('100x100')
#window.title('Grid')
#canvas = Canvas(window,width = 100,height = 100,background = 'white')
#canvas.grid(row = 0,column=0)
cells = {}
for row in range(3):
    for column in range(4):
        cell = Canvas(window, bg='white', highlightbackground="black",
                     highlightcolor="black", highlightthickness=1,
                     width=100, height=100)
        
        cell.grid(row=row, column=column)
        cells[(row, column)] = cell
        
        cell.create_line(0,0,100,100,fill='red')#,width=30) # Use this with different width and color to show the shortest path
        #cell.create_line(0,0,1,1,fill='black')
#cells[(3,4)].configure(background="red") #To color the Blocked cells
window.mainloop()
