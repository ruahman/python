import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    def _():
        print("local vars")
        is_active = True  # pylint: disable=invalid-name
        is_admin = False  # pylint: disable=invalid-name
        print(is_active,is_admin)

    _()
    return


if __name__ == "__main__":
    app.run()
