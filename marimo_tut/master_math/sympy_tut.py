import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import sympy
    import marimo as mo
    from IPython.display import display,Math
    sympy.init_printing()
    return Math, display, mo, np, sympy


@app.cell
def _(display, np, sympy):
    x,y = sympy.symbols('x,y')
    display(x)
    display(y + 4)
    display(x**y)
    display(x/y)
    display(np.sqrt(2))
    return x, y


@app.cell
def _(display, sympy):
    mu,alpha,sigma = sympy.symbols('mu,alpha,sigma')
    display(sympy.exp( (mu-alpha)**2 / (2*sigma) ))
    return alpha, mu, sigma


@app.cell
def _(x, y):
    _exp = x + 4 + 2 * y
    _exp.subs({x:-4, y: 3})
    return


@app.cell
def _(Math, display, sympy, x):
    _expr = 3/x 
    _latex = sympy.latex(_expr)
    display(Math(_latex))
    display(Math(sympy.latex(sympy.sympify('3/4'))))
    return


@app.cell
def _(display, x):
    _expr = x**2 + 4
    display(_expr)
    display(_expr.subs(x,-2))
    return


if __name__ == "__main__":
    app.run()
