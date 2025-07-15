import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def _(np):
    _arr = np.array([1,2,3,4])
    print(_arr)
    return


@app.cell
def _(np):
    zeros = np.zeros((3,3))
    print(zeros)
    return (zeros,)


@app.cell
def _(np):
    ones = np.ones((2,4))
    print(ones)
    return (ones,)


@app.cell
def _(np):
    range_array = np.arange(1, 10, 2)
    print(range_array)
    return (range_array,)


@app.cell
def _(np):
    linespace_array = np.linspace(0, 1, 5) # split it up 5 ways
    print(linespace_array)
    return (linespace_array,)


@app.cell
def _(np):
    _arr = np.array([1,2,3,4,5,6])
    reshaped = _arr.reshape((2,3))
    print(reshaped)
    return (reshaped,)


@app.cell
def _(np):
    _arr = np.array([1,2,3])
    expanded = _arr[:, np.newaxis]
    print(expanded) # create new axis for each element
    return (expanded,)


@app.cell
def _(np):
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    print(a + b)
    print(a * b)
    print(a / b)
    return a, b


@app.cell
def _(np):
    _arr = np.array([4, 16, 25])
    print(np.sqrt(_arr))
    print(np.sum(_arr))
    print(np.mean(_arr))
    print(np.max(_arr))
    return


@app.cell
def _(np, reshaped):
    _arr = np.array([10,20,30,40,50,60])
    print(_arr[2])
    print(_arr[-1])
    print(_arr[1:4])
    print(_arr[3:])
    _reshaped = _arr.reshape(2,3)
    print(reshaped)
    return


@app.cell
def _(np):
    _a = np.arange(1, 6)
    _b = np.arange(6, 11)
    return


if __name__ == "__main__":
    app.run()
