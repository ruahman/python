import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        """
        # UI Elements

        One of marimo's most powerful features is its first-class
        support for interactive user interface (UI) elements: interacting
        with a UI element will automatically run cells that reference it.
        """
    )
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(start=1, stop=10, step=1)
    slider

    mo.md(
        f"""
        The `marimo.ui` module has a library of pre-built elements.

        For example, here's a `slider`: {slider}
        """
    )
    return (slider,)


@app.cell
def _(mo, slider):
    mo.md(f"and here's its value: **{slider.value}**.")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### How interactions run cells

        Whenever you interact with a UI element, its value is sent back to 
        Python. When this happens, all cells that reference the global variable 
        bound to the UI element, but don't define it, will run.

        This simple rule lets you use UI elements to
        drive the execution of your program, letting you build
        interactive notebooks and tools for yourselves and others.
        """
    )
    return


@app.cell
def _(mo):
    number = mo.ui.number(start=1, stop=10, step=1)
    number
    return (number,)


@app.cell
def _(number):
    number.value
    return


@app.cell
def _(mo):
    checkbox = mo.ui.checkbox(label="checkbox")
    checkbox
    return (checkbox,)


@app.cell
def _(checkbox):
    checkbox.value
    return


@app.cell
def _(mo):
    text = mo.ui.text(placeholder="type some text ...")
    text
    return (text,)


@app.cell
def _(text):
    text.value
    return


@app.cell
def _(mo):
    text_area = mo.ui.text_area(placeholder="type some text ...")
    text_area
    return (text_area,)


@app.cell
def _(text_area):
    text_area.value
    return


@app.cell
def _(mo):
    dropdown = mo.ui.dropdown(["a", "b", "c"])
    dropdown
    return (dropdown,)


@app.cell
def _(dropdown):
    dropdown.value
    return


@app.cell
def _(mo):
    run_button = mo.ui.run_button(label="click me")
    run_button
    return (run_button,)


@app.cell
def _(run_button):
    "Run button was clicked!" if run_button.value else "Click the run button!"
    return


@app.cell
def _(mo):
    array = mo.ui.array(
        [mo.ui.text(), mo.ui.slider(start=1, stop=10), mo.ui.date()]
    )
    array
    return (array,)


@app.cell
def _(array):
    array.value
    return


@app.cell
def _(mo):
    dictionary = mo.ui.dictionary(
        {
            "text": mo.ui.text(),
            "slider": mo.ui.slider(start=1, stop=10),
            "date": mo.ui.date(),
        }
    )
    dictionary
    return (dictionary,)


@app.cell
def _(dictionary):
    dictionary.value
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
