import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    x = 7
    x
    return (x,)


@app.cell
def _(x):
    x - 2
    return


@app.cell
def _(x):
    _x = x 
    print(_x)
    _x = 10
    _x
    return


@app.cell
def _():
    _x = 10
    _x = _x - 2*5
    _x
    return


@app.cell
def _():
    _x = 10
    _y = 20
    _z = 31
    print(_x + _y * _z)
    print(_x - _y * _z)
    return


@app.cell
def _():
    mike = 10
    spike = 34

    mike + spike
    return mike, spike


@app.cell
def _():
    _x = 7
    _y = -2
    _z = 5

    print(3 * _x * (4 + _y))
    print(-_y - (_x + 3)/_z)
    return


if __name__ == "__main__":
    app.run()
