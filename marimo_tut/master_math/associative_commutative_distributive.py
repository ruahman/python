import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import sympy as sym
    return mo, sym


@app.cell
def _(mo):
    mo.md(
        r"""
        # The associative rule
        $$
        2(3 \times 4) = (2 \times 3)4\\
        2(12) = (6)4\\
        24 = 24
        $$

        it doesn't matter where you start multiplying

        $$
        a(b \times c) = (a \times b)c\\
        a(bc) = (ab)c\\
        abc = abc
        $$
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # The commutiative rule
        $$
        a \times b = b \times a
        $$
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        # The distributive rule 
        $$
        x(y + z) = xy + xz
        $$
        """
    )
    return


@app.cell
def _():
    # associative
    from sympy.abc import x,y 

    expr1 = x*(4*y)
    expr2 = (x*4)*y

    print(expr1 - expr2)
    return expr1, expr2, x, y


@app.cell
def _(x, y):
    # commutative
    e1 = 4*x*y
    e2 = x*4*y
    e3 = x*y*4 

    print(e1.subs({x:3,y:2}))
    print(e2.subs({x:3,y:2}))
    print(e3.subs({x:3,y:2}))
    return e1, e2, e3


@app.cell
def _(sym):
    # distributive 
    a,b,c,d = sym.symbols('a,b,c,d')
    ex1 = (a+b)*(c+d)
    sym.expand(ex1)
    return a, b, c, d, ex1


@app.cell
def _(mo):
    mo.md(
        r"""
        # Exersises 
        $$
        f_1 = x(y + z)
        $$

        $$
        f_2 = \frac{3}{x} + x^2
        $$

        $$
        x_1 = w(4 -w) + \frac{1}{w^2}(1 + w)
        $$
        """
    )
    return


@app.cell
def _(sym, x, y):
    z,w = sym.symbols('z w')
    x1 = w*(4-w) + 1/w**2 * (1*w)
    f1 = x*(y + z)
    f2 = 3/x + x**2

    print((f1 * f2) - (f2 * f1))
    return f1, f2, w, x1, z


if __name__ == "__main__":
    app.run()
