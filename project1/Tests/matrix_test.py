import numpy as np

"""
m = np.matrix('1,2,3;4,5,6;7,8,9')

print(m)


x = np.where(m == 5)

print(x)



y = x[0]

print type(y)


l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

matrix = [l1, l2, l3]

print matrix

for l in matrix:
    try:
        print l.index(9)
    except:
        print "Not Found"

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print np.unravel_index(5, m.shape)

print(m)

#z = np.unravel_index(15, m.shape)
z = np.where(m == 15)

print(z)

i,j = np.where(m == 0)
x,y = np.where(m == 3)

print i,j
print x,y

m[i,j] = 3
m[x,y] = 0

print("New Matrix After Swap:")
print(m)
"""

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
i,j = np.where(m == 5)
print "i,j : "
print i,j
print "i,j == (1,1):"
print ((i,j) == (1,1))
l = i.tolist(),j.tolist()
joined = l[0] + l[1]
print "joined:"
print joined
print "joined == [1 ,1]:"
print joined == [1 , 1]

