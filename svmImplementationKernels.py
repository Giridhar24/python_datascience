# Topic of the Day: SVM Implementation (Kernels)
#
# Explanation: Yesterday we discussed the "Kernel Trick" (projecting data into 3D to slice it). Today we use it.
#
# Linear Kernel: Draws a straight line.
#
# RBF Kernel: Draws a curved/circular boundary (good for complex clusters).

from sklearn.svm import SVC
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# 1. Create tricky data (A small circle inside a big circle)
# A straight line CANNOT separate these!
X, y = make_circles(n_samples=100, factor=0.5, noise=0.1)

# 2. Train SVM with RBF Kernel (Radial Basis Function)
model = SVC(kernel='rbf')
model.fit(X, y)

# 3. Visualize Prediction
# (If we plotted this, we would see a circular boundary separating the inner dots)
print(f"Accuracy: {model.score(X, y)}")
# Result: ~1.0 (100%), because RBF can handle circles.
# A 'linear' kernel would get ~0.5 (50%) fail.