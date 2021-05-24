import numpy as np
import matplotlib.pyplot as plt
import FemFunctions as ff
import scipy.integrate as spint

# ----------------------------------------------------------------------------------------------------------------------
# private function
# ----------------------------------------------------------------------------------------------------------------------


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

    poczatek = 0
    koniec = 3
    n = 5
    wezly, elementy = ff.geometry_definition_auto(poczatek, koniec, n)
    warunki_brzegowe = [{'ind': 1, 'typ': 'D', 'wartosc': 1},
                        {'ind': 2, 'typ': 'D', 'wartosc': 2}]

    ff.geometry_plot(wezly, elementy)

    [A, b] = ff.mem_allocation(n)

    stopien_funkcji_baz = 1
    phi, dphi = ff.base_functions(stopien_funkcji_baz)

    # xx = np.linspace(-1, 1, 101)
    # plt.plot(xx, phi[0](xx), 'r')
    # plt.plot(xx, phi[1](xx), 'g')
    # plt.plot(xx, phi[2](xx), 'b')
    # plt.plot(xx, dphi[0](xx), 'c')
    # plt.plot(xx, dphi[1](xx), 'm')
    # plt.plot(xx, dphi[2](xx), 'y')
    # plt.show()

    for indeks_elementu in np.arange(0, np.shape(elementy)[0]):
        indeks_globalny_pocz = elementy[indeks_elementu, 1]
        indeks_globalny_konc = elementy[indeks_elementu, 2]
        globalne_indeksy = np.array([indeks_globalny_pocz, indeks_globalny_konc])

        x_a = wezly[indeks_globalny_pocz - 1, 1]
        x_b = wezly[indeks_globalny_konc - 1, 1]

        J = (x_b - x_a) / 2

        M = np.zeros([stopien_funkcji_baz + 1, stopien_funkcji_baz + 1])

        for n in range(stopien_funkcji_baz + 1):
            for m in range(stopien_funkcji_baz + 1):
                val = spint.quad(ff.Aij(c, dphi[n], dphi[m], phi[n], phi[m]), -1, 1)[0]
                M[n, m] = J * val

        A[np.ix_(globalne_indeksy - 1, globalne_indeksy - 1)] += M

        if warunki_brzegowe[0]['typ'] == 'D':
            indeks_wezla = warunki_brzegowe[0]['ind']
            wartosc_war_brzeg = warunki_brzegowe[0]['wartosc']

            indeks_wezla_poczatkowego = indeks_wezla - 1

            wzmacniacz = 10 ** 14

            b[indeks_wezla_poczatkowego] = A[
                                               indeks_wezla_poczatkowego, indeks_wezla_poczatkowego] * wzmacniacz * wartosc_war_brzeg
            A[indeks_wezla_poczatkowego, indeks_wezla_poczatkowego] = A[
                                                                          indeks_wezla_poczatkowego, indeks_wezla_poczatkowego] * wzmacniacz

    if warunki_brzegowe[1]['typ'] == 'D':
        indeks_wezla = warunki_brzegowe[1]['ind']
        wartosc_war_brzeg = warunki_brzegowe[1]['wartosc']

        indeks_wezla_poczatkowego = indeks_wezla - 1

        wzmacniacz = 10 ** 14

    b[indeks_wezla_poczatkowego] = A[
                                       indeks_wezla_poczatkowego, indeks_wezla_poczatkowego] * wzmacniacz * wartosc_war_brzeg
    A[indeks_wezla_poczatkowego, indeks_wezla_poczatkowego] = A[
                                                                  indeks_wezla_poczatkowego, indeks_wezla_poczatkowego] * wzmacniacz

    u = np.linalg.solve(A, b)

    ff.plot_solution(wezly, elementy, warunki_brzegowe, u)

# ----------------------------------------------------------------------------------------------------------------------
# end main function
# ----------------------------------------------------------------------------------------------------------------------
