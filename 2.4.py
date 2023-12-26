# for i in [1, 2, 3]:
#     print(i)
# for i in range(10):
#     print(i)
    
# sum = 0

# for i in range(1, 10, 2):
#     sum = sum + i
#     print(i, sum)
    
# print("合計は%d" % sum)


# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 2 * np.pi, 0.1)
# y = 0

# for i in range(1, 3) :
#     y = y + np.sin(i*x) / i
    
# plt.plot(x, y)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, 0.1)
y = 0

for i in range(1, 50) :
    y = y + np.sin((2*i-1)*x) / (2*i-1)
    
plt.plot(x, y)
plt.show()
