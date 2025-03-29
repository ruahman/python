import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    print("hello world")
    print("where is this saved?")
    return


@app.cell
def _():
    print("next cell")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""mo.md("#his")""")
    return


@app.cell
def _(mo):

    mo.md("#test")
    return


if __name__ == "__main__":
    app.run()
