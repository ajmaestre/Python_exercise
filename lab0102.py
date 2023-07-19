
import numpy as np

# ---------------------------------------TASK 1 ----------------------------------

t1_actual    = np.random.randint(2, size=20)
t1_predicted = np.abs(t1_actual*(np.random.random(size=20)>(np.random.random()*.9+.05)).astype(int))
print ("actual   ", ", ".join([str(i) for i in t1_actual]))
print ("predicted", ", ".join([str(i) for i in t1_predicted]))

print(np.mean(t1_actual == t1_predicted))

asiertos = t1_actual == t1_predicted
print(sum(asiertos)/len(asiertos))


# ------------------------------------------ TASK 2 -------------------------------------------

t2_predicted = np.random.randint(2, size=20)
t2_actual = np.random.randint(2, size=20)
t2_predicted[np.argwhere(t2_actual==1)[0][0]]=0
print ("actual   ", ", ".join([str(i) for i in t2_actual]))
print ("predicted", ", ".join([str(i) for i in t2_predicted]))

vp = 0
fn = 0
for i in range(len(t2_actual)):
    if t2_actual[i] == t2_predicted[i] and t2_actual[i] == 1:
        vp += 1
    elif t2_actual[i] != t2_predicted[i] and t2_actual[i] == 1:
        fn += 1

tpr = vp/(vp + fn)
print(tpr)


# -------------------------------------------- TASK 3 -----------------------------------------

t3_actual    = np.random.randint(80,size=15)+20
t3_predicted = np.random.randint(80,size=15)+20
print ("actual   ", t3_actual)
print ("predicted", t3_predicted)

suma = 0
i = 0
n = len(t3_actual)

while i < n:
    suma += (np.log(t3_predicted[i] + 1) - np.log(t3_actual[i] + 1))**2
    i += 1

rmsle = np.sqrt((1/n)*suma)

print(round(rmsle, 3))

# ---------------------------------------- TASK 4 ---------------------------------------------

t4_predicted = np.random.random(size=(7,5)).T+0.5
t4_predicted = np.round((t4_predicted/np.sum(t4_predicted,axis=0)),2).T

t4_actual = np.eye(5)[np.random.randint(5,size=len(t4_predicted))].astype(int)

print ("actual")
print (t4_actual)
print ("\npredicted")
print (t4_predicted)

suma = 0
i = 0
m = len(t4_actual)

while i < m:
    j = 0
    n = len(t4_actual[i])
    while j < n:
        suma += (t4_actual[i][j] * np.log(t4_predicted[i][j]))
        j += 1
    i += 1

print('')
suma = - (1/m) * suma
print(round(suma, 3))