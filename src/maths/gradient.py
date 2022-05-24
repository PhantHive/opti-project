import numpy as np
from src.maths.functions import Functions

class Gradient:


    def __init__(self, x0, rho, tol, Nitermax, f_der, Hf):

        self.x0 = x0
        self.rho = rho
        self.tol = tol
        self.Nitermax = Nitermax
        self.fct = Functions(None, None)
        self.f_der = getattr(self.fct, f_der)
        self.Hf = getattr(self.fct, Hf)

    def rechercheDuPas(self, x, d, tolR, maxIt):
        rho_0 = 10 * self.rho
        j = 1
        while abs(self.rho - rho_0) > tolR and j < maxIt:
            self.fct.set_x(x[0] + self.rho * d[0], x[1] + self.rho * d[1])
            phi_p = d.T @ self.f_der()
            phi_s = d.T @ self.Hf() @ d
            rho_0 = self.rho
            self.rho = self.rho - phi_p / phi_s
            j += 1
        return self.rho

    def gradientPasFixe(self):
        i = 0
        x = self.x0.copy()
        x_list = [x]
        self.fct.set_x(x[0], x[1])
        while np.linalg.norm(self.f_der()) > self.tol and i < self.Nitermax:
            d = -self.f_der()
            x += self.rho * d
            i += 1
            self.fct.set_x(x[0], x[1])
            x_list.append(x.copy())
        return x, x_list, i

    def gradientPasOptimal(self):

        i = 0
        x = self.x0
        x_list = [x]
        self.fct.set_x(x[0], x[1])
        while np.linalg.norm(self.f_der()) > self.tol and i < self.Nitermax:
            d = -self.f_der()
            rho = self.rechercheDuPas(x, d, 10 ** -8, 10 ** 4)
            x += rho * d
            i += 1
            self.fct.set_x(x[0], x[1])
            x_list.append(x)
        return x, x_list, i



if __name__ == '__main__':

    from functions import Functions
    from graph import Graph

    x0_1 = np.array([1.2, 1.2]).T
    pas_1 = 10 ** -2
    grad = Gradient(x0_1, pas_1, 10 ** -4, 10 ** 5, "g_der", "H_g")


    Sol1 = grad.gradientPasFixe()
    Sol2 = grad.gradientPasOptimal()
    print(Sol1[0], Sol1[2])
    print(Sol2[0], Sol2[2])

    fct = Functions(None, None)
    # graphical part
    gr = Graph(-3, 3, 0.1, fct, "g")
    gr.Surface()
    gr.Lignes_niveau([i for i in range(12)])
