import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell
def _():
    c = 7
    d = 7.0
    print(type(c))
    print(type(d))
    return c, d


@app.cell
def _():
    first = "diego"
    last = "vila"
    first + last
    return first, last


@app.cell
def _(first):
    first * 6
    return


@app.cell
def _():
    s1 = '4'
    s2 = '4.7'
    n1 = 5 
    n2 = 5.8

    print(int(s1))
    #print(int(s2)) # causes a problem
    print(float(s1))
    print(float(s2))
    return n1, n2, s1, s2


@app.cell
def _():
    # list
    # numpy arrays
    return


@app.cell
def _():
    alist = [0,1,2,3,4,5]
    type(alist)
    return (alist,)


@app.cell
def _(alist):
    slist = [ '0','1','2','3','4','5']

    alist + slist
    return (slist,)


@app.cell
def _(mo):
    mo.md("""numpy is a way to make array in python""")
    return


@app.cell
def _(alist, np):
    alist_np = np.array(alist)
    print(type(alist))
    print(type(alist_np))

    return (alist_np,)


@app.cell
def _(alist_np):
    alist_np * 3

    return


@app.cell
def _(alist_np):
    alist_np + 3
    return


@app.cell
def _(alist):
    for idx, item in enumerate(alist):
        print(idx,item)
    return idx, item


@app.cell
def _(alist):
    alist[2:]
    return


@app.cell
def _(alist_np):
    alist_np[2:]
    return


if __name__ == "__main__":
    app.run()
