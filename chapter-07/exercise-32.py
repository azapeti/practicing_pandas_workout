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
    mo.md(rf"""
    ### Take the eight CSV files I’ve provided, containing weather data from eight different cities (spanning four states), and turn them into a data frame. The files are san+francisco,ca.csv, new+york,ny.csv, springfield,ma.csv, boston,ma.csv, springfield,il.csv, albany,ny.csv, los+angeles,ca.csv, and chicago,il.csv.

    ### We are only interested in the first three columns from each CSV file: the date and time, the max temperature, and the min temperature.
    """)
    return


@app.cell
def _():
    files_list = ['san+francisco,ca.csv', 'new+york,ny.csv', 'springfield,ma.csv', 'boston,ma.csv', 'springfield,il.csv', 'albany,ny.csv', 'los+angeles,ca.csv', 'chicago,il.csv']
    return (files_list,)


@app.cell
def _(files_list, pd):
    dfs = []

    for i in files_list:
        name = i.replace('.csv', '')
        city, state = name.split(',')
        city = city.replace('+', '_')

        _df = pd.read_csv(
            f'/home/peti/Documents/Pandas_workout/data/{i}',
            header=0,
            usecols=[0, 1, 2],
            names=['date_time', 'max_temp', 'min_temp']
        )

        _df['city'] = city
        _df['state'] = state

        dfs.append(_df)

    '''
    the "_" sign usually suggests:

    temporary/helper dataframe
    not meant to be used outside the current context
    intermediate step in a pipeline
    “internal use” variable

    It does not change how Python works — _df behaves exactly like df.

    In Marimo specifically, people often use _-prefixed variables to:

    avoid clutter in the notebook namespace
    mark intermediate variables
    signal “don’t rely on this cell output elsewhere”
    '''

    # NOTE: Reuven solution is muhn cooler then mine, check it because you can learn a lot from that.
    return (dfs,)


@app.cell
def _(dfs, pd):
    df = pd.concat(dfs)
    return (df,)


@app.cell
def _(df):
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ### Does the data for each city and state start and end at (roughly) the same time?
    ### How do you know?
    """)
    return


@app.cell
def _(dfs):
    for j in dfs:
        print(j['date_time'].head(1).to_string(header=False))

    for k in dfs:
        print(k['date_time'].tail(1).to_string(header=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is the lowest minimum temperature recorded for each city in the data set?
    """)
    return


@app.cell
def _(dfs):
    for p in dfs:
        print(
            p.loc[p['min_temp'] == p['min_temp'].min()][['city', 'min_temp']]
            .head(1)
        )

    # After i checked the solutions, I have no idea why i did this in this complicated way.
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is the highest maximum temperature recorded in each state in the data set?
    """)
    return


@app.cell
def _(df):
    df.groupby('state')['max_temp'].max()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Beyond the exercise_1
    ### Run `describe` on the minimum and maximum temperature for each state-city combination.
    """)
    return


@app.cell
def _(df):
    df.groupby(['state', 'city'])['min_temp'].describe()
    return


@app.cell
def _(df):
    df.groupby(['state', 'city'])['max_temp'].describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Beyond the exercise_2
    ### Running `describe` works, but we only see the first and last few rows from each result. Using `pd.set_option` to change the value of `display_max_rows` makes it possible to see all the results in Jupyter. Then reset the option to 10 rows.
    """)
    return


@app.cell
def _():
    # This is not relevant question in my solution
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Beyond the exercise_3

    ### What is the average difference in temperature (i.e., max – min) for each of the cities in our data set?
    """)
    return


@app.cell
def _(df):
    df.groupby('city')['max_temp'].mean() - df.groupby('city')['min_temp'].mean()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
