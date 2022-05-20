# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 07:44:00 2022

@author: coren
"""
import matplotlib.pyplot as pp
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def g(x1, x2):
    return x1**2 + x2**4 + 2 * x2**2


def g_der(x1, x2):
    return np.array([2 * x1, 4 * x2**3 + 4 * x2])


def H_g(x1, x2):
    return np.array([[2, 0], [0, 12 * x2**2 + 4]])


def Rosenbrock(x, y):
    return (x - 1) ** 2 + 10 * (x**2 - y) ** 2


def Ros_der(x, y):
    return np.array([40 * x**3 + 2 * x - 2 - 40 * x * y, -20 * x**2 + 20 * y])


def H_Ros(x, y):
    return np.array([[120 * x**2 + 2 - 40 * y, -40 * x], [-40 * x, 20]])


def Surface(a, b, h, f):
    x = np.arange(a, b, h)
    y = np.arange(a, b, h)
    xx, yy = np.meshgrid(x, y)
    fig = pp.figure()
    ax = Axes3D(fig)
    ax.plot_surface(xx, yy, f(xx, yy))
    pp.show()


def Lignes_niveau(a, b, h, f, arg):
    x = np.arange(a, b, h)
    y = np.arange(a, b, h)
    xx, yy = np.meshgrid(x, y)
    pp.figure()
    pp.contour(xx, yy, f(xx, yy), arg)
    pp.colorbar()
    pp.show()


def gradientPasFixe(x0, rho, tol, Nitermax, f_der):
    i = 0
    x = x0.copy()
    x_list = [x]
    while np.linalg.norm(f_der(x[0], x[1])) > tol and i < Nitermax:
        d = -f_der(x[0], x[1])
        x += rho * d
        i += 1
        x_list.append(x.copy())
    return (x, x_list, i)


def gradientPasOptimal(x0, rho, tol, Nitermax, Hf, f_der):

    i = 0
    x = x0
    x_list = [x]
    while np.linalg.norm(f_der(x[0], x[1])) > tol and i < Nitermax:
        d = -f_der(x[0], x[1])
        rho = rechercheDuPas(x, d, rho, 10**-8, 10**4, Hf, f_der)

        x += rho * d
        i += 1
        x_list.append(x)
    return (x, x_list, i)


def rechercheDuPas(x, d, rho, tolR, maxIt, Hf, f_der):
    rho_0 = 10 * rho
    j = 1
    while abs(rho - rho_0) > tolR and j < maxIt:
        phi_p = d.T @ f_der(x[0] + rho * d[0], x[1] + rho * d[1])
        phi_s = d.T @ Hf(x[0] + rho * d[0], x[1] + rho * d[1]) @ d
        rho_0 = rho
        rho = rho - phi_p / phi_s
        j += 1
    return rho


def gradientPreconditionne(x0, rho, tol, Nitermax, H_f, f_der, f):
    pass


Surface(-3, 3, 0.1, g)
Lignes_niveau(-3, 3, 0.1, g, [i for i in range(12)])
x0_1 = np.array([1.2, 1.2]).T
pas_1 = 10**-2
Sol1 = gradientPasFixe(x0_1, pas_1, 10**-4, 10**5, g_der)
Sol2 = gradientPasOptimal(x0_1, pas_1, 10**-4, 10**5, H_g, g_der)
print(Sol1[0], Sol1[2])
print(Sol2[0], Sol2[2])
