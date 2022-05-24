import numpy as np
from matplotlib import pyplot as plt, cm
import matplotlib.ticker as mtick
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mpl_toolkits.mplot3d import Axes3D


def dark_style():
    plt.style.use("seaborn-dark")
    for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
        plt.rcParams[param] = '#151515'  # bluish dark grey
    for param in ['text.color', 'xtick.color', 'grid.color', 'ytick.color', 'axes.labelcolor']:
        plt.rcParams[param] = 'white'  # very light grey
    plt.rcParams["axes.edgecolor"] = "white"
    plt.rcParams["axes.linewidth"] = 1


class Canvas(FigureCanvas):

    def __init__(self, parent):
        dark_style()

        self.fig, self.ax = plt.subplots(dpi=77)

        super().__init__(self.fig)
        self.setParent(parent)
        self.ax.grid(c="#003740")

    def plot(self, x, y):
        self.ax.clear()
        self.ax.set(xlabel='?', ylabel='?', title='?')
        self.ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
        self.ax.grid(c="#003740")
        self.ax.plot(x, y)

    def surface(self, a, b, h, f_class, fct):

        self.fig.clf()

        self.a = a
        self.b = b
        self.h = h
        self.f_class = f_class
        self.fct = getattr(self.f_class, fct)

        x = np.arange(self.a, self.b, self.h)
        y = np.arange(self.a, self.b, self.h)
        xx, yy = np.meshgrid(x, y)
        ax = Axes3D(self.fig)
        self.f_class.set_x(xx, yy)
        ax.plot_surface(xx, yy, self.fct(), cmap=cm.coolwarm)

    def contour(self, x, y, h, f_class, fct, arg):
        self.ax.clear()
        a = int(x - 1)
        b = a + 2
        c = int(y - 1)
        d = c + 2

        self.f_class = f_class
        self.fct = getattr(self.f_class, fct)
        x = np.arange(a, b, h)
        y = np.arange(c, d, h)
        xx, yy = np.meshgrid(x, y)
        self.f_class.set_x(xx, yy)

        self.ax.contour(xx, yy, self.fct(), arg)




