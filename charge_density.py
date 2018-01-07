import numpy as np
import copy
#This is the coordinate of the Pt atom
Source = [0.5,0.5]
#The charge density matrix is stored in the variable A
A = np.loadtxt('charge_densities')
#The following snippet stores the coordinates of the grid
B = []
for j in range(120):
    for i in range(120):
        B.append([i/119*10.460582,j/119*10.460582])
#Reshaping the charge density matrix so that there is a correspondance between the grid matrix and the charge density matrix
A = np.reshape(A,120*120)
#Convert numpy array into python list
A = A.tolist()
#A 2-d polar coordinate variable theta to rotate the vectors
theta = 0
#List Z to store the ccoordinates of points having max charge densities along multiple directions
Z =[]
while 1:
    #List X to store indices of points which lie on a particular vector
    X = []
    for i in range(len(B)):
        #List M defined to apply the determinant formula of checking whether 3 points lie on a line
        M = [Source+[1],[0.5+30*np.cos(theta*np.pi/180),0.5+30*np.sin(theta*np.pi/180),1],B[i]+[1]]
        #Some range of error is allowed
        if abs(np.linalg.det(M)) < 0.001:
            X.append(i)
    #List Y to store charge densities corresponding to the coordinates
    Y = copy.deepcopy(X)
    for j in range(len(X)):
        Y[j] = A[j]
    #Checking if there's atleast one value in Y in because max function doesn't allow empty list
    if len(Y) > 0:
        #Index of the maximum charge density value for that particular value of theta
        index = Y.index(max(Y))
        #The cartesian cordinate is retrived from list X and is appended to list Z
        Z.append(B[X[index]])
    #Amount by the vector has to be rotated after every iteration
    theta += 1
    #If one rotation is complete, break!
    if theta >= 360:
        break
#Following snippet removes duplicate elements from list Z
new_Z = []
for point in Z:
    if point not in new_Z:
        new_Z.append(point)
Z = new_Z
#All the coordinates cooresponding to maximum charge densities are printed
print(Z)
