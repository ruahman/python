import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    mo.md(
        r"""
        marimo supports several popular plotting libraries, including matplotlib,
        plotly, seaborn, and altair. 

        This tutorial gives examples using matplotlib; other libraries are
        used similarly.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        To show a plot, include it in the last expression of a cell (just
        like any other output).

        ```python3
        # create the plot in the last line of the cell
        import matplotlib.pyplot as plt
        plt.plot([1, 2])
        ```
        """
    )
    return


@app.cell
def _(plt):
    plt.plot([1, 2])
    # ... do some work ...
    # make plt.gca() the last line of the cell
    plt.gca()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        **A new figure every cell.** Every cell starts with an empty figure for 
        the imperative `pyplot` API.
        """
    )
    return


@app.cell
def _(np):
    x = np.linspace(start=-4, stop=4, num=100, dtype=float)
    return (x,)


@app.cell
def _(plt, x):
    plt.plot(x, x)
    plt.plot(x, x**2)
    plt.gca() # this will show on top
    #plt.show() # this will show in the bottom
    return


@app.cell
def _(plt, x):
    plt.plot(x, x**3)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        To build a figure over multiple cells, use the object-oriented API and
        create your own axis:
        """
    )
    return


@app.cell
def _(plt, x):
    _, axis = plt.subplots()
    axis.plot(x, x)
    axis.plot(x, x**2)
    axis
    return (axis,)


@app.cell
def _(axis, x):
    axis.plot(x, x**3)
    axis
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Draw plots interactively

        Draw plots interactively by parametrizing them with UI elements.
        """
    )
    return


@app.cell
def _(mo):
    exponent = mo.ui.slider(1, 5, value=1, step=1, label='exponent')

    mo.md(
        f"""
        **Visualizing powers.**

        {exponent}
        """
    )
    return (exponent,)


@app.cell
def _(mo, plt, x):
    @mo.cache
    def plot_power(exponent):
        plt.plot(x, x**exponent)
        return plt.gca()
    return (plot_power,)


@app.cell
def _(exponent, mo, plot_power):
    _tex = (
        f"$$f(x) = x^{exponent.value}$$" if exponent.value > 1 else "$$f(x) = x$$"
    )

    mo.md(
        f"""

        {_tex}

        {mo.as_html(plot_power(exponent.value))}
        """
    )
    return


if __name__ == "__main__":
    app.run()
