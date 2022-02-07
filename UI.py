import tkinter as tk

class Grid(tk.Tk):
    def __init__(self,path,start,end,grid_max,blocked_cell,hg):#blocked_cells_list
        tk.Tk.__init__(self)
        #self.canvas = tk.Canvas(self, width=1000, height=1000, borderwidth=0, highlightthickness=0)
        self.canvas = tk.Canvas(self, width=(grid_max[0] * 12) + 12, height=(grid_max[1] * 12) + 12, borderwidth=0, highlightthickness=1)
        self.canvas.pack(side="top", fill="both", expand="true")
        self.rows = grid_max[1]
        self.columns = grid_max[0]
        self.cells = {}
        self.dots = {}
        self.start = start
        self.end = end
        self.path = path
        self.canvas.bind("<Configure>", self.draw_grid(blocked_cell,hg))
        self.status = tk.Label(self, anchor="w")
        self.status.pack(side="bottom", fill="x")
       

    def draw_grid(self, blocked_cell,hg,event=None):
        self.canvas.delete("r")
        w = 12
        h = 12
        for column in range(1,self.columns+2):
            for row in range(1,self.rows+2):
                x1 = column*w
                y1 = row * h
                x2 = x1 + w
                y2 = y1 + h
                if not row == self.rows+1 and not column == self.columns+1:
                    cell = self.canvas.create_rectangle(x1,y1,x2,y2, fill="white", tags="r")
                #cell.grid(row=row, column=column)
                dot = self.canvas.create_oval(x1-1,y1-1,x1+1,y1+1,fill='black')
                self.cells[(row,column)] = cell
                self.canvas.tag_bind(dot, "<Button-1>", lambda event, row=row, column=column: self.btn(column, row,hg))
                self.dots[row,column] = dot
        for b in range(len(blocked_cell)):
            cell = self.cells[blocked_cell[b]]
            self.canvas.itemconfigure(cell, fill='black')
        #l = [(1,1),(2,2),(2,2),(3,3)]
        #self.canvas.create_line(10,10,20,20,fill='red',width=2)
        #cells[3,4].configure(background="red")
        for c in range(len(self.path)-1):
            self.canvas.create_line(self.path[c][0]*12,self.path[c][1]*12,self.path[c+1][0]*12,self.path[c+1][1]*12,fill='red',width=2)
        for c in range(len(self.path)):
            path_dot = self.canvas.create_oval(self.path[c][0]*12-3,self.path[c][1]*12-3,self.path[c][0]*12+3,self.path[c][1]*12+3,fill='yellow')
            self.canvas.tag_bind(path_dot, "<Button-1>", lambda event, y = self.path[c][1], x=self.path[c][0]: self.btn(x, y,hg))
        
        start_dot = self.canvas.create_oval(self.start[0]*12-4,self.start[1]*12-4,self.start[0]*12+4,self.start[1]*12+4,fill='Green')
        self.canvas.tag_bind(start_dot, "<Button-1>", lambda event, y = self.start[1], x=self.start[0]: self.btn(x, y,hg))
        end_dot = self.canvas.create_oval(self.end[0]*12-4,self.end[1]*12-4,self.end[0]*12+4,self.end[1]*12+4,fill='blue')
        self.canvas.tag_bind(end_dot, "<Button-1>", lambda event, y = self.end[1], x=self.end[0]: self.btn(x, y,hg))
    def btn(self, x, y,hg):
        if((x,y) in hg):
            self.status.configure(text="vertex:(%s,%s)-> h: %s || g: %s || f: %s" % (x,y,hg[(x,y)][0],hg[(x,y)][1],hg[(x,y)][0] + hg[(x,y)][1]))

if __name__ == "__main__":
    start = (20,30)
    end = (10,2)
    path = [(1,1),(2,2),(3,3),(10,2),(20,30),(20,20)]
    blocked_cell = [(3,4),(7,8),(1,1)]
    hg = {(2,2):(4,5),(3,3):(6,7),(10,2):(3,5),(20,30):(10,5),(20,20):(1,7)}
    Grid(path,start,end,(100,50),blocked_cell,hg).mainloop()
