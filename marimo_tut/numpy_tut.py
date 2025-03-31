import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        numpy is a multi dimensional array library in python.

        python does not have array but lists and list can 
        store many differt types

        also list are slow while numpy is fast
        - that is because numpy uses fixed types
        - you don't have to do typechecking for each element

        **continuous memory** 
        all element are arranged together in memory
        and not scatterd about like lists

        a matlab replacement????

        useful for plotting (Matplotlib)
        Backend(Pandas)
        Machine Learning
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np

    arr = np.array([1, 2, 3, 4, 5])

    print(arr)

    print(type(arr))
    return arr, np


@app.cell
def _(np):
    a1 = np.array([1,2,3],dtype='int16')
    a1
    return (a1,)


@app.cell
def _(np):
    b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
    b
    return (b,)


@app.cell
def _(a1):
    a1.ndim
    return


@app.cell
def _(b):
    b.ndim
    return


@app.cell
def _(a1):
    a1.shape
    return


@app.cell
def _(b):
    b.shape
    return


@app.cell
def _(a1):
    a1.dtype
    return


@app.cell
def _(b):
    b.dtype
    return


@app.cell
def _(a1):
    a1.itemsize
    return


@app.cell
def _(np):
    a2 = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
    print(a2)
    return (a2,)


@app.cell
def _(a2):
    a2[0,:]
    return


@app.cell
def _(a2):
    a2[:,2]
    return


@app.cell
def _(a2):
    a2[0,1:6:2]
    return


@app.cell
def _(a2):
    _a = a2 
    _a[1,5] = 20
    print(_a)
    return


@app.cell
def _(mo):
    mo.md(r"""### fill by zeros""")
    return


@app.cell
def _(np):
    np.zeros(())
    return


@app.cell
def _(np):
    np.zeros((2,3,3))
    return


@app.cell
def _(mo):
    mo.md(r"""### fill by ones""")
    return


@app.cell
def _(np):
    np.ones((4,2,2))
    return


@app.cell
def _(mo):
    mo.md(r"""### fill anyting""")
    return


@app.cell
def _(np):
    np.full((2,2), 99, dtype='float32')
    return


@app.cell
def _(mo):
    mo.md(r"""### fill random""")
    return


@app.cell
def _(np):
    np.random.rand(4,2)
    return


@app.cell
def _(mo):
    mo.md(r"""### identity matrix""")
    return


@app.cell
def _(np):
    np.identity(5)
    return


@app.cell
def _(mo):
    mo.md(r"""### mathematics""")
    return


@app.cell
def _(np):
    a3 = np.array([1,2,3,4])
    return (a3,)


@app.cell
def _(a3):
    a3 + 2
    return


@app.cell
def _(a3):
    a3 - 2
    return


@app.cell
def _(a3):
    a3 * 2
    return


@app.cell
def _(a3):
    a3 ** 2
    return


@app.cell
def _(a3, np):
    np.sin(a3)
    return


@app.cell
def _(mo):
    mo.md(r"""### linear algerbra""")
    return


@app.cell
def _(a3, np):
    b2 = np.array([1,0,1,0])
    a3 + b2
    return (b2,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ### statistics 
        min, max, ave,
        """
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
