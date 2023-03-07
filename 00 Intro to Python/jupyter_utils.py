import numpy as np
from matplotlib import pyplot as plt
#path=np.load('path.npy')


# mystery variables for 02_conditionals
test_var = 0
mystery_number = 4
x = 1
team = "49ers"
team2 = "Rams"

mystery_number_b = 8

def show_player_olld(map,pos, direc=[0,1], show_direc=False, has_ball=False):
    xpos = pos[0]#+4
    ypos = pos[1]#+2
    [n,m]=map.shape
    map2 = np.zeros((n,m))
    map2[ypos,xpos]=8
    if has_ball:
        map[ypos,ypos]=10
    nose = (ypos+direc[0],xpos+direc[1])
    dorsal = (ypos+direc[1], xpos-direc[0])
    ventral = (ypos-direc[1],xpos+direc[0])
    if show_direc:
        if (nose[0]<n and nose[1]<m):
            if map[nose]==1:
                map2[nose]=2
            elif map[nose]==0:
                map2[nose]=0
            else:
                map2[nose]=6    
        if (dorsal[0]<n and dorsal[1]<m):
            if map[dorsal]==1:
                map2[dorsal]=2
            else:
                map2[dorsal]=6
        if (ventral[0]<n and ventral[1]<m):
            if map[ventral]==1:
                map2[ventral]=2
            else:
                map2[ventral]=6
        
    plt.imshow(np.flipud(map+map2), vmin = 0, vmax=10)
    plt.axis("off")
    
def show_player_2(map, pos, direc=[1,0], show_direc=False, has_ball=False):
    xpos = pos[0]#+4
    ypos = pos[1]#+2
    direc = [direc[1],direc[0]]
    [n,m]=map.shape
    map2 = np.zeros((n,m))
    map2[ypos,xpos]=8
    if has_ball:
        map[ypos,ypos]=10
    nose = (ypos+direc[0],xpos+direc[1])
    dorsal = (ypos+direc[1], xpos-direc[0])
    ventral = (ypos-direc[1],xpos+direc[0])
    if show_direc:
        if (nose[0]<n and nose[1]<m):
            if map[nose]==1:
                map2[nose]=2
            elif map[nose]==0:
                map2[nose]=0
            else:
                map2[nose]=6    
        if (dorsal[0]<n and dorsal[1]<m):
            if map[dorsal]==1:
                map2[dorsal]=2
            else:
                map2[dorsal]=6
        if (ventral[0]<n and ventral[1]<m):
            if map[ventral]==1:
                map2[ventral]=2
            else:
                map2[ventral]=6
        
    plt.imshow(np.flipud(map+map2), vmin = 0, vmax=10)
    plt.axis("off")
    plt.show()
    
    
