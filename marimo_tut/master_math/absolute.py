import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    _x = abs(-5)
    mo.md(rf"""
    |x| = {_x}
    """)
    return


if __name__ == "__main__":
    app.run()
