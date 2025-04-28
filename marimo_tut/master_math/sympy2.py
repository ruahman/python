import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import sympy as sym

    return (sym,)


if __name__ == "__main__":
    app.run()
