import numpy as np
import transferFunctions as tf

p1 = np.array([-1, 1, -1 ,1])
p2 = np.array([1, -1, 1, 1])
# i
i = p1.T @ p2

# ii
P = np.array([p1, p2])
W = P.T @ P

# iii
pt = np.array([1,1,1,1])
output = W @ pt
print(tf.hardlims(output))