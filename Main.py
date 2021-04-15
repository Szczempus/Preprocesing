import numpy as np
import matplotlib.pyplot as plt


# -----------------------
# private function
# -----------------------
def params_init( ):

    return params


def genGeometricMatrix(x_0, x_p, n):
    temp = (x_p - x_0) / (n - 1)
    matrix = np.array([x_0])
    i = []
    for i in range(1, n, 1):
        matrix = np.block([matrix, i * temp + x_0])
    return i, matrix

# -----------------------
# end private function
# -----------------------
# -----------------------
# global variables
# -----------------------
wezly = np.array([0, 1, 0.5, 0.75])
elementy = np.array([[1, 3], [4, 2], [3, 4]])

twb_L = "D"
twb_P = "D"
wwb_L = 0
wwb_P = 1

# -----------------------
# end global variables
# -----------------------
# -----------------------
# main function
# -----------------------
if __name__ == '__main__':
    num, matrix = genGeometricMatrix(0, 4, 10)
    print(f'liczba wezłów {num+1},\n\twartości {matrix}\n\t')
    # [parametry_sterujace] = params_init()

# -----------------------
# end main function
# -----------------------
