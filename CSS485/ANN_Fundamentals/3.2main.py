import numpy as np
import transferFunctions as tf

p1 = np.array([-1, 1, -1 ,1])
p2 = np.array([1, -1, 1, 1])

# ii
P = np.array([p1, p2])
W = np.linalg.pinv(P) @ P

print(W)
# iii
pt = np.array([1,1,1,1])
output = W @ pt
print(tf.hardlims(output))