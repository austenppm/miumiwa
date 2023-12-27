# def fukuri(ganpon, kinri, year):
#     chokin = ganpon
#     for i in range(1, year+1) :
#         chokin = chokin + chokin * kinri
#         print(chokin)
#         print(year)
#     return chokin
# A = fukuri(100000, 0.01, 10)
# B = fukuri(100000, 0.02, 10)
# print(int(A), int(B))
# print(chokin)
# print(year)

import numpy as np
import matplotlib.pyplot as plt

def sin_sum(x, n):
    sum = 0
    for i in range(1, n+1):
        sum += np.sin(i*x) / i
    return sum

x = np.arange(0, 2*np.pi, 0.1)
y1 = sin_sum(x, 10)
y2 = sin_sum(x, 50)
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()