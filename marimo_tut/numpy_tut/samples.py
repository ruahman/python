import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def _(mo):
    mo.md(r"""## scaler and array broadcasting""")
    return


@app.cell
def _(np):

    _arr = np.array([1,2,3])
    print(_arr + 10) # add 10 to each element
    return


@app.cell
def _(np):
    _matrix = np.array([[1,2,3],[4,5,6]])
    _vector = np.array([1,0,1])
    print(_matrix + _vector)
    return


@app.cell
def _(mo):
    mo.md(r"""# Aggregation Functions""")
    return


@app.cell
def _(np):
    _arr = np.array([[1,2,3], [4,5,6]])
    print("Sum: ", np.sum(_arr))
    print("Mean: ", np.mean(_arr))
    print("Max: ", np.max(_arr))
    print("Min: ", np.min(_arr))
    print("Standar Deviation: ", np.std(_arr))
    print("Sum along rows: ", np.sum(_arr, axis=1))
    print("Sum along cols: ", np.sum(_arr, axis=0))
    return


@app.cell
def _(mo):
    mo.md(r"""# Boolean Indexing and Filtering""")
    return


@app.cell
def _(np):
    _arr = np.array([1,2,3,4,5,6]) 
    evens = _arr[_arr % 2 == 0]
    print("Evens: ", evens)

    # all elements greater than 3 will be assigned 0
    _arr[_arr > 3] = 0
    print("Modified Array: ", _arr)
    return (evens,)


@app.cell
def _(mo):
    mo.md(r"""# Random Number Generation and Setting Seeds""")
    return


@app.cell
def _(np):
    np.random.seed(42) # so random is constant
    _random_array = np.random.rand(3,3)
    print(_random_array)
    return


@app.cell
def _(np):
    _random_integers = np.random.randint(0,20, size=(2,3))
    print(_random_integers)
    return


if __name__ == "__main__":
    app.run()
