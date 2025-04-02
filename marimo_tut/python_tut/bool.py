import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    print(10 > 9)
    print(10 == 9)
    print(10 < 9)
    return


if __name__ == "__main__":
    app.run()
