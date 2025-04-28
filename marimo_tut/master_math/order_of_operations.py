import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""**P**lease **E**xcuse **M**y **D**ear **A**unt **S**ally""")
    return


@app.cell
def _(mo):
    mo.md(r"""PENDAS""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        Parentheses <br> 
        Exponents <br>
        Multiplication <br>
        Division <br>
        Addition <br>
        Subtraction
        """
    )
    return


@app.cell
def _(mo):
    _x = ( (4+3) * (2-1) )
    mo.md(rf'''
    $4 + 3 \times (2 - 1) = {_x}$
    ''')
    return


@app.cell
def _(mo):
    _x = int(4*5 / (7 + 3))
    mo.md(rf"""
    $4 \times 5 \div (7 + 3) = {_x}$
    """)
    return


@app.cell
def _(mo):
    _x = 9 / (3 + 6) - 1
    mo.md(rf"""
    $9 \div (3 + 6) = {_x}$
    """)
    return


if __name__ == "__main__":
    app.run()
