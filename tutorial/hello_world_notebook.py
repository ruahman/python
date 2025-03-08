import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md("#hello world")
    return (mo,)


@app.cell
def _():
    print("hello console")
    return


if __name__ == "__main__":
    app.run()
