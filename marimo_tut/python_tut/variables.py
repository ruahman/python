import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    _x = 5
    _y = "John"
    print(_x)
    print(_y)
    return


@app.cell
def _():
    # change value type
    _x = 4       # x is of type int
    _x = "Sally" # x is now of type str
    print(_x)
    return


@app.cell
def _():
    # cast to specifig type
    _x = str(3)    # x will be '3'
    _y = int(3)    # y will be 3
    _z = float(3)  # z will be 3.0
    return


@app.cell
def _():
    # get the type
    _x = 5
    _y = "John"
    print(type(_x))
    print(type(_y))
    return


@app.cell
def _():
    # single or double quotes
    _x = "John"
    # is the same as
    _x = 'John'
    return


@app.cell
def _():
    # case sensitive
    _a = 4
    _A = "Sally"
    return


@app.cell
def _():
    _x, _y, _z = "Orange", "Banana", "Cherry"
    print(_x)
    print(_y)
    print(_z)
    return


@app.cell
def _():
    # unpack a collection 
    _fruits = ["apple", "banana", "cherry"]
    _x, _y, _z = _fruits
    print(_x)
    print(_y)
    print(_z)
    return


@app.cell
def _():
    _x = "awesome"

    def _myfunc():
      print("Python is " + _x)

    _myfunc()
    return


@app.cell
def _():
    _x = "awesome"

    def _myfunc():
      _x = "fantastic"
      print("Python is " + _x)

    _myfunc()

    print("Python is " + _x)
    return


@app.cell
def _():
    def _myfunc():
      # this defines a global variable
      global x
      x = "fantastic"

    _myfunc()

    print("Python is " + x)
    return (x,)


if __name__ == "__main__":
    app.run()
