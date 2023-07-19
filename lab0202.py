
import numpy as np


# ------------------------------------------------ TASK 1 ------------------------------------------------

def cauchy(x, y):
    c = (x.reshape(-1,1) - y)
    if c[c == 0].shape[0] != 0:
        raise ValueError
    r = 1 / c
    return r

x = np.array([45, 31, 67, 75, 54])
y = np.array([17,  3, 15, 15, 18])
print(cauchy(x,y))
print()

# ---------------------------------------------------- TASK 2 -------------------------------------------

def minimo(x, v):
    return np.argmin(np.abs(x-v))

x = np.arange(25,55,3)
v = 34
print(minimo(x,v))
print()

# ------------------------------------------------------- TASK 3 ---------------------------------------

def media(X):
    return  X - (np.mean(X, axis=1)).reshape(-1,1)

X = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])
print(media(X))
print()

# ------------------------------------------------------- TASK 4 ------------------------------------------

def doublediag(X):
    return X * ((np.eye(X.shape[0]) + 1))

X = np.array([[79, 45, 67,  8, 37],
              [47, 40,  5, 79, 86],
              [72, 25, 44, 45, 22],
              [12, 85,  8, 53, 28],
              [ 4, 37, 36, 40, 16]])
print(doublediag(X))