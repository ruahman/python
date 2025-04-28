import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""$10 \div 3 = 3 R1$""")
    return


@app.cell
def _():
    _a = 10
    _b = 3 

    print(_a/_b)
    print(int(_a/_b))
    print(int(_a%_b))
    return


if __name__ == "__main__":
    app.run()
