import numpy as np
A = np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
A_inv=np.linalg.inv(A)
b=np.array([6,2,-5,17,12])
x=A_inv@b
print("x =",x[0])
print("y =",x[1])
print("z =",x[2])
print("t =",x[3])
print("u =",x[4])
print(np.linalg.solve(A,b))