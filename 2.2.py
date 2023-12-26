# x = 1
# x = x + 2
# x = x * 3
# print(x)

# x = 4
# print(x)

# a = 2
# b = 3
# c = (a + b) / 3
# d = (a + b) % 3
# e = ((a - b) * b + a) * b
# f = int(c)
# print(a, b, c, d, e, f)
# print(type(c), type(d))


# a = 2
# b = 3
# c = (a + b) / 3
# d = (a + b) % 3
# e = ((a - b) * b + a) * b
# f = int(c)

# print("cは%f, eは%dです" % (c, e))
# print(type("d") , type(d))


# a = [1, 2, 3]
# print(a)
# print(len(a))
# print(a[0], a[2])


# import numpy as np

# a = np.array([1, 2, 3])
# b = np.array([2, 2, 2])
# print(a*2)
# print(a/2)
# print(a+2)
# print(a+b)
# print(a*b)
# print(a.dot(b))


# import numpy as np
# a = np.array([1, 2, 3, 4])
# b = a[0:2]
# print(b)
# c = a[1:]
# print(c)
# d = a[:3]
# print(d)

# import numpy as np
# a = "Hello World"
# b = list(range(5))
# c = list(range(1, 10, 2))
# d = np.zeros(4)
# e = np.ones(3)
# f = np.arange(0, 1, 0.1)
# print(a[3:9])
# print(b, c)
# print(d, e, f)


# import numpy as np
# A = np.array([[1, 2, 3], [4, 5, 6]])
# b = np.array([2, 2, 2])
# print(A)
# print(A[0][0], A[0][1], A[1][0])
# print(A.shape[0], A.shape[1])
# print(A*3)
# print(A*b)
# print(A+b)

import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.ones([2, 2])
print(A)
print(B)
print(A+B)
print(A*B)
print(np.dot(A, B))
print(A.T)
print(np.linalg.inv(A))