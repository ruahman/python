import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    for i in [1,2,3,4,5]:
        print(i)
    return (i,)


@app.cell
def _():
    list(range(0,3))

    return


@app.cell
def _():
    for query in range(0,3):
        print(query)
    return (query,)


if __name__ == "__main__":
    app.run()
