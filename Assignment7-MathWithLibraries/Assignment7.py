from functools import reduce

import matplotlib.pyplot as plt
from sympy import *
import matplotlib.pyplot as mpl

""" These symbols are set here so that they are available through all the assignment. """
x, y, z, t, f, g, h = symbols('x y z t f g h')

########################### question 1.a ############################


def float_range(begin=0.0, end=10.0, step=0.1):  #ascending
    """
    This method is trying to enhance the functionality of the built-in function of python - "range". given the
    starting, ending and the intervals to be made, the function returns a list of numbers with the aforementioned
    intervals between the starting and ending points. the end points and the intervals must be in logical order to
    function, for example: 1 through 5 with the steps of 0.5 is logical but -5 through -10 in the steps of 0.3 isn't.
    :param begin [int] - A value to start from.
    :param end [int] - A value to end on.
    :param step [int] - A value for the intervals wanted.
    :return A [list] of numbers representing the all the start to end points with the spaces of steps.
    """
    return [0.0 if round((begin + (step * times)), 2) == -0.0 else round((begin + (step * times)), 2) for times in range(round((end + (-begin))/step) + 1)]


########################### question 1.b.1 ###########################


def create_quadratic_equation(symbol, a, b, c):
    """
    This is a simple method to create a quadratic equation as a string with 3 given parameters and a symbol for the
    equation, all using the sympify function from sympy.
    :param symbol [sympy.core.symbol.Symbol] - A sympy variable to represent x
    :param a, b, c [int] - The parameters of the equation
    :return A [sympy.core.symbol.Symbol] expression of the equation.
    @ to be noted: If it was up to me, I would have used the "factor" function - which returns a [sympy.core.mul.Mul]
      but dishes out the most convenient expression. Awesome nonetheless!
    """
    return factor(f'{a}*{symbol}**2 + {b}*{symbol} + {c}')

# print(create_quadratic_equation(x, 1, 2, 3))

########################### question 1.b.2 ###########################


def concatenating_expressions(exprs):
    """
    This method is responsible to break a list of expressions (using the "unpack operator" in python) and concatenate
    them right after. After the list (or tuple) of expressions is unpacked, the "Add" function in sympy concatenate
    all expressions together to on readable and usable equation.
    :param exprs [list]/[tuple] - A list or tuple containing mathematical expressions in the form of Symbols.
    :return A [sympy.core.symbol.Symbol] expression. The Add function is calculated first and then translated to Symbol.
    """
    return Symbol(str(Add(*exprs)))


########################### question 1.b.3 ###########################


def string_to_expressions(str_exprs):
    """
    This method is used to convert a string of expressions to a symbol type
    :param str_exprs [str] - The expression in string form, separated by commas, that we want to convert.
    :return A [sympy.core.add.Add] symbols inside of a list, seperated by commas.
    """
    return list(sympify(str_exprs))


########################### question 1.b.4 ###########################
# def sub_in_expr(expr, symbol):
#     return expr.subs({list(expr.free_symbols)[0]: symbol})


def sub_in_expr(expr, symbol):
    """
    This method is responsible to replace all occurrences of a symbol in an expression with a given value. if possible,
    calculating it.
    :param expr [sympy.core.symbol.Symbol] - A symbolic expression.
    :param symbol [Symbol / Integer] - A symbol or an integer to replace in the expression.
    :return The expression with the new symbol in it, if no symbols are left after the replacement, solves it.
    """
    return lambda too_many_x_in_this_project:  expr.subs({symbol: too_many_x_in_this_project})  #  list(expr.free_symbols)[0] instead of "symbol" in lambda would have gotten rid of the need to use symbol at all


########################### question 1.c ############################

def plot_expr(expr, symbol, start, end, step=1.0):
    """
    This method (IS SO COOL) is responsible to receive an expression, calculate its values for a given range and
    print its plot.
    :param expr [Symbolic expression] - A given expression.
    :param symbol [Symbol (da...)] - A symbol to calculate the graph by.
    :param start [integer] - Starting point for x values.
    :param end [integer] - Ending point for x values.
    :param step [integer] - An interval between x values
    :return Outputs a graph with information regarding its values.
    """
    # x = Symbol(symbol)
    symbol_values = []
    current_value = start
    while current_value <= end:
        symbol_values.append(current_value)
        current_value += step
    expr_values = [expr.evalf(subs={x: v}) for v in symbol_values]

    mpl.plot(symbol_values, expr_values, color='red')
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.title(f"A GRAPH OF THE FUNCTION: Y = {sympify(expr)}")
    mpl.grid(visible=True)
    mpl.figure(figsize=(1920/100, 1080/100))
    mpl.show()
    plt.savefig('line_plot.png')

