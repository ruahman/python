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

    plt.savefig('matplotlib_tut/mygraph.png')
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


@app.cell
def _(mo):
    mo.md(r"""## Real world examples""")
    return


@app.cell
def _(pd, plt):
    gas = pd.read_csv('matplotlib_tut/gas_prices.csv')
    plt.title('Gas Prices over Time')
    plt.plot(gas.Year, gas.USA, 'b.-', label="USA")
    plt.plot(gas.Year, gas.Canada, 'r.-', label="Canada")
    plt.plot(gas.Year, gas['South Korea'], 'g.-', label="South Koria")
    plt.plot(gas.Year, gas.Australia, 'y.-')
    plt.xticks(gas.Year[::3])
    plt.xlabel("Year")
    plt.ylabel("US Dolars")
    plt.legend()
    plt.savefig("matplotlib_tut/Gas_prices.png")
    plt.show()
    return (gas,)


@app.cell
def _(mo):
    mo.md(r"""### Load  fifa data""")
    return


@app.cell
def _(pd):

    fifa = pd.read_csv('matplotlib_tut/fifa_data.csv')
    fifa.head()
    return (fifa,)


@app.cell
def _(mo):
    mo.md(r"""### histagram""")
    return


@app.cell
def _(fifa, plt):
    bins = [40,50,60,70,80,90,100]
    plt.hist(fifa.Overall, bins=bins)
    plt.xticks(bins)
    plt.ylabel('Number of Player')
    plt.xlabel('Skill Level')
    plt.title('Players skills')
    plt.show()
    return (bins,)


@app.cell
def _(mo):
    mo.md(r"""## pie charts""")
    return


@app.cell
def _(fifa, plt):
    left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count().iloc[0]
    right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count().iloc[0]
    _labels = ['Left','Right']
    plt.pie([left,right], labels = _labels, autopct='%.2f%%')
    plt.show()
    return left, right


if __name__ == "__main__":
    app.run()
