from math import *
from numpy import linspace
import matplotlib.pyplot as plt

def f(x : float, y : float) -> float:
    return -sin(x)/y

##Definição dos pontos iniciais
x_o, y_o, x_f = 0, -1, pi/3

h = 0.1

def y_analitico(x, xInicial, yInicial):
    return -sqrt(yInicial**2 + 2*(cos(x) - cos(xInicial)))


def analiticalSolver(xInicial, xFinal, yInicial):
    x = linspace(xInicial, xFinal, 100)
    y = [y_analitico(i, xInicial, yInicial) for i in x]

    return x, y

def eulerSolver(xInicial, yInicial,xFinal, g, h):
    """Retorna uma tupla de arrays com a solução do método de Euler para um 
    determinado h, considerando y' = g(x,y)
    """
    x = [xInicial]
    y = [yInicial]

    i = 0
    while(x[i] < xFinal):
        x.append(x[i] + h)
        y.append(y[i] + h* g(x[i], y[i]))
        i += 1

    return x, y

def heunSolver(xInicial, yInicial,xFinal, g, h):
    """Retorna uma tupla de arrays com a solução do método de Heun para um 
    determinado h, considerando y' = g(x,y)
    """

    def k1(x, y):
        return g(x, y)

    def k2(x, y):
        return g(x + h, y + h*g(x, y + h*k1(x, y)))

    x = [xInicial]
    y = [yInicial]

    i = 0
    while(x[i] < xFinal):
        x.append(x[i] + h)
        y.append(y[i] + (h/2)*(k1(x[i], y[i]) + k2(x[i], y[i])))
        i += 1

    return x, y

def RK4Solver(xInicial, yInicial,xFinal, g, h):
    """Retorna uma tupla de arrays com a solução do método de Runge-Kutta de 4ª
    ordem para um determinado h, considerando y' = g(x,y)
    """
    def k1(x, y):
        return g(x, y)

    def k2(x, y):
        return g(x + h/2, y + (h/2)*k1(x, y))

    def k3(x, y):
        return g(x + h/2, y + (h/2)*k2(x, y))
    
    def k4(x, y):
        return g(x + h, y + h*k3(x,y))

    x = [xInicial]
    y = [yInicial]

    i = 0
    while(x[i] < xFinal):
        x.append(x[i] + h)
        y.append(y[i] + (h/6)*(k1(x[i], y[i]) + 2*k2(x[i], y[i])  + 2*k3(x[i], y[i]) + k4(x[i], y[i])))
        i += 1

    return x, y

def main():
    fig, ax = plt.subplots()

    eulerSolution = eulerSolver(x_o, y_o, x_f, f, h)
    heunSolution = heunSolver(x_o, y_o, x_f, f, h)
    RKSolution = RK4Solver(x_o, y_o, x_f, f, h)
    AnaliticalSolution = analiticalSolver(x_o, x_f, y_o)


    ax.plot(eulerSolution[0], eulerSolution[1], label = 'euler', ls = '--', color = 'red')
    ax.plot(heunSolution[0], heunSolution[1], label = 'heun', ls = '--')
    ax.plot(RKSolution[0], RKSolution[1], label = 'Runge-Kutta', ls = '--', color = 'green')
    ax.plot(AnaliticalSolution[0], AnaliticalSolution[1], label = 'Solução Analítica', color =  'black')

    ax.set_title(f'Aproximação para h = {h}')
    ax.legend()
    plt.show()

if __name__ == '__main__':
    main()
