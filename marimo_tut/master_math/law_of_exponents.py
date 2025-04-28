import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy
    from IPython.display import Math,display
    sympy.init_printing()
    return Math, display, mo, sympy


@app.cell
def _(mo):
    mo.md(
        r"""
        $$
        x^yx^z = x^{y+z}\\
        \frac{x^y}{x^z} = x^yx^{-z} = x^{y-z}\\
        x^yy^z = x^yy^z
        $$
        """
    )
    return


@app.cell
def _(display, sympy):
    x,y,z = sympy.symbols('x,y,z')
    _ex = x**y * x**z
    display(_ex)
    display(sympy.simplify(_ex))
    return x, y, z


@app.cell
def _(Math, display, sympy, x, y, z):
    ex1 = x**y * x**z 
    ex2 = x**y / x**z 
    ex3 = x**y * y**z

    display(Math("%s = %s" % (sympy.latex(ex1), sympy.latex(sympy.simplify(ex1)))))

    display(Math("%s = %s" % (sympy.latex(ex2), sympy.latex(sympy.simplify(ex2)))))

    display(Math("%s = %s" % (sympy.latex(ex3), sympy.latex(sympy.simplify(ex3)))))


    return ex1, ex2, ex3


if __name__ == "__main__":
    app.run()
