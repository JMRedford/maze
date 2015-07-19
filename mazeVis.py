import maze
from tkinter import *

root = Tk()
wid = 800
hei = 800
w = Canvas(root, scrollregion=(0,0,wid,hei), bg="white", width=wid, height=hei)
w.pack()

bl = maze.newBlank(int(wid/48)-1,int(hei/48)-1)
rbmaze = maze.recursiveBacktrack(bl)
print('xdim = ',len(rbmaze),'  ydim = ',len(rbmaze[0]))

for i in range(len(rbmaze)):
    for j in range(len(rbmaze[0])):
        if rbmaze[i][j] == 1:
            w.create_rectangle(24*i,24*j,24*(i+1),24*(j+1),fill='black',width=0)

root.mainloop()