def show_player(map, loc, direc=[0,1], show_direc=True):
    xpos = loc[1]*3+1
    ypos = loc[0]*3+1
    #direc = [direc[1],direc[0]]
    [n,m]=map.shape
    map2 = np.zeros((3*n,3*m))
    for ii in range(3*n):
        for jj in range(3*m):
            map2[ii,jj]=map[ii//3, jj//3]
    map2[ypos-1:ypos+2,xpos-1:xpos+2]=10
    nose = (ypos+direc[0]*3,xpos+direc[1]*3)
    dorsal = (ypos+direc[1]*3, xpos-direc[0]*3)
    ventral = (ypos-direc[1]*3,xpos+direc[0]*3)
    if show_direc:
        map2[nose] = 10
        map2[dorsal]= 10
        map2[ventral]= 10
    plt.imshow(np.flipud(map2), vmin = 0, vmax=10)
    plt.axis("off")
    
    
def turnRight(direc_x, direc_y):
    vec_dir = np.array([[direc_x],[direc_y]])
    mat_rot = np.array([[-1,0],[0,1]])
    vec_dir = np.dot(mat_rot,vec_dir)
    return int(vec_dir[1]), int(vec_dir[0])

def turnLeft(direc_x, direc_y):
    direc_x, direc_y = turnRight(direc_x, direc_y)
    direc_x, direc_y = turnRight(direc_x, direc_y)
    direc_x, direc_y = turnRight(direc_x, direc_y)
    return direc_x, direc_y

def jump(pos_x, pos_y, direc_x, direc_y):
        
    pos_x_new = pos_x + 2* direc_x
    pos_y_new = pos_y + 2*direc_y
    
    return pos_x_new, pos_y_new

def steps(n, pos_x, pos_y, direc_x, direc_y):
    #move the player forward from n steps in direc_x and direc_y starting from pos_x and pos_y.
    #Inputs:
        # n - the number of steps forward
        # pos_x, pos_y - the starting position
        # direc_x, direc_y - the direction of motion. 
    
    pos_x_new = pos_x+n*direc_x
    pos_y_new = pos_y+n*direc_y
    
    return pos_x_new, pos_y_new


def checkMove(pos_x, pos_y):
    if path[pos_y, pos_x]==0:
        return False
    else:
        return True
    
def step(position, direction):
   #move the player forward from n steps in direc_x and direc_y starting from pos_x and pos_y.
   #Inputs:
       # pos_x, pos_y - the starting position
       # direc_x, direc_y - the direction of motion. 
    pos_x = position[0]
    pos_y = position[1]
    direc_x = direction[0]
    direc_y = direction[1]
    pos_x_new = pos_x+direc_x
    pos_y_new = pos_y+direc_y
    return [pos_x_new, pos_y_new]


def checkSteps(n, pos_x, pos_y, direc_x, direc_y):
    
    pos_x_test, pos_y_test = steps(n, pos_x, pos_y, direc_x, direc_y)

    if checkMove(pos_x_test, pos_y_test):
        return True
    else: 
        return False
    
def checkTurnR(pos_x, pos_y, direc_x, direc_y):
    
    direc_x_test, direc_y_test = turnRight(direc_x, direc_y)
    pos_x_test, pos_y_test = steps(1, pos_x, pos_y, direc_x_test, direc_y_test)

    if checkMove(pos_x_test, pos_y_test):
        return True
    else: 
        return False
    
    
def checkTurnL(pos_x, pos_y, direc_x, direc_y):
    
    direc_x_test, direc_y_test = turnLeft(direc_x, direc_y)
    pos_x_test, pos_y_test = steps(1, pos_x, pos_y, direc_x_test, direc_y_test)

    if checkMove(pos_x_test, pos_y_test):
        return True
    else: 
        return False
    
def checkJump(pos_x, pos_y, direc_x, direc_y):
    pos_x_test, pos_y_test = jump(pos_x, pos_y, direc_x, direc_y) 
    
    if checkMove(pos_x_test, pos_y_test):
        return True
    else: 
        return False 
    
    
def move(pos_x, pos_y, direc_x, direc_y):
     
    if checkSteps(1, pos_x,pos_y, direc_x, direc_y): # check to see if the player can move one step forward       
        pos_x_new, pos_y_new = steps(1, pos_x,pos_y, direc_x, direc_y) # what would the new position be
        direc_x_new = direc_x # the direction doesn't change so the new direction values are the same. 
        direc_y_new = direc_y
    
    elif checkTurnR(pos_x, pos_y, direc_x, direc_y): # the player turns right and takes a step. 
        direc_x_new, direc_y_new = turnRight(direc_x, direc_y)
        pos_x_new, pos_y_new = steps(1, pos_x, pos_y, direc_x_new, direc_y_new)
    
    elif checkTurnL(pos_x, pos_y, direc_x, direc_y): # The player turns left and takes a step
        direc_x_new, direc_y_new = turnLeft(direc_x, direc_y)
        pos_x_new, pos_y_new = steps(1, pos_x, pos_y, direc_x_new, direc_y_new)
    
    else:
        pos_x_new, pos_y_new = jump(pos_x, pos_y, direc_x, direc_y) #find the new position if the player jumps forward.
        direc_x_new = direc_x
        direc_y_new = direc_y 
        
    return pos_x_new, pos_y_new, direc_x_new, direc_y_new # return the new position and direction values
    

    

path = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
       [0, 3, 3, 3, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 3, 3, 3, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0],
       [0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
       [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 5, 5, 5, 5, 5, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, 5, 5, 5, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, 5, 5, 5, 5, 0],
       [0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 5, 5, 5, 5, 5, 0],
       [0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 5, 5, 5, 5, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


dc_sunrise = np.array([[7, 6, 7, 6, 5, 5, 5, 6, 6, 7, 6, 7], [23, 57, 17, 29, 53, 40, 53, 20, 48, 16, 49, 18]])
dc_sunset = np.array([[5, 5, 7, 7, 8, 8, 8, 8, 7, 6, 4, 4],[11, 46, 16, 46, 15, 36, 34, 4, 18, 31, 55, 48]])

dc_sunrise_orig = np.array([[7, 6, 7, 6, 5, 5, 5, 6, 6, 7, 6, 7], [23, 57, 17, 29, 53, 40, 53, 20, 48, 16, 49, 18]])
dc_sunset_orig = np.array([[5, 5, 7, 7, 8, 8, 8, 8, 7, 6, 4, 4],[11, 46, 16, 46, 15, 36, 34, 4, 18, 31, 55, 48]])

berlin_sunrise = np.float32(np.array([[8,7,6,6,5,4,4,5,6,7,7,8],[7,20,18,6,7,40,59,47,39,30,26,8]]))
berlin_sunset = np.float32(np.array([[4,5,6,8,8,9,9,8,7,6,4,3],[23,20,11,6,57,33,25,34,24,14,15,54]]))


canberra_sunrise = np.float32(np.array([[6,6,7,6,6,7,7,6,6,6,5,5],[3,35,0,25,49,8,8,43,2,19,47,41]]))
canberra_sunset = np.float32(np.array([[8,8,7,5,5,4,5,5,5,7,7,8],[22,0,24,41,9,59,10,32,55,19,48,15]]))

beijing_sunrise = np.float32(np.array([[7,7,6,5,4,4,4,5,5,6,6,7],[32,5,24,35,58,43,56,24,53,23,57,26]]))
beijing_sunset = np.float32(np.array([[5,5,6,6,7,7,7,7,6,5,5,4],[14,51,21,53,23,46,43,13,25,37,0,51]]))

helsinki_sunrise = np.float32(np.array([[9,7,6,6,4,3,4,5,6,7,8,9],[6,56,34,0,37,50,19,31,45,57,16,15]]))
helsinki_sunset = np.float32(np.array([[3,5,6,8,9,10,10,9,7,6,3,3],[53,12,23,40,55,50,33,17,44,14,53,15]]))

manila_sunrise = np.float32(np.array([[6,6,6,5,5,5,5,5,5,5,5,6],[23,18,2,41,27,25,33,40,43,46,55,11]]))
manila_sunset = np.float32(np.array([[5,6,6,6,6,6,6,6,5,5,5,5],[47,1,7,11,17,27,30,20,59,37,25,30]]))

def f(x, y):
    return np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
X, Y = np.meshgrid(np.linspace(0, 5, 30), np.linspace(0, 5, 20))
contour = f(X,Y)*400+1400

hiking_path = [(19,2),(18,2),(17,2),(16,2),(16,3),(15,3),(14,3),(13,4),(12,4),(11,5),(10,6),\
              (9,7),(9,8),(9,9),(10,10),(10,11),(10,12),(9,13),(9,14),(9,15),(8,16),(8,17),\
              (7,18), (7,19), (7,20), (7,21), (7,22), (8, 23), (9,22), (9,21),(10,20), (11,19),\
              (11,18),(12,17), (12, 16), (13,15), (14,14),(15,13),(15,13),(16,13),(17,12), (18,12),(19,12)]






