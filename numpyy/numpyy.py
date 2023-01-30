import numpy as np
matric=[]
row = int(input("enter the number of row "))
col= int(input("enter the number of column "))
for i in range(row):
    a=[]
    for i in range(col):
        ii=int(input("enter the number "))
        a.append(ii)
    matric.append(a)
arr=np.array(matric)
for i in range(row):
    for j in range(col):
        print(arr[i][j],end='   ')
    print()