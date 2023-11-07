# Definição da função
def f(x : float) -> float:
    return x

# Definição do tamanho do passo
def dx(a: float, b: float, n : int) -> float:
    return (b-a)/n

# Definição da soma de Riemann
def sum(a : float, b : float, n : int , f) -> float:
    deltaX = dx(a, b, n)
    x = a
    sum = 0
    for k in range(1, n+1):
        x += deltaX
        sum += deltaX * f(x)

    return sum

for i in range(5):
    n = 10**i
    soma = sum(0, 1, n, f)
    print(f'n = {n} : soma = {soma} , erro = {abs(0.5 - soma)/(0.005)}')

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

for i in range(5):
    n = 10**i
    x = []
    y = []
    deltaX = dx(0, 1, n)
    for i in range(1, n+1):
        x.append(i*deltaX)
        y.append(sum(0,i*deltaX,n,f))

    ax.plot(x, y, label = f'n = {n}', ls = '--')


x = np.linspace(0,1, 100)
y = [(i**2)/2 for i in x]
ax.plot(x, y, label = 'valor real', color = 'black')

ax.set(ylim = (0,0.6))
ax.legend()
plt.show()
