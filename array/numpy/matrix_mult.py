from numpy import *

mat1=matrix('1,2,5;3,4,6')
mat2=matrix('1,2;3,4;5,6')

# mutiply two matrix

for i in range(mat1.shape[0]):
    for j in range(mat2.shape[1]):
        sum=0
        for k in range(mat1.shape[1]):
            sum+=mat1[i,k]*mat2[k,j]
        print(sum,end=' ')
    print()
    