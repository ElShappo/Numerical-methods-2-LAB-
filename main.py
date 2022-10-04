import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


def func(x):
    return np.exp(-2*x) * np.cos(x)


def deriv1(x):
    return -np.exp(-2 * x) * (np.sin(x) + 2 * np.cos(x))


def deriv2(x):
    return 2 * np.exp(-2 * x) * (np.sin(x) + 2 * np.cos(x)) - np.exp(-2 * x) * (np.cos(x) - 2 * np.sin(x))


def central_dif(x, h):
    return (func(x+h) - func(x-h)) / (2 * h)


def forward_dif(x, h):
    return (func(x+h)-func(x)) / h


def central_dif2_order2(x, h):
    return (func(x-h)+func(x+h)-2*func(x))/(h**2)


def central_dif2_order4(x, h):
    return (-func(x-2*h) + 16*func(x-h)-30*func(x) + 16*func(x+h) - func(x+2*h)) / (12 * (h**2))


def get_relative_error_list(list1, list2):
    return list(map(lambda x, y: abs(x - y)/abs(y)*100, list1, list2))


def main():
    a, b, step = -0.8,   0.8,   0.2

    uniform_nodes = np.arange(a, b, step)

    analytic_deriv1_list = list(map(deriv1, uniform_nodes)) # values of 1st deriv in nodes
    analytic_deriv2_list = list(map(deriv2, uniform_nodes)) # values of 2nd deriv in nodes

    numeric_central_dif_list = [central_dif(x, step) for x in uniform_nodes]
    numeric_forward_dif_list = [forward_dif(x, step) for x in uniform_nodes]

    numeric_central_dif2_order2_list = \
        [central_dif2_order2(x, step) for x in uniform_nodes]
    numeric_central_dif2_order4_list = \
        [central_dif2_order4(x, step) for x in uniform_nodes]


    plt.subplot(2, 2, 1)
    plt.title("Первая производная,\n правые разности")
    plt.xlabel("x")
    plt.ylabel("y'")
    plt.grid()
    plt.plot(uniform_nodes, numeric_forward_dif_list, color='k', label='Численное значение')
    plt.plot(uniform_nodes, analytic_deriv1_list, ls='--', color='k', label='Аналитическое значение')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.title("Погрешность \n для правых разностей (%)")
    plt.xlabel("x")
    plt.ylabel("ε")
    plt.grid()
    plt.plot(uniform_nodes, get_relative_error_list(numeric_forward_dif_list, analytic_deriv1_list),
             ls='dotted', color='b', label='Погрешность')

    plt.subplot(2, 2, 3)
    plt.title("Первая производная,\n центральные разности")
    plt.xlabel("x")
    plt.ylabel("y'")
    plt.grid()
    plt.plot(uniform_nodes, numeric_central_dif_list, color='k', label='Численное значение')
    plt.plot(uniform_nodes, analytic_deriv1_list, ls='--', color='k', label='Аналитическое значение')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.title("Погрешность \n для центральных разностей (%)")
    plt.xlabel("x")
    plt.ylabel("ε")
    plt.grid()
    plt.plot(uniform_nodes, get_relative_error_list(numeric_central_dif_list, analytic_deriv1_list),
             ls='dotted', color='b', label='Погрешность')

    plt.show()


    # -----------------------------------------------------

    plt.subplot(2, 2, 1)
    plt.title("Вторая производная,\n 2-й порядок точности")
    plt.xlabel("x")
    plt.ylabel("y''")
    plt.grid()
    plt.plot(uniform_nodes, numeric_central_dif2_order2_list, color='k', label='Численное значение')
    plt.plot(uniform_nodes, analytic_deriv2_list, ls='--', color='k', label='Аналитическое значение')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.title("Погрешность \n (2-й порядок точности) (%)")
    plt.xlabel("x")
    plt.ylabel("ε")
    plt.grid()
    plt.plot(uniform_nodes, get_relative_error_list(numeric_central_dif2_order2_list, analytic_deriv2_list),
             ls='dotted', color='b', label='Погрешность')

    plt.subplot(2, 2, 3)
    plt.title("Вторая производная,\n 4-й порядок точности")
    plt.xlabel("x")
    plt.ylabel("y''")
    plt.grid()
    plt.plot(uniform_nodes, numeric_central_dif2_order4_list, color='k', label='Численное значение')
    plt.plot(uniform_nodes, analytic_deriv2_list, ls='--', color='k', label='Аналитическое значение')
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.title("Погрешность \n (4-й порядок точности) (%)")
    plt.xlabel("x")
    plt.ylabel("ε")
    plt.grid()
    plt.plot(uniform_nodes, get_relative_error_list(numeric_central_dif2_order4_list, analytic_deriv2_list),
             ls='dotted', color='b', label='Погрешность')

    plt.show()



main()
