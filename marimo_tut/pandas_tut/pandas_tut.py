import marimo

__generated_with = "0.11.8"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        data frames  is the main structuree of pandas
        basically it's tables with extra functionality
        allows us to work with spreadsheets and database tables
        """
    )
    return


@app.cell
def _(pd):
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"])
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df):
    df.index
    return


@app.cell
def _(df):
    df.index.tolist()
    return


@app.cell
def _(df):
    df.info()
    return


@app.cell
def _(df):
    df.describe()
    return


@app.cell
def _(df):
    df.shape
    return


@app.cell
def _(pd):
    coffee = pd.read_csv("./pandas_tut/coffee.csv")
    coffee
    return (coffee,)


@app.cell
def _(pd):
    results = pd.read_parquet("./pandas_tut/results.parquet")
    results
    return (results,)


@app.cell
def _(pd):
    bios = pd.read_csv('./pandas_tut/bios.csv')
    bios
    return (bios,)


@app.cell
def _(pd):
    olympics_data = pd.read_excel("./pandas_tut/olympics-data.xlsx")
    olympics_data
    return (olympics_data,)


@app.cell
def _(coffee):
    coffee.head(10)
    return


@app.cell
def _(coffee):
    coffee.tail(5)
    return


@app.cell
def _(coffee):
    coffee.sample(3)
    return


@app.cell
def _(coffee):
    coffee.loc[0:4]
    return


@app.cell
def _(coffee):
    coffee.loc[0:4,["Day","Coffee Type"]]
    return


@app.cell
def _(coffee):
    coffee.iloc[0:4,[0,1]]
    return


@app.cell
def _(coffee):
    coffee.at[0,"Units Sold"]
    return


@app.cell
def _(coffee):
    coffee.iat[0,2]
    return


@app.cell
def _(coffee):
    coffee.Day
    return


@app.cell
def _(coffee):
    coffee["Units Sold"]
    return


@app.cell
def _(coffee):
    coffee.sort_values(["Units Sold","Coffee Type"],ascending=[0,1])
    return


@app.cell
def _(coffee):
    for index, row in coffee.iterrows():
        print(index)
        print(row)
    return index, row


@app.cell
def _(bios):
    bios.tail(3)
    return


@app.cell
def _(bios):
    bios.loc[bios['height_cm'] > 215,["name","height_cm"]]
    return


@app.cell
def _(bios):
    bios[(bios['height_cm'] > 215) & (bios['born_country']=='USA')][["name","height_cm"]]
    return


@app.cell
def _(bios):
    bios[bios['name'].str.contains("Keith|patrick",case=False)]
    return


@app.cell
def _(bios):
    bios[bios['born_country'].isin(["FRA","USA"])]
    return


@app.cell
def _(bios):
    bios.query("born_country == 'FRA'")
    return


@app.cell
def _(coffee):
    import numpy as np
    coffee['new_price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99)
    coffee
    return (np,)


@app.cell
def _(coffee):
    coffee.drop(columns=['Day'])
    return


@app.cell
def _(bios):
    def categorize_athlete(row):
        if row['height_cm'] < 175 and row['weight_kg'] < 70:
            return 'Lightweight'
        elif row['height_cm'] < 185 or row['weight_kg'] <= 80:
            return 'Middleweight'
        else:
            return 'Heavyweight'

    bios['Category'] = bios.apply(categorize_athlete, axis=1)
    bios.head()
    return (categorize_athlete,)


@app.cell
def _(pd):
    nocs = pd.read_csv('./pandas_tut/noc_regions.csv')
    nocs.head()
    return (nocs,)


@app.cell
def _(bios, nocs, pd):
    bios_merged = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how='left')
    bios_merged.head()
    return (bios_merged,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
