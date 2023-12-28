def fukuri(ganpon, kinri, year):
    chokin = ganpon
    for current_year in range(1, year+1) :
        chokin = chokin + chokin * kinri
        print(current_year, chokin)
        print(year)
    return chokin

A = fukuri(100000, 0.01, 10)
B = fukuri(100000, 0.02, 10)

# def fukuri(ganpon, kinri1, kinri2, year):
#     chokin1 = ganpon
#     chokin2 = ganpon
#     for year in range(1, year+1) :
#         chokin1 = chokin1 + chokin1 * kinri1
#         chokin2 = chokin2 + chokin2 * kinri2
#         print(year, chokin1, chokin2)
        
#     return chokin1, chokin2

# A, B = fukuri(100000, 0.01, 0.02, 10)
# print(int(A))
# print(type(A))

# print(int(A), int(B))
# print(chokin)
# print(year)

# import numpy as np
# import matplotlib.pyplot as plt

# def sin_sum(x, n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += np.sin(i*x) / i
#     return sum

# x = np.arange(0, 2*np.pi, 0.1)
# y1 = sin_sum(x, 3)
# y2 = sin_sum(x, 3)
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# def sin_sum24(x, n):
#     sum = 0 
#     for i in range (1, n+1):
#         sum = sum + np.sin((2*i-1)*x) / (2*i-1)
#     return sum

# x = np.arange(0, 2*np.pi, 0.1)
# y1 = sin_sum24(x, 50)
# plt.plot(x, y1)
# plt.show()
