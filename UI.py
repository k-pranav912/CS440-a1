import tkinter as tk

class Grid(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas = tk.Canvas(self, width=1010, height=510, borderwidth=0, highlightthickness=1)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = 50
        self.columns = 100
        self.cells = {}
        self.canvas.bind("<Configure>", self.draw_grid)

    def draw_grid(self, event=None):
        self.canvas.delete("r")
        w = 10
        h = 10
        for column in range(1,self.columns+1):
            for row in range(1,self.rows+1):
                x1 = column*w
                y1 = row * h
                x2 = x1 + w
                y2 = y1 + h
                cell = self.canvas.create_rectangle(x1,y1,x2,y2, fill="yellow", tags="r")
                dot = self.canvas.create_oval(x1-1.5,y1-1.5,x1+1.5,y1+1.5,fill='blue')
                self.cells[row,column] = cell
                #self.dots[row,column] = dot
               
        l = [(10,10),(20,20),(20,20),(30,30)]
        #self.canvas.create_line(10,10,20,20,fill='red',width=2)
        for c in range(len(l)):
            self.canvas.create_line(l[c],l[c+1],fill='red',width=2)

if __name__ == "__main__":
    Grid().mainloop()
