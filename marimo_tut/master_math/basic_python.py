import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    abs(-4)
    return


if __name__ == "__main__":
    app.run()
