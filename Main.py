import numpy as np
import matplotlib.pyplot as plt


# -----------------------
# private function
# -----------------------
def control_params(c, f):
    """
    
    :param c: constant
    :param f: constant
    :return: c, f
    """
    return c, f


def params_init(section, conditions, types):
    """

    section     =   przedział obsazaru. Jego forma to lista zawierająca lewą i prawą stronę
                    np. [0, 10] - przedział od 0 do 6
    conditions  =   parametry wartości brzegowych. Jest to lista z lewym i prawym warunkiem 
                    brzegowym 
    types       =   lista typów warunkó brzegowych. np ["D","N"], gdzie typem lewego warunku
                    jest warunek Dirchleta, a typem prawego jest warunek Neumann'a
                      
    :param section: numpy.ndarray
    :param conditions: numpy.ndaaray
    :param types: array of strings
    :return: section, conditions, types
    """
    return section, conditions, types


def geometry_definition(section, knots):
    """
    section     =   przedział obszaru w formacie [lewa strona, prawa strona]
    knosts      =   wektor numerów wezłów globalnych np. [0, 3, 4, 2]

    Funkcja liczy długość przedziału, ilość węzłów, ilość elementów i długość jednego elementu)

    :param section: numpy.ndarray
    :param knots: vector
    :return: length, number of knots, number of elements, length of element
    """
    x = section[1] - section[0]
    knots_num = len(knots)
    elem_num = knots_num - 1
    elem_length = x/elem_num

    return x, knots_num, elem_num, elem_length



# def genGeometricMatrix(x_0, x_p, n):
#     temp = (x_p - x_0) / (n - 1)
#     matrix = np.array([x_0])
#     i = []
#     for i in range(1, n, 1):
#         matrix = np.block([matrix, i * temp + x_0])
#     return i, matrix


# -----------------------
# end private function
# -----------------------
# -----------------------
# global variables
# -----------------------


# wezly = np.array([0, 1, 0.5, 0.75])
# elementy = np.array([[1, 3], [4, 2], [3, 4]])
#
# twb_L = "D"
# twb_P = "D"
# wwb_L = 0
# wwb_P = 1

# -----------------------
# end global variables
# -----------------------
# -----------------------
# main function
# -----------------------
if __name__ == '__main__':
    control_param = control_params(1, 5)
    print(f"Parametr sterujący c: {control_param[0]}\nParametr sterujący f: {control_param[1]}\n")
    params = params_init(section=[-2, 10], conditions=[-1, 5], types=["D", "N"])
    print(params)
# -----------------------
# end main function
# -----------------------
