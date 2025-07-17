import marimo

__generated_with = "0.12.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    # one dimensional data structure
    s = pd.Series([10,20,30], index=["a","b","c"])
    print(s)
    return (s,)


@app.cell
def _(pd):
    # two dimensional data structure
    _data = {"name": ["Alice","Bob"], "Age": [25, 30]}
    _df = pd.DataFrame(_data)
    print(_df)
    return


@app.cell
def _(pd):
    # create data frame from csv
    df = pd.read_csv("pandas_tut/data.csv")
    df.to_csv("pandas_tut/backup-data.csv")
    print(df)



    return (df,)


@app.cell
def _(df):

    print(df.head())
    return


@app.cell
def _(df):
    print(df.tail(3))
    return


@app.cell
def _(df):
    print(df.info())
    return


@app.cell
def _(df):
    print(df.describe())
    return


@app.cell
def _(df):
    # get column
    print(df["name"])
    return


@app.cell
def _(df):
    # filter rows
    print(df[df["age"] > 25])
    return


@app.cell
def _(df):
    # get row
    print(df.iloc[0])
    return


@app.cell
def _(df):
    # get column
    print(df.iloc[:, 0])
    return


@app.cell
def _(df):
    # get column by lable
    print(df.loc[:, "age"])
    return


if __name__ == "__main__":
    app.run()
