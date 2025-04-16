import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        # Layout

        `marimo` provides functions to help you lay out your output, such as
        in rows and columns, accordions, tabs, and callouts.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ## Rows and columns

        Arrange objects into rows and columns with `mo.hstack` and `mo.vstack`.
        """
    )
    return


@app.cell
def _(mo):
    mo.hstack(
        [mo.ui.text(label="hello"), mo.ui.slider(1, 10, label="slider")],
        justify="start",
    )
    return


@app.cell
def _(mo):
    mo.vstack([mo.ui.text(label="world"), mo.ui.number(1, 10, label="number")])
    return


@app.cell
def _(mo):
    grid = mo.vstack(
        [
            mo.hstack(
                [mo.ui.text(label="hello"), mo.ui.slider(1, 10, label="slider")],
            ),
            mo.hstack(
                [mo.ui.text(label="world"), mo.ui.number(1, 10, label="number")],
            ),
        ],
    ).center()

    mo.md(
        f"""
        Combine `mo.hstack` with `mo.vstack` to make grids:

        {grid}

        You can pass anything to `mo.hstack` to `mo.vstack` (including
        plots!).
        """
    )
    return (grid,)


@app.cell
def _(mo):
    justify = mo.ui.dropdown(
        ["start", "center", "end", "space-between", "space-around"],
        value="space-between",
        label="justify",
    )
    align = mo.ui.dropdown(
        ["start", "center", "end", "stretch"], value="center", label="align"
    )
    gap = mo.ui.number(start=0, step=0.25, stop=2, value=0.5, label="gap")
    wrap = mo.ui.checkbox(label="wrap")

    mo.hstack([justify, align, gap, wrap], justify="center")
    return align, gap, justify, wrap


@app.cell
def _(mo):
    size = mo.ui.slider(label="box size", start=60, stop=500)
    mo.hstack([size], justify="center")
    return (size,)


@app.cell
def _(mo, size):
    def create_box(num=1):
        box_size = size.value + num * 10
        return mo.Html(
            f"<div style='min-width: {box_size}px; min-height: {box_size}px; background-color: orange; text-align: center; line-height: {box_size}px'>{str(num)}</div>"
        )


    boxes = [create_box(i) for i in range(1, 5)]
    return boxes, create_box


@app.cell
def _(align, boxes, gap, justify, mo, wrap):
    mo.hstack(
        boxes,
        align=align.value,
        justify=justify.value,
        gap=gap.value,
        wrap=wrap.value,
    )
    return


@app.cell
def _(align, boxes, gap, mo):
    mo.vstack(
        boxes,
        align=align.value,
        gap=gap.value,
    )
    return


@app.cell
def _(mo):
    mo.md("This markdown is centered.").center()
    return


@app.cell
def _(mo):
    mo.md("This markdown is right-justified.").right()
    return


@app.cell
def _(mo):
    mo.accordion(
        {
            "Multiple items": "By default, only one item can be open at a time",
            "Allow multiple items to be open": (
                """
                Use the keyword argument `multiple=True` to allow multiple items
                to be open at the same time
                """
            ),
        }
    )
    return


@app.cell
def _(mo):
    _settings = mo.vstack(
        [
            mo.md("**Edit User**"),
            mo.ui.text(label="First Name"),
            mo.ui.text(label="Last Name"),
        ]
    )

    _organization = mo.vstack(
        [
            mo.md("**Edit Organization**"),
            mo.ui.text(label="Organization Name"),
            mo.ui.number(label="Number of employees", start=0, stop=1000),
        ]
    )

    mo.ui.tabs(
        {
            "🧙‍♀ User": _settings,
            "🏢 Organization": _organization,
        }
    )
    return


if __name__ == "__main__":
    app.run()
