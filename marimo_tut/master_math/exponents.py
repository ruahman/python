import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    from IPython.display import display, Math
    return Math, display


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# The law of exponents""")
    return


@app.cell
def _(Math, display):
    _x = 3 ** 2
    display(Math("3^2 = 3 \\times 3 = %g" % (_x)))
    return


@app.cell
def _(Math, display):
    _x = 3 ** 4
    display(Math("3^4 = 3 \\times 3 \\times 3 \\times 3 = %g" % (_x)))
    return


@app.cell
def _(Math, display):
    _x = 3**2 * 3** 4
    display(Math("3^2 \\times 3^4= 3^{2 + 4} = 3^6 = %g" % (_x)))
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        you can only add exponents if bases are simular

        $3^2 \times 4^3 = 3 + 3 + 4 + 4 + 4$
        """
    )
    return


@app.cell
def _(mo):
    _x = 3**(2 + 4)
    mo.md(rf"""
    $3^{{2 + 4}} = {_x}$ 
    """)
    return


@app.cell
def _(mo):
    _x = int(4**(1/2))
    mo.md(rf"""
    $\sqrt{4} = {_x}$
    """)
    return


@app.cell
def _(mo):
    mo.md("""x = 5&nbsp;&nbsp;&nbsp;&nbsp;y = 5.1""")
    return


@app.cell
def _(mo):
    _x = 5
    _y = 5.1 

    _res = _x**(3/4) * 4**_y

    mo.md(rf"""
    $x^{{ 3/4 }} \times 4^y= {_res}$
    """)
    return


@app.cell
def _(mo):
    _x = 5
    _y = 5.1 

    _res = 3**3/_x**_y

    mo.md(rf"""
    $\frac{{3^3}}{{x^y}} = {_res}$
    """)
    return


@app.cell
def _(mo):
    _x = 5
    _y = 5.1 

    _res = 10**(_x - 4)

    mo.md(rf"""
    $10^{{x-4}}={_res}$
    """)
    return


if __name__ == "__main__":
    app.run()
