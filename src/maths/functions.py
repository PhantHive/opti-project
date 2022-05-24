import numpy as np


class Functions:

    def __init__(self, x1=None, x2=None):
        """
        functions with their derivatives
        :param self.x1:
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

        # ------------------------
        #          Equation 1
        # ------------------------

    def f(self):
        return self.x1**2 + self.x2**4 + 2 * self.x2**2

    def f_der(self):
        return np.array([2 * self.x1, 4 * self.x2**3 + 4 * self.x2])

    def H_f(self):
        return np.array([[2, 0], [0, 12 * self.x2**2 + 4]])

        # ------------------------
        #          Equation 2
        # ------------------------

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

        # ------------------------
        #          Equation 3
        # ------------------------

    def g1(self):
        return (self.x1 - 1)**2 + 2 * self.x2**2

    def g1_der(self):
        return np.array([2 * self.x1 - 2, 2 * self.x2])

    def H_g1(self):
        return np.array([[2, 0], [0, 2]])

        # ------------------------
        #          Equation 4
        # ------------------------

    def g2(self):
        return 2 * self.x1**3 - 6 * self.x1 * self.x2 + 3 * self.x2**2

    def g2_der(self):
        return np.array(
            [6 * self.x1**2 - 6 * self.x2, -6 * self.x1 - 6 * self.x2])

    def H_g2(self):
        return np.array([[12 * self.x1, -6], [-6, -6]])

        # ------------------------
        #          Equation 5
        # ------------------------

    def g3(self):
        return self.x1**2 * self.x2**3

    def g3_der(self):
        return np.array(
            [2 * self.x1 * self.x2**3, 3 * self.x1**2 * self.x2**2])

    def H_g3(self):
        return np.array([
            [2 * self.x2**3, 6 * self.x1 * self.x2**2],
            [6 * self.x1 * self.x2**2, 6 * self.x1**2 * self.x2],
        ])

       # ------------------------
        #          Equation Speciale
        # ------------------------

    def s(self):
        return (self.x1 ** 2 + self.x2 - 11) ** 2 + (self.x1 + self.x2 ** 2 - 7) ** 2

    def s_der(self):
        return np.array([4 * self.x1 ** 3 + 2 * self.x2 ** 2 - 42 * self.x1 + 4 * self.x1 * self.x2 - 14,
                         4 * self.x2 ** 3 + 2 * self.x1 ** 2 - 26 * self.x2 + 4 * self.x1 * self.x2 - 22])

    def H_s(self):
        return np.array([[12 * self.x1 ** 2 + 4 * self.x2 - 42, 4 * self.x1 + 4 * self.x2],
                         [4 * self.x1 + 4 * self.x2, 4 * self.x1 * self.x2 ** 2 - 26 + 8 * self.x2 ** 2]])