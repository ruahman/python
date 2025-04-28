import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    def myFunc(param):
        print(f"hello func {param}")
    return (myFunc,)


@app.cell
def _(myFunc):
    myFunc("foobar")
    return


if __name__ == "__main__":
    app.run()
