import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    return np, pd, plt


@app.cell
def _(mo):
    mo.md(r"""## Basic Graph""")
    return


@app.cell
def _(np, plt):
    x = [0,1,2,3,4]
    y = [0,2,4,6,8]
    plt.plot(x,y, label='2x', color='red', linewidth=4, marker=".", markersize=20, linestyle="--")

    x2 = np.arange(0,4.5,0.5)
    plt.plot(x2, x2 ** 2, 'r', label="x^2")

    plt.title("Our first graph")
    plt.xlabel("x axis")
    plt.ylabel("y axis") 
    plt.xticks([0,1,2,3])
    plt.yticks([0,2,4,6])
    plt.legend()

    plt.savefig('mygraph.png')
    plt.show()
    return x, x2, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## bar charts""")
    return


@app.cell
def _(plt):
    values = ['A','B','C']
    labels = [1,4,2]
    bars = plt.bar(values, labels)
    bars[0].set_hatch('/')
    bars[1].set_hatch('o')
    bars[2].set_hatch('*')

    plt.show()
    return bars, labels, values


if __name__ == "__main__":
    app.run()
