import numpy as np


class Functions:

    def __init__(self, x1=None, x2=None):
        """
        functions with their derivatives
        :param x1:
        :param x2:
        """

        self.x1 = x1
        self.x2 = x2
        self.eq = 1

    def set_x(self, x1, x2):

        self.x1 = x1
        self.x2 = x2

    def set_equation(self, i):
        self.eq = i

    def get_equation(self):
        return self.eq

    def g(self):
        return self.x1**2 + self.x2**4 + 2 * self.x2**2

    def g_der(self):
        return np.array([2 * self.x1, 4 * self.x2**3 + 4 * self.x2])

    def H_g(self):
        return np.array([[2, 0], [0, 12 * self.x2**2 + 4]])

    def Rosenbrock(self):
        return (self.x1 - 1)**2 + 10 * (self.x1**2 - self.x2)**2

    def Ros_der(self):
        return np.array([
            40 * self.x1**3 + 2 * self.x1 - 2 - 40 * self.x1 * self.x2,
            -20 * self.x1**2 + 20 * self.x2,
        ])

    def H_Ros(self):
        return np.array([
            [120 * self.x1**2 + 2 - 40 * self.x2, -40 * self.x1],
            [-40 * self.x1, 20],
        ])
