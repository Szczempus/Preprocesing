import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------------------------------------------------
# private function
# ----------------------------------------------------------------------------------------------------------------------

def control_params(c, f):
    """
    
    :param c: constant
    :param f: constant
    :return: c, f
    """
    return c, f


def params_init(x_0, x_P, wwb_L, wwb_P, twb_L, twb_P):
    """

    x_0         =   początek przedziału
    x_0         =   koniec przedziału
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


def geometry_definition(przedzial, wezly):
    """

    section     =   przedział obszaru w formacie [lewa strona, prawa strona]
    knosts      =   wektor numerów wezłów globalnych np. [0, 3, 4, 2]

    Funkcja liczy długość przedziału, ilość węzłów, ilość elementów i długość jednego elementu)

    :param przedzial: numpy.ndarray
    :param wezly: vector
    :return: długość przedziału, liczba węzłów, liczba elementów, długość elementów, węzły początkowe i końcowe elementów
    """
    x = przedzial[1] - przedzial[0]
    knots_num = len(wezly)
    elem_num = knots_num - 1
    elem_length = x / elem_num
    elem_length = np.around(elem_length, 1)
    elem_array = []
    nodes = np.array([przedzial[0]])

    for i in range(knots_num - 1):
        elem_array.append(np.array([wezly[i], wezly[i + 1]]))
    for i in range(knots_num):
        nodes = np.block([nodes, i * elem_length + przedzial[0]])

    return x, knots_num, elem_num, elem_length, elem_array, nodes


def geometry_plot(section, knots, types):
    """
    section   =   zakres poczatku i końca przedziału [początek przedzału, koniec przedziału]


    :param section: numpy.ndarray
    :param knots:
    :param types:
    :return:
    """
    plt.plot(section[0], 0, '*')
    plt.plot(section[1], 0, '*')
    plt.plot(section, [0, 0])
    plt.plot(knots, np.zeros(len(knots)), '*')

    plt.text(section[0] - 0.15, 0, types[0])
    plt.text(section[1] + 0.15, 0, types[1])

    for i in range(0, len(knots)):
        plt.text(knots[i] - 0.03, 0.01, str(knots[i]))
        plt.text(knots[i] - 0.05, -0.05, str(i + 1))

    for i in range(0, len(knots) - 1):
        print((knots[i] - knots[i + 1]) / 2)
        plt.text(knots[i] / 2 + knots[i + 1] / 2, 0.05, str(i + 1))

    plt.xlim([section[0] - 0.3, section[1] + 0.3])
    plt.ylim([-0.2, 0.42])

    plt.show()


def geometry_definition_auto(x_0, x_p, n):
    """

    :param x_0: float first element
    :param x_p: float last element
    :param n: number of knots
    :return:
    """

    return


def base_functions(i):
    if i == 0:
        f = lambda x: 0 * x + 1
        df = lambda x: 0 * x
    elif i == 1:
        f = (lambda x: -1 / 2 * x + 1 / 2, lambda x: 0.5 * x + 0.5)
        df = (lambda x: -1 / 2 + 0 * x, lambda x: 0.5)
    # TODO elif i == 2:
    #     f =
    #     df =
    else:
        raise Exception("Bład w funkcji bazowych. ")
    return f, df


def Aij(dphi1, dphi2, c, phi1, phi2):
    Aij = lambda x: -dphi1(x) * dphi2(x) + c * phi1(x) * phi2(x)
    return Aij


# def genGeometricMatrix(x_0, x_p, n):
#     temp = (x_p - x_0) / (n - 1)
#     matrix = np.array([x_0])
#     i = []
#     for i in range(1, n, 1):
#         matrix = np.block([matrix, i * temp + x_0])
#     return i, matrix


# ----------------------------------------------------------------------------------------------------------------------
# end private function
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# global variables
# ----------------------------------------------------------------------------------------------------------------------


# wezly = np.array([0, 1, 0.5, 0.75])
# elementy = np.array([[1, 3], [4, 2], [3, 4]])
#
# twb_L = "D"
# twb_P = "D"
# wwb_L = 0
# wwb_P = 1

# ----------------------------------------------------------------------------------------------------------------------
# end global variables
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
# main function
# ----------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    c = 0
    f = lambda x: 0

    control_param = control_params(c=f, f=f)
    print(f"Parametr sterujący c: {control_param[0]}\nParametr sterujący f: {control_param[1]}\n")

    params = params_init(x_0=-2, x_P=20, wwb_L=-1, wwb_P=5, twb_L="D", twb_P="N")
    print(params)

    geometry = geometry_definition(przedzial=params[0], wezly=[1, 3, 4, 5, 6, 7, 8, 2])
    print(geometry)

    geometry_plot(section=params[0], knots=geometry[5], types=params[2])

    phi, dphi = base_functions(1)

    # xx = np.linspace(-1, 1, 101)
    # plt.plot(xx, phi[0](xx), 'r')
    # plt.plot(xx, phi[1](xx), 'g')
    # plt.plot(xx, dphi[0](xx), 'b')
    # plt.plot(xx, dphi[1](xx), 'c')
    # plt.show()
    liczbaElementow = geometry[3]
    for ee in np.arange(0, liczbaElementow):
        elemIndRow = ee

# ----------------------------------------------------------------------------------------------------------------------
# end main function
# ----------------------------------------------------------------------------------------------------------------------
