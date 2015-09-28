# display the maze
import maze
from Tkinter import *

root = Tk()
wid = 700
hei = 700
w = Canvas(root, scrollregion=(0,0,wid,hei), bg="white", width=wid, height=hei)
w.pack()

bl = maze.newBlank(int(wid/6)-1,int(hei/6)-1)
rbmaze = maze.recursiveBacktrack(bl)
print('xdim = ',len(rbmaze),'  ydim = ',len(rbmaze[0]))

for i in range(len(rbmaze)):
    for j in range(len(rbmaze[0])):
        if rbmaze[i][j] == 1:
            w.create_rectangle(3*i,3*j,3*(i+1),3*(j+1),fill='black',width=0)

root.mainloop()