plot_expr(tan(cos(sin(x**2))), x, -5, 5, 0.1)
########################### question 1.d.1 ###########################
# def derivative_func_recursive(expr, symbol, num): definitely wrong
#     if num == 0: return expr
#     return derivative_func_recursive(((expr(symbol + h) - expr(symbol))/h), symbol, 0), symbol, num - 1)


def derivative_func_recursive(expr, symbol, num):
    """
    This method is the entry function to the recursion.
    :param expr [Symbolic expression] - The given expression
    :param symbol [Symbol] - The symbol by which the derivative is calculated
    :param num [int] - the number of time we would like the derivative to occur
    :return returns the wrappers calculated derivative.
    """
    h = Symbol('h')

    def derivative_helper(expr, symbol, num):
        if num == 0:
            return expr
        expr = limit((expr.subs({symbol: symbol + h}) - expr) / h, h, 0)
        return derivative_helper(expr, symbol, num - 1)

    return derivative_helper(expr, symbol, num)


########################## question 1.d.2 ###########################


def graph_of_2_derivatives(expr, symbol, start, end, step=1.0):
    """
    This method (IS SO MUCH COOLER) is given an expression and prints the graphs for the expression and next
    2 derivatives. The graph includes a legend showing the names and colors of the different graphs.
    :param expr [Symbolic expression] - The given expression.
    :param symbol [Symbol] - The symbol to derive by.
    :param start [int] - Starting point for x values.
    :param end [integer] - Ending point for x values.
    :param step [integer] - An interval between x values
    :return Outputs a graph with information regarding its values.
    """
    # y = Symbol(symbol)
    symbol_values_all = []
    current_value = start
    while current_value <= end:
        symbol_values_all.append(current_value)
        current_value += step
    expr02 = derivative_func_recursive(expr, symbol, 1)
    expr03 = derivative_func_recursive(expr, symbol, 2)
    expr_values1 = [expr.evalf(subs={list(expr.free_symbols)[0]: v}) for v in symbol_values_all]
    expr_values2 = [expr02.evalf(subs={list(expr.free_symbols)[0]: v}) for v in symbol_values_all]
    expr_values3 = [expr03.evalf(subs={list(expr.free_symbols)[0]: v}) for v in symbol_values_all]

    mpl.plot(symbol_values_all, expr_values1, color='crimson', label=f"f({y})")#, label=f"f({y})"
    mpl.plot(symbol_values_all, expr_values2, color='green', label=f"f'({y})")#, label=f"f'({y})"
    mpl.plot(symbol_values_all, expr_values3, color='blue', label=f"f''({y})")#, label=f"f''({y})"
    mpl.legend()
    mpl.xlabel("x")
    mpl.ylabel("y")
    mpl.title(f"A GRAPH OF THE FUNCTION: Y = {sympify(expr)}")
    mpl.grid(visible=True)
    mpl.show()

graph_of_2_derivatives(x**2, x, -5, 5, 0.1)
##################### question 1.e - the final boss - B.F.G 9000 required to enter this stage ######################
########### The B.F.G 9000 is achieved by completing difficult challenges. It often symbolises the Doom  ###########
### franchise in general: over-the-top, merciless and vicious nature... really reminding me of this assignment... ##
# Hopefully this caught your eyes and brought you even a little smile, thank you for the effort you put up for us! #


def integral_func(expr, symbol, h=0.001):
    """
    This method is a mathematical calculation of an integral. With a given expression and symbol, returns the
    integral area value of the expression.
    :param expr [Symbolic expression] - The given expression.
    :param symbol [Symbol] - The symbol to integral by.
    :param h [int] - the delta by which to calculate the integral.
    :return [int] The calculated value of the integral.
    """
    return lambda a, b: h*reduce(lambda m, n: m + n, map(lambda d: expr.subs({list(expr.free_symbols)[0]: symbol}).evalf(subs={x: a + d}), [i * h for i in range(int((b - a) / h))]))
