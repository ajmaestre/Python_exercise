import numpy as np

# ---------------------------------- TASK 1 -----------------------------

def suma_matrices(a,b):
    ## --- TU CODIGO AQUI ---
    result = a + b
    return result


a = np.random.randint(10, size=(3,2))
b = np.random.randint(10, size=(3,2))
print (a)
print (b)
print (suma_matrices(a,b))


# -------------------------------------------- TASK 2 ------------------------------

rlist = np.random.randint(100, size=10)
print(rlist)

# usando numpy
print(np.mean(rlist))

# usando un método rebuscado
print(sum(rlist)/len(rlist))