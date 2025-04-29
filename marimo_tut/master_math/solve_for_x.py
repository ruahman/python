import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy
    from IPython.display import Math,display
    return Math, display, mo, sympy


@app.cell
def _(sympy):
    x = sympy.symbols('x') 

    expr = 2*x + 4 - 9 # setup a homgouns equation 2x + 4 - 9 = 0
    sympy.solve(expr) # solve for x
    return expr, x


@app.cell
def _(expr, mo, sympy):
    mo.md(r"""
    $$
    %s\\
    x=%s
    $$
    """ % (sympy.latex(expr), sympy.solve(expr)[0]))
    return


@app.cell
def _(sympy, x):
    sympy.solve(x**2 - 4)
    return


@app.cell
def _(display, sympy, x):
    y = sympy.symbols('y')
    _expr = x/4 - x*y + 5
    display(_expr)
    display(sympy.solve(_expr,x)[0]) # solve for x
    display(sympy.solve(_expr,y)[0]) # solve for y


    return (y,)


if __name__ == "__main__":
    app.run()
