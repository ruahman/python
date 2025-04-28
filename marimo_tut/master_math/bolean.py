import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    4 > 5
    return


@app.cell
def _():
    4 < 5
    return


@app.cell
def _():
    5 == 5
    return


@app.cell
def _(mo):
    _x = 2
    _left = 4 * _x + 3
    print(_left)
    _right = 17 - _x ** 2
    print(_right)
    mo.md(rf"""
    x = 2<br>
    $4x + 3 < 17 - x^2 = {_left < _right}$
    """)
    return


@app.cell
def _(mo):
    _x = 2
    _left = 8 * _x - 2
    print(_left)
    _right = -3 * _x + 42
    print(_right)
    mo.md(rf"""
    x = 2<br>
    $8x - 2 \leq -3x - 42 = {_left <= _right}$
    """)
    return


if __name__ == "__main__":
    app.run()
