from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore
import numpy as np


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.a = coeffs
        self.b = coeffs
        self.c = coeffs
        self.delta = self.b ** 2 - 4*self.a * self.c
        self.degree = len(self.coeffs) - 1


    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        g, l = sorted((self, other), key=lambda x: len(x.coeffs), reverse=True)
        new_coeffs = []
        for i in range(len(g)):
            if i <= l.degree:
                new_coeffs.append(g.coeffs[i] + l.coeffs[i])
            else:
                new_coeffs.append(g.coeffs[i])
        new_poly = Poly2(*new_coeffs)
        return new_poly
        
    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        coeffs = [-coeff for coeff in other.coeffs]
        return self + Poly2(*coeffs)

    def __repr__(self):
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs.values())]) + ')'
        return msg

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        assert p1.__str__()=='2X^2 - 4X + 3'

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        if self.delta < 0 :
            return None
        elif self.delta == 0 :
            return -self.b / (2 * self.a)
        else :
            return ( (- self.b - sqrt(self.delta)) / (2 * self.a) ,
                     (- self.b + sqrt(self.delta)) / (2 * self.a) )

    def __val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        val = self.coeffs[0]
        pw = 1
        for k  in range(1, len(self.coeffs)) :
            pw = pw*x
            val = val + self.coeffs[k]*x
        return val

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        x = plt.plot(x_points[1], x_points[1], 1)
        y = plt.plot([self(c) for c in x])
        plt.grid()
        plt.title(f'{self.__str__()}')
        plt.plot(x, y)

if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)

    baz = [1, 1, 1]
    p2 = Poly2(*baz)

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2

    print(p1.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png
