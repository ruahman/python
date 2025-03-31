import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""### hello world""")
    return


@app.cell
def _():
    print("Hello, World!")
    return


@app.cell
def _(mo):
    mo.md("""### system info""")
    return


@app.cell
def _():
    import sys

    print(sys.version)
    return (sys,)


@app.cell
def _(mo):
    mo.md("""### python indentation""")
    return


@app.cell
def _():
    if 5 > 2:
        print("Five is greater than two!")
    return


@app.cell
def _(mo):
    mo.md(r"""### variables""")
    return


@app.cell
def _():
    x = 5
    y = "Hello, World!"
    print(x,y)
    return x, y


@app.cell
def _(mo):
    mo.md(r"""### comments""")
    return


@app.cell
def _():
    #This is a comment.
    print("Hello, World!")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
