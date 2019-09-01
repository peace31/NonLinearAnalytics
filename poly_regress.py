import numpy as np
from sklearn.preprocessing import PolynomialFeatures
deg = int(input ("input the degree: "))
# Create matrix and vectors
X = [[0.44, 0.68], [0.99, 0.23]]
y = [109.85, 155.72]
X_test = np.array([0.49, 0.18]).reshape(1,-1)

# PolynomialFeatures (prepreprocessing)
poly = PolynomialFeatures(degree=deg)
X_ = poly.fit_transform(X)
X_test_ = poly.fit_transform(X_test)

print("Real test value: ",X_test)
print("regressed test value: ",X_test_)