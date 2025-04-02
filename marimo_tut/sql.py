import marimo

__generated_with = "0.11.8"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import string
    import matplotlib as plt
    return mo, plt, string


@app.cell
def _():
    has_duckdb_installed = False
    try:
        import duckdb

        has_duckdb_installed = True
    except ImportError:
        pass

    has_polars_installed = False
    try:
        import polars

        has_polars_installed = True
    except ImportError:
        pass

    has_pandas_installed = False
    try:
        import pandas

        has_pandas_installed = True
    except ImportError:
        pass
    return (
        duckdb,
        has_duckdb_installed,
        has_pandas_installed,
        has_polars_installed,
        pandas,
        polars,
    )


@app.cell
def _(has_duckdb_installed, mo):
    if has_duckdb_installed:
        mo.output.replace(
            mo.md(
                """
        !!! Tip "Installed"
            If you see this, DuckDB is already installed.
        """
            )
        )
    else:
        mo.output.replace(
            mo.md(
                """
        !!! Warning "Not Installed"
            If you see this, DuckDB is not installed.
        """
            )
        )
    return


@app.cell
def _(mo):
    mo.md(r"""Let's take a look at a SQL cell. The next cell generates a dataframe called `df`.""")
    return


@app.cell
def _(has_polars_installed):
    _SIZE = 1000


    def _create_token_data(n_items=100):
        import random
        import string

        def generate_random_string(length):
            letters = string.ascii_lowercase
            result_str = "".join(random.choice(letters) for i in range(length))
            return result_str

        def generate_random_numbers(mean, std_dev, num_samples):
            return [int(random.gauss(mean, std_dev)) for _ in range(num_samples)]

        random_numbers = generate_random_numbers(50, 15, n_items)
        random_strings = sorted(
            list(set([generate_random_string(3) for _ in range(n_items)]))
        )

        return {
            "token": random_strings,
            "count": random_numbers[: len(random_strings)],
        }


    _data = _create_token_data(_SIZE)

    # Try polars
    if has_polars_installed:
        import polars as pl

        df = pl.DataFrame(_data)
    # Fallback to pandas (maybe trying to install it)
    else:
        import pandas as pd

        df = pd.DataFrame(_data)
    return df, pd, pl


@app.cell
def _(mo):
    mo.md(r"""Next, we create a SQL query, refercing the Python dataframe `df` directly.""")
    return


@app.cell
def _(df, mo):
    _df = mo.sql(
        f"""
        -- This SQL cell is special since we can reference existing dataframes in the global scope as a table in the SQL query. For example, we can reference the `df` dataframe in the global scope, which was defined in another cell using Python.

        SELECT * FROM df;

        -- By default, the output variable starts with an underscore (`_df`), making it private to this cell. To access the query result in another cell, change the name of the output variable.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""You can create SQL statements that depend on Python values, such as UI elements:""")
    return


@app.cell
def _(mo, string):
    token_prefix = mo.ui.dropdown(
        list(string.ascii_lowercase), label="token prefix", value="a"
    )
    token_prefix
    return (token_prefix,)


@app.cell
def _(df, mo, token_prefix):
    result = mo.sql(
        f"""
        -- Change the dropdown to see the SQL query filter itself!
        --
        -- Here we use a duckdb function called `starts_with`:
        SELECT * FROM df WHERE starts_with(token, '{token_prefix.value}')

        -- Notice that we named the output variable `result`
        """
    )
    return (result,)


@app.cell
def _(mo):
    mo.md(
        r"""
        Since we named the output variable above **`result`**,
        we can use it back in Python.
        """
    )
    return


@app.cell
def _(result):
    result
    return


@app.cell
def _(mo):
    mo.md(r"""### download files online""")
    return


@app.cell
def _(cars, mo):
    _df = mo.sql(
        f"""
        CREATE OR replace TABLE cars as
        FROM 'https://datasets.marimo.app/cars.csv';

        -- Query the table
        SELECT * from cars;
        """
    )
    return (cars,)


if __name__ == "__main__":
    app.run()
