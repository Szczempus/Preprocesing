import numpy as np
import matplotlib.pyplot as plt


def geomtery_definition_manual():
    wezly = np.array([[1, 0],
                      [2, 1],
                      [3, 0.5],
                      [4, 0.75]])
    elementy = np.array([[1, 1, 3],
                         [2, 4, 2],
                         [3, 3, 4]])
    warunki_brzegowe = [{'ind': 1, 'typ': 'D', 'wartosc': 1},
                        {'ind': 2, 'typ': 'D', 'wartosc': 2}]

    liczba_wezlow = np.shape(wezly)[0]

    return wezly, elementy, warunki_brzegowe, liczba_wezlow


def control_params(c: float, f: float):
    """

    :param c: constant
    :param f: constant
    :return: c, f
    """
    return c, f


def params_init(x_0: float, x_P: float, wwb_L: float, wwb_P: float, twb_L: str, twb_P: str):
    """

    x_0         =   początek przedziału
    x_P         =   koniec przedziału
    wwb_L       =   wartość warunku brzegowego lewego
    wwb_P       =   wartość warunku brzegowego prawego
    twb_L       =   typ warunku brzegowego lewego
    twb_P       =   typ warunku brzegowego prawego
    section     =   przedział obsazaru. Jego forma to lista zawierająca lewą i prawą stronę
                    np. [0, 10] - przedział od 0 do 6
    conditions  =   parametry wartości brzegowych. Jest to lista z lewym i prawym warunkiem
                    brzegowym [wartość warunku brzegowego lewego, wartość warunku brzegowego prawego]
    types       =   lista typów warunkó brzegowych. np ["D","N"], gdzie typem lewego warunku
                    jest warunek Dirchleta, a typem prawego jest warunek Neumann'a

    :param x_0: int
    :param x_P: int
    :param wwb_L: int
    :param wwb_P: int
    :param twb_L: string
    :param twb_P: string
    :return: przedział, wartości brzegowe, typy
    """

    przedzial = np.array([x_0, x_P])
    warunki_brzeg = np.array([wwb_L, wwb_P])
    typy = np.array([twb_L, twb_P])

    return przedzial, warunki_brzeg, typy


def geometry_definition_auto(poczatek: float, koniec: float, ilosc: int):
    lp = np.arange(1, ilosc + 1)
    x = np.linspace(poczatek, koniec, ilosc)
    wezly = (np.vstack((lp.T, x.T))).T

    lp = np.arange(1, ilosc)
    c1 = np.arange(1, ilosc)
    c2 = np.arange(2, ilosc + 1)
    elementy = (np.block([[lp], [c1], [c2]])).T

    return wezly, elementy


def geometry_plot(wezly: list, elementy: list, warunki_brzegowe: dict = None):
    fh = plt.figure()
    plt.plot(wezly[:, 1], np.zeros((np.shape(wezly)[0], 1)), '-bo')

    numer_wezlow = np.shape(wezly)[0]

    for i in np.arange(0, numer_wezlow):
        ind = wezly[i, 0]
        x = wezly[i, 1]
        plt.text(x, 0.01, str(int(ind)), c='b')
        plt.text(x, -0.01, str(x))

    numer_elementow = np.shape(elementy)[0]
    for i in np.arange(0, numer_elementow):
        wezel_pocz = elementy[i, 1]
        wezel_konc = elementy[i, 2]

        x = (wezly[wezel_pocz - 1, 1] + wezly[wezel_konc - 1, 1]) / 2
        plt.text(x, 0.01, str(i + 1), c='r')

    plt.show()


def base_functions(i):
    '''

    :param i: stopień funkcji bazowych dla elementu (do wyboru 1 lub 2)
    :return: funkcja bazowa i jej pochodna
    '''
    if i == 0:
        f = lambda x: 0 * x + 1
        df = lambda x: 0 * x
    elif i == 1:
        f = (lambda x: -1 / 2 * x + 1 / 2, lambda x: 0.5 * x + 0.5)
    elif i == 2:
        f = (lambda x: 1 / 2 * x * (x - 1), lambda x: -x ** 2 + 1, lambda x: 1 / 2 * x * (x + 1))
        df = (lambda x: x - 1 / 2, lambda x: -2 * x, lambda x: x + 1 / 2)
    else:
        raise Exception("Bład w funkcji bazowych. ")
    return f, df


def Aij(c, dphi1, dphi2, phi1, phi2):
    '''

    :param c: stała
    :param phi, dphi: kolejne funkcje dphi lub phi
    :return:
    '''
    return lambda x: -dphi1(x) * dphi2(x) + c * phi1(x) * phi2(x)


def mem_allocation(n: int):
    '''

    :param n: wielkość macierzy A i wektora b
    :return: tablice o rozmiarach nxn i nx1
    '''
    A = np.zeros([n, n])
    b = np.zeros([n, 1])
    return A, b
