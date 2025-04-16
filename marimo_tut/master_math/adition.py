import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    4 + 8
    return


@app.cell
def _():
    4 + 1 + 5
    return


@app.cell
def _():
    5 - 3
    return


@app.cell
def _():
    3 * 3
    return


@app.cell
def _():
    3 * 3 + 1 - 5
    return


@app.cell
def _():
    (1 + 3 )/ 4
    return


@app.cell
def _():
    5 - (2/4) * (3/5)
    return


@app.cell
def _():
    (4-5) / (3+5*6)
    return


if __name__ == "__main__":
    app.run()
