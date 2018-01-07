import numpy as np
#This is the coordinate of the Pt atom
Source = [0.5,0.5]
#The charge density matrix gives only the values of the charge desnities and not the coordinates. Following snippet stores the coordinates of the grid
B = []#Matrix B stores the coordinates of the grid
for j in range(120):
    for i in range(120):
        B.append([i/119*10.460582,j/119*10.460582])
#A list created to store the points which lie on the vector
L =[]
#A variable theta is defined in order to rotate the vector originating from the source
theta = 0
#The while loop iterates over different values of theta
while 1:
    #The for loop iterates over the points of the grid for a given value of theta
    for point in B:
        #Matrix M defined to apply determinant formula to check if three points are on a straight line
        M = [Source+[1],[0.5+30*np.cos(theta*np.pi/180),0.5+30*np.sin(theta*np.pi/180),1],point+[1]]
        #Some range of error is allowed
        if abs(np.linalg.det(M)) < 0.001:
            L.append(point)
    theta += 1
    if theta >= 360:
        break
#No. of points in the list (this includes repeating elements too)
print("The no. of points covered by the vectors are "+str(len(L)))
#Remove duplicate elements from the list
new_L = []
for point in L:
    if point not in new_L:
        new_L.append(point)
#No. of unique points in the list
print("The no. of unique points covered by the vectors are "+str(len(new_L)))
