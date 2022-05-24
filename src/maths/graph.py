import numpy as np
import matplotlib.pyplot as pp
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''

def dark_style():
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#151515'  # bluish dark grey
    for param in ['text.color', 'xtick.color', 'grid.color', 'ytick.color', 'axes.labelcolor']:
        plt.rcParams[param] = 'white'  # very light grey
    plt.rcParams["axes.edgecolor"] = "white"
    plt.rcParams["axes.linewidth"] = 1'''

class Graph:

    def __init__(self, a, b, h, f_class, fct):

        #dark_style()
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

if __name__ == '__main__':

    from src.maths.functions import Functions
    fct = Functions(None, None)

    grph = Graph(-5, 5, 0.1, fct, "s")
    grph.Surface()
