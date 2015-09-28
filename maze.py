import random

fileObj = open('./mazetext.txt','w')

def newBlank(sizex,sizey):
    retarray = []
    for i in range(2*sizex+1):
        temp = []
        for j in range(2*sizey+1):
            temp.append(1) # 1 signifies an untouched place on the grid
        retarray.append(temp)
    return retarray

def recursiveBacktrack(blank):
    sizex = (len(blank)-1)/2
    sizey = (len(blank[0])-1)/2
    start = (1,1,'n') # start in upper left and make an entrance to the maze from the north
    stack=[]
    stack.append(start) # so, not quite recursion.  Done with a stack.
    while len(stack)>0:
        prob = random.random()
        if prob < .9:
            current = stack.pop()
        else:  # 10 percent of the time, pick a random spot to add a branch
            current = random.choice(stack)
            stack.remove(current)
        blank[current[0]*2-1][current[1]*2-1]=3  # 3 is a place on the actual maze
        if current[2] == 'n':  # and add to the maze the edge from one place to the other
            blank[current[0]*2-1][current[1]*2-2]=3
        elif current[2] == 'e':
            blank[current[0]*2][current[1]*2-1]=3
        elif current[2] == 's':
            blank[current[0]*2-1][current[1]*2]=3
        elif current[2] == 'w':
            blank[current[0]*2-2][current[1]*2-1]=3
        adjacent = []
        
        if current[0] > 1:
            if blank[(current[0]-1)*2-1][current[1]*2-1]<2:
                blank[(current[0]-1)*2-1][current[1]*2-1]=2
                adjacent.append((current[0]-1,current[1],'e'))
            elif blank[(current[0]-1)*2-1][current[1]*2-1]<3:
                try:
                    stack.remove((current[0]-1,current[1],'n'))
                except ValueError:
                    try:
                        stack.remove((current[0]-1,current[1],'w'))
                    except ValueError:
                        try:
                            stack.remove((current[0]-1,current[1],'s'))
                        except ValueError:
                            pass
                adjacent.append((current[0]-1,current[1],'e'))
            
        if current[1] > 1:
            if blank[current[0]*2-1][(current[1]-1)*2-1]<2:
                blank[current[0]*2-1][(current[1]-1)*2-1]=2
                adjacent.append((current[0], current[1]-1,'s'))
            elif blank[current[0]*2-1][(current[1]-1)*2-1]<3:
                try:
                    stack.remove((current[0],current[1]-1,'n'))
                except ValueError:
                    try:
                        stack.remove((current[0],current[1]-1,'w'))
                    except ValueError:
                        try:
                            stack.remove((current[0],current[1]-1,'e'))
                        except ValueError:
                            pass
                adjacent.append((current[0],current[1]-1,'s'))
            
        if current[0] < sizex:
            if blank[(current[0]+1)*2-1][current[1]*2-1]<2:
                blank[(current[0]+1)*2-1][current[1]*2-1]=2
                adjacent.append((current[0]+1, current[1],'w'))
            elif blank[(current[0]+1)*2-1][current[1]*2-1]<3:
                try:
                    stack.remove((current[0]+1,current[1],'n'))
                except ValueError:
                    try:
                        stack.remove((current[0]+1,current[1],'e'))
                    except ValueError:
                        try:
                            stack.remove((current[0]+1,current[1],'s'))
                        except ValueError:
                            pass
                adjacent.append((current[0]+1,current[1],'w'))
            
        if current[1] < sizey:
            if blank[current[0]*2-1][(current[1]+1)*2-1]<2:
                blank[current[0]*2-1][(current[1]+1)*2-1]=2
                adjacent.append((current[0], current[1]+1,'n'))
            elif blank[current[0]*2-1][(current[1]+1)*2-1]<3:
                try:
                    stack.remove((current[0],current[1]+1,'e'))
                except ValueError:
                    try:
                        stack.remove((current[0],current[1]+1,'w'))
                    except ValueError:
                        try:
                            stack.remove((current[0],current[1]+1,'s'))
                        except ValueError:
                            pass
                adjacent.append((current[0],current[1]+1,'n'))
            
        if len(adjacent) > 0:
            random.shuffle(adjacent)
            stack = stack + adjacent
    blank[len(blank)-2][len(blank[0])-1]=3
    for row in blank:
        for elem in row:
            fileObj.write(str(elem) + ',')
        fileObj.write('\n')
    fileObj.close()
    return blank
        

        
