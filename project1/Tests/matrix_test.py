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
"""

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print np.unravel_index(5, m.shape)


m = np.array([[1,2,3,10],[4,5,6,11],[7,8,9,12]])
print(m)
print np.unravel_index(5, m.shape)


