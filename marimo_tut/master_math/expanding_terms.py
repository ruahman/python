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
def _(mo):
    mo.md(
        r"""
        $$
        a(b + c) = ab + ac\\
        (a + b)(c + d) = ac + ad + bc + bd
        $$
        """
    )
    return


@app.cell
def _(display, sympy):
    from sympy.abc import x,y

    term1 = (4*x + 5)
    term2 = x 

    display(term1 * term2)
    display(sympy.expand(term1 * term2))
    return term1, term2, x, y


@app.cell
def _(display, sympy, term1, x):
    term3 = x - 7
    display(term1 * term3)
    display(sympy.expand(term1 * term3))
    return (term3,)


@app.cell
def _(display, sympy, x, y):
    _ex = x * (2*y**2 - 5**x/x)
    display(_ex)
    display(sympy.expand(_ex))
    return


@app.cell
def _(x, y):
    Fxy = (4+x)*(2-y)
    Fxy.subs({x:1,y:0})
    return (Fxy,)


if __name__ == "__main__":
    app.run()
