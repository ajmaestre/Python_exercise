import numpy as np


# -------------------------------------------- TASK 1 ---------------------------------------------------

def palindromo(n): # assume n is an integer
    # your code here
    r = list(str(n))
    r.reverse()
    return list(str(n)) == r

print(palindromo('nanan'))

# ----------------------------------------------- TASK 2 ---------------------------------------------------

def change_money(n):
    r=[0,0,0] #recall: r[0]== n_1, r[1]== n_10 y r[2]== n_25 
    #if n>99 or n<1: use return None
    
    ## tu codigo aquí

    if n < 100 and n > 0:
        r[2] = n // 25
        r[1] = (n % 25) // 10
        r[0] = ((n % 25) % 10) // 1
        return r
    else:
        return None

print(change_money(47))


# ---------------------------------------------- TASK 3 ---------------------------------------

def fibonacci(n):
    f_1=1
    f_2=1
    suma=0
    
    # tu codigo aqui
    arr = []
    arr.insert(0, 0)
    arr.insert(1, f_1)
    arr.insert(2, f_2)
    for i in range(3, n+1):
        arr.insert(i, arr[i-1] + arr[i-2])
    suma = arr[-1]
    return suma

print(fibonacci(10))


# ----------------------------------------------------- TASK 4 -------------------------------------------

def perfecto(n):
    #tu codigo aqui, pista:
    # halle todos los divisores de n y sumelos en una variable auxiliar,
    #compare este resultado con el valor original
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    print(suma)
    if suma == n:
        return True
    else:
        return False

print(perfecto(51))