import numpy as np


class IterPower:

    def __init__(self, A, eps, nmax):
        self.A = A
        self.eps = eps
        self.nmax = nmax
        self.w = None
        self.old_w = None
        # generate x vector
        self.x = np.random.random(len(self.A))

    def w_sequence(self, k):
        w = (self.A ** k) * self.x / (np.linalg.norm((self.A ** k) * self.x))
        return w

    def c_sequence(self, w):
        c = self.A * w
        return c

    def iter(self):
        for k in range(1, self.nmax):
            print("k=", k)
            self.w = self.w_sequence(k)
            print(self.w, self.old_w)
            if self.old_w is not None:

                diff = np.linalg.norm(self.w - self.old_w)
                print(diff)
                if diff <= self.eps:
                    verif = True
                else:
                    verif = False
            else:
                verif = False

            if verif:
                print("abs() < eps")
                return
            else:
                self.old_w = self.w

                c = self.c_sequence(self.w)

        print("nmax reached")


if __name__ == '__main__':
    n = 3
    a = np.random.randint(0, 1000, size=(n, n))
    matA = (a + a.T)/2
    print(matA)
    iP = IterPower(matA, 10, 100)
    iP.iter()
