import numpy as np
import matplotlib.pyplot as pp
from mpl_toolkits.mplot3d import Axes3D

class Graph:

    def __init__(self, a, b, h, f_class, fct):

        self.a = a
        self.b = b
        self.h = h
        self.f_class = f_class
        self.fct = getattr(self.f_class, fct)

    def Surface(self):
        x = np.arange(self.a, self.b, self.h)
        y = np.arange(self.a, self.b, self.h)
        xx, yy = np.meshgrid(x, y)
        fig = pp.figure()
        ax = Axes3D(fig)
        self.f_class.set_x(xx, yy)
        ax.plot_surface(xx, yy, self.fct())
        pp.show()

    def Lignes_niveau(self, arg):
        x = np.arange(self.a, self.b, self.h)
        y = np.arange(self.a, self.b, self.h)
        xx, yy = np.meshgrid(x, y)
        self.f_class.set_x(xx, yy)
        pp.figure()
        pp.contour(xx, yy, self.fct(), arg)
        pp.colorbar()
        pp.show()