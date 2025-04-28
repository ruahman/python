import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from IPython.display import display,Math
    return Math, display, mo


@app.cell
def _(mo):
    mo.md(rf"""
    $\sigma = \mu \times \sqrt{{5}}$
    """)
    return


@app.cell
def _(Math, display):
    display(Math("\\sigma"))
    display(Math("\\sigma"))
    display(Math("\\sigma"))
    return


@app.cell
def _(mo):
    mo.md(r"""$x_{mm} + y^{n + 2k -15}$""")
    return


@app.cell
def _(mo):
    mo.md(r"""$\sqrt{x}\sqrt{x}$""")
    return


@app.cell
def _(mo):
    mo.md(r"""$\frac{1 + x}{2v -s^{t + 4r}}$""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        $$
        \frac{2}{3}
        $$
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""$2x + 5y = 8x = 71$""")
    return


@app.cell
def _(mo):
    mo.md(r"""$\sin(2\pi ft + 0)$""")
    return


@app.cell
def _(mo):
    mo.md(r"""$e = mc^2$""")
    return


@app.cell
def _(mo):
    mo.md(r"""$\frac{4 + 5x^2}{(1 + x)(1 - x)}$""")
    return


if __name__ == "__main__":
    app.run()
