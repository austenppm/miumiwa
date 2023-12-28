# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(0, 2 * np.pi, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.scatter(x, y)
# plt.bar(x, y, width=0.05)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 2 * np.pi, 0.1)
# y = np.sin(x) + np.sin(x*2.0) * 0.5
# plt.plot(x, y)
# plt.scatter(x, y)
# plt.bar(x, y, width=0.05)
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 2 * np.pi, 0.1)
# y = np.sin(x) + np.sin(x/3.0) / 3.
# print(x)
# plt.plot(x, y)
# plt.scatter(x, y)
# plt.bar(x, y, width=0.05)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 12 * np.pi, 0.1)
y = np.sin(x/2.0) + np.sin(x/3.0)
plt.plot(x, y)
plt.scatter(x, y)
plt.bar(x, y, width=0.05)
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt

# x = np.arange(0, 1* np.pi, 0.1)
# y = np.cos(x)**2
# plt.plot(x, y)
# plt.scatter(x, y)
# plt.bar(x, y, width=0.05)
# plt.show()