import math 
import numpy as np
import matplotlib.pyplot as plt

"""Piecewise-linear Interpolation. (Code 0)."""
def piecewise_linear( down, nom, up, alpha):
    delta_up = up - nom
    delta_down = nom - down
    if alpha > 0:
        delta = delta_up * alpha
    else:
        delta = delta_down * alpha
    return delta + nom

"""Piecewise-Exponential Interpolation (Code 1)."""
def piecewise_exponential( down, nom, up, alpha):
    delta_up = up / nom
    delta_down = down / nom
    if alpha > 0:
        delta = math.pow(delta_up, alpha)
    else:
        delta = math.pow(delta_down, (-alpha))
    return delta * nom

"""Quadratic Interpolation (Code 2)."""
def quadratic( down, nom, up, alpha):
    a = 0.5 * (up + down) - nom
    b = 0.5 * (up - down)
    if -1 <= alpha <= 1:
        delta = a * alpha * alpha + b * alpha
    elif alpha > 1:
        delta = (b + 2 * a) * (alpha - 1)
    else:
        delta = (b - 2 * a) * (alpha + 1)
    if -1 <= alpha <= 1:
        return delta + nom
    if alpha > 1:
        return delta + quadratic( down, nom, up, 0.999999) 
    else:
        return delta + quadratic( down, nom, up, -0.99999999)


"""Polynomial Interpolation (Code 4)."""

def polinomial( down, nom, up, alpha):
    delta_up = up / nom
    delta_down = down / nom
    if alpha >= 1:
        delta = math.pow(delta_up, alpha)
    elif -1 < alpha < 1:
        delta_up_alpha0 = math.pow(delta_up, 1)
        delta_down_alpha0 = math.pow(delta_down, 1)
        b = [
            delta_up_alpha0 - 1,
            delta_down_alpha0 - 1,
            math.log(delta_up) * delta_up_alpha0,
            -math.log(delta_down) * delta_down_alpha0,
            math.pow(math.log(delta_up), 2) * delta_up_alpha0,
            math.pow(math.log(delta_down), 2) * delta_down_alpha0,
            ]
        A_inverse = [
            [
                15.0 / (16 * 1),
                -15.0 / (16 * 1),
                -7.0 / 16.0,
                -7.0 / 16.0,
                1.0 / 16 * 1,
                -1.0 / 16.0 * 1,
                ],
            [
                3.0 / (2 * math.pow(1, 2)),
                3.0 / (2 * math.pow(1, 2)),
                -9.0 / (16 * 1),
                9.0 / (16 * 1),
                1.0 / 16,
                1.0 / 16,
                ],
            [
                -5.0 / (8 * math.pow(1, 3)),
                 5.0 / (8 * math.pow(1, 3)),
                 5.0 / (8 * math.pow(1, 2)),
                 5.0 / (8 * math.pow(1, 2)),
                 -1.0 / (8 * 1),
                 1.0 / (8 * 1),
                 ],
            [
                3.0 / (-2 * math.pow(1, 4)),
                3.0 / (-2 * math.pow(1, 4)),
                -7.0 / (-8 * math.pow(1, 3)),
                7.0 / (-8 * math.pow(1, 3)),
                -1.0 / (8 * math.pow(1, 2)),
                -1.0 / (8 * math.pow(1, 2)),
                ],
            [
                3.0 / (16 * math.pow(1, 5)),
                -3.0 / (16 * math.pow(1, 5)),
                -3.0 / (16 * math.pow(1, 4)),
                -3.0 / (16 * math.pow(1, 4)),
                1.0 / (16 * math.pow(1, 3)),
                -1.0 / (16 * math.pow(1, 3)),
                ],
            [
                1.0 / (2 * math.pow(1, 6)),
                1.0 / (2 * math.pow(1, 6)),
                -5.0 / (16 * math.pow(1, 5)),
                5.0 / (16 * math.pow(1, 5)),
                1.0 / (16 * math.pow(1, 4)),
                1.0 / (16 * math.pow(1, 4)),
                ],
            ]
        
        coefficients = [
            sum([A_i * b_j for A_i, b_j in zip(A_row, b)]) for A_row in A_inverse
            ]
        delta = 1
        for i in range(1, 7):
            delta += coefficients[i - 1] * math.pow(alpha, i)
    else:
        delta = math.pow(delta_down, (-alpha))
    return delta*nom


if __name__ == '__main__':
    print('Ciao')
    for down,nom,up in [(0.85,1,1.15),(1.2,1,1.8),(0.1,1,1.9),(0.95,1,1.5)]:
        list_piecewise_linear = []
        list_piecewise_exponential = []
        list_quadratic = []
        list_polinomial = []
        list_alpha = []
        for alpha in np.linspace(-2,2,200):
        #print("alpha",alpha)
            val_piecewise_linear = piecewise_linear( down, nom, up, alpha) 
        #print("val_piecewise_linear",val_piecewise_linear)
            val_piecewise_exponential = piecewise_exponential( down, nom, up, alpha) 
        #print("val_piecewise_exponential",val_piecewise_exponential)
            val_quadratic = quadratic( down, nom, up, alpha)
        #print("val_quadratic",val_quadratic)
            val_polinomial = polinomial( down, nom, up, alpha)
        #print("val_polinomial",val_polinomial)
        #print('')
            list_alpha.append(alpha)
            list_piecewise_linear.append(val_piecewise_linear)
            list_piecewise_exponential.append(val_piecewise_exponential)
            list_quadratic.append(val_quadratic)
            list_polinomial.append(val_polinomial)
            list_one = [1 for i in list_alpha]
        plt.plot(list_alpha, list_one, color='black')
        plt.plot(list_alpha, list_piecewise_linear, label='Piecewise Linear')
        plt.plot(list_alpha, list_piecewise_exponential, label='Piecewise exponential')
        plt.plot(list_alpha, list_quadratic, label='Quadratic')
        plt.plot(list_alpha, list_polinomial, label='Polinomial')
        plt.plot([-1, 0, 1], [down, nom, up], 'o', color='pink',markersize=12)
        plt.legend(loc='best', shadow=False, fontsize='large')
        plt.xlabel(r"$\theta$", fontsize='large')
        plt.ylabel(r"b($\theta$)", fontsize='large')
        plt.grid(True)
        plt.savefig('../'+str(down).replace('.','-')+'_'+str(nom).replace('.','-')+'_'+str(up).replace('.','-')+'.pdf')
        plt.close()
        
