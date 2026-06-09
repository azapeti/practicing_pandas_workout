import marimo

__generated_with = "0.23.8"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from pandas import Series, DataFrame

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Read in the scores file (sat-scores.csv). This time, you want the following columns: Year, State.Code, Total.Math, Family Income.Less than 20k.Math, Family Income.Between 20-40k.Math, Family Income.Between 40-60k.Math, Family Income.Between 60-80k.Math, Family Income.Between 80-100k.Math, and Family Income.More than 100k.Math.

    ## Rename the income-related column names to something shorter. I recommend income<20k, 20k<income<40k, 40k<income<60k, 60k<income<80k, 80k<income 100k, and income>100k.
    """)
    return


@app.cell
def _(pd):
    _df = pd.read_csv(
        '/home/peti/Documents/Pandas_workout/data/sat-scores.csv',
        usecols=[
        "Year",
        "State.Code",
        "Total.Math",
        "Family Income.Less than 20k.Math",
        "Family Income.Between 20-40k.Math",
        "Family Income.Between 40-60k.Math",
        "Family Income.Between 60-80k.Math",
        "Family Income.Between 80-100k.Math",
        "Family Income.More than 100k.Math"
        ]
    )

    # Rename the columns
    df = _df.rename(columns={
        "Year": "Year",
        "State.Code": "State_Code",
        "Total.Math": "Total_Math",
        "Family Income.Less than 20k.Math": "income<20k",
        "Family Income.Between 20-40k.Math": "20k<income<40k",
        "Family Income.Between 40-60k.Math": "40k<income<60k",
        "Family Income.Between 60-80k.Math": "60k<income<80k",
        "Family Income.Between 80-100k.Math": "80k<income<100k",
        "Family Income.More than 100k.Math": "income>100k"
    })
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Find the average SAT math score for each income level, grouped and then sorted by year.
    """)
    return


@app.cell
def _(df):
    mean_sat_by_year = df.groupby('Year')[df.filter(like='income').columns].mean().round(2).reset_index()
    return (mean_sat_by_year,)


@app.cell
def _(mean_sat_by_year):
    mean_sat_by_year
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## For each year in the data set, determine how much better each income group did, on average, than the next-poorer group of students. Do you see (just by looking at the data) any income group that did worse, in any year, than the next-poorer students?
    """)
    return


@app.cell
def _(df):
    desired_col_order = [
        "income<20k",
        "20k<income<40k",
        "40k<income<60k",
        "60k<income<80k",
        "80k<income<100k",
        "income>100k"
    ]

    percentage_change_df = df.groupby('Year')[desired_col_order].mean().transpose().pct_change().round(3)

    percentage_change_df

    # Do you see (just by looking at the data) any income group that did worse, in any year, than the next-poorer students?
    # My answer is NO.
    return (percentage_change_df,)


@app.cell
def _(mo, percentage_change_df):
    # Renders the classic, static Pandas HTML table with the index intact
    mo.Html(percentage_change_df.to_html())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Which income bracket, on average, had the greatest advantage over the next-poorer income bracket?
    """)
    return


@app.cell
def _(percentage_change_df):
    rows = list(percentage_change_df.index)
    # rows2 = percentage_change_df.index.to_list() <- both gives the same list

    rows
    return (rows,)


@app.cell
def _(percentage_change_df, rows):
    for i in rows:
        print(f' {i:<18}| {round(percentage_change_df.loc[i].mean(), 3):>10}')

    # 20k<income<40k had the greatest advantage over next-poorer income bracket
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Can we find, in a calculated and automated way, which income levels consistently (i.e., across all years) do worse than the next-poorest group?
    """)
    return


@app.cell
def _(percentage_change_df):
    percentage_change_df[percentage_change_df < 0]

    # there was never a single occasion like this
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
