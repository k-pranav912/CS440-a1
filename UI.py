import tkinter as tk

class Grid(tk.Tk):
    def __init__(self,path,start,end,grid_max,blocked_cell,hg):#blocked_cells_list
        tk.Tk.__init__(self)
        #self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas = tk.Canvas(self, width=(grid_max[0] * 10) + 10, height=(grid_max[1] * 10) + 10, borderwidth=0, highlightthickness=1)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = grid_max[1]
        self.columns = grid_max[0]
        self.cells = {}
        self.canvas.bind("<Configure>", self.draw_grid(blocked_cell,hg))
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")
       

    def draw_grid(self, blocked_cell,hg,event=None):
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
                #cell.grid(row=row, column=column)
                dot = self.canvas.create_oval(x1-2.5,y1-2.5,x1+2.5,y1+2.5,fill='blue')
                self.cells[(row,column)] = cell
                self.canvas.tag_bind(dot, "<Button-1>", lambda event, row=row, column=column: self.btn(row, column,hg))
                #self.dots[row,column] = dot
        for b in range(len(blocked_cell)):
            cell = self.cells[blocked_cell[b]]
            self.canvas.itemconfigure(cell, fill='bLACK')
        #l = [(1,1),(2,2),(2,2),(3,3)]
        #self.canvas.create_line(10,10,20,20,fill='red',width=2)
        #cells[3,4].configure(background="red")
        for c in range(len(path)-1):
            self.canvas.create_line(path[c][0]*10,path[c][1]*10,path[c+1][0]*10,path[c+1][1]*10,fill='red',width=2)
    def btn(self, x, y,hg):
        if((x,y) in hg):
            self.status.configure(text="vertex:(%s,%s) h value: %s  g value: %s  f value : %s" % (x,y,hg[(x,y)][0],hg[(x,y)][1],hg[(x,y)][0] + hg[(x,y)][1]))

if __name__ == "__main__":
    start = (2,2)
    end = (3,3)
    path = [(1,1),(2,2),(2,2),(3,3)]
    blocked_cell = [(3,4),(7,8),(1,1)]
    hg = {(2,2):(4,5),(3,3):(6,7)}
    Grid(path,start,end,(100,50),blocked_cell,hg).mainloop()
