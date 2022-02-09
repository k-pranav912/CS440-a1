README

This program runs search algorithms on a grid. 

The program uses tkinter to display a GUI, so an appropriate compabitable software is needed to run this program.

At any point the user may enter Q to quit.

The input is a text file of format specified in the project description. The program first takes an input for a path to the grid you want to search. 
There are sample files in the folder Grids. Grid0.txt is an example of a grid with no path between the start and goal, whereas Grids1.txt to Grids50.txt are randomly generated grids of size 100x50 with 10% blocked cells and contain a path between the start and goal (they were prechecked for blocked paths). 
The user is reccomended to add testing grids to this folder to keep it organized, making the input "[Path to Folder]/Grids/[Grid Name].txt" for the file path

The program then takes a single capital character to run a search or change files. 
    F: Allows the user to change the file for the grid
    A: Runs A* search on the grid, then displays the resulting path on a GUI
    T: Runs Theta* search on the grid, then displays the resulting path on a GUI
    
GUI: 
In order to display the h, g, and f values of verticies that have been searched, the user may press on the vertex itself, and the values will display at the bottom of the screen. If the vertex has not been searched, the text will not be updated.
In order to close the GUI, simply click the X, and the terminal will allow for the next input once it has been closed.
