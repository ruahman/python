import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    from IPython.display import display, Math
    return Math, display


@app.cell
def _(display):
    display("4 + 3 = 7")
    return


@app.cell
def _(display):
    display("4 + 3 = " + str(4 + 3))
    return


@app.cell
def _(Math, display):
    display(Math('4 + 3 = 7'))
    return


@app.cell
def _(Math, display):
    x = 4
    y = 5
    display(Math(str(x) + " + " + str(y) + " = " + str(x + y)))
    return x, y


@app.cell
def _(Math, display, x, y):
    display(Math("%g + %g = %g" % (x,y,x+y)))
    return


@app.cell
def _(Math, display):
    display(Math("\\frac{4}{5} = .8"))
    return


@app.cell
def _(Math, display):
    _x = 3.4 
    _y = 17

    display(Math('%g \\times %g = %g' % (_x, _y, _x * _y)))
    return


@app.cell
def _(Math, display):
    _x = 7
    _y = -2
    _z = 5
    ans = 3*_x*(4+_y)
    display(Math('3\\times%g(4%g) = %g' % (_x,_y,ans)))
    return (ans,)


@app.cell
def _(Math, ans, display):
    _x = 7
    _y = -2
    _z = 5
    _ans = -_y - (_x+3)/_z
    display(Math("%g - \\frac{%g+3}{%g} = %g" % (_y,_x,_z,ans)))
    return


if __name__ == "__main__":
    app.run()
