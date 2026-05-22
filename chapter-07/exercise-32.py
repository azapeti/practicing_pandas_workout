import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from pandas import Series, DataFrame

    return mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    Take the eight CSV files I’ve provided, containing weather data from eight dif-
    ferent cities (spanning four states), and turn them into a data frame. The files
    are san+francisco,ca.csv, new+york,ny.csv, springfield,ma.csv, boston,ma.csv,
    springfield,il.csv, albany,ny.csv, los+angeles,ca.csv, and chicago,il.csv.

    We are only interested in the first three columns from each CSV file: the date
    and time, the max temperature, and the min temperature.
    """)
    return


@app.cell
def _():
    san_francisco_ca = "/home/peti/Documents/Pandas_workout/data/san+francisco,ca.csv"
    new_york_ny = "/home/peti/Documents/Pandas_workout/data/new+york,ny.csv"
    springfield_ma = "/home/peti/Documents/Pandas_workout/data/springfield,ma.csv"
    boston_ma = "/home/peti/Documents/Pandas_workout/data/boston,ma.csv"
    springfield_il = "/home/peti/Documents/Pandas_workout/data/springfield,il.csv"
    albany_ny = "/home/peti/Documents/Pandas_workout/data/albany,ny.csv"
    los_angeles_ca = "/home/peti/Documents/Pandas_workout/data/los+angeles,ca.csv"
    chicago_il = "/home/peti/Documents/Pandas_workout/data/chicago,il.csv"
    return (
        albany_ny,
        boston_ma,
        chicago_il,
        los_angeles_ca,
        new_york_ny,
        san_francisco_ca,
        springfield_il,
        springfield_ma,
    )


@app.cell
def _(
    albany_ny,
    boston_ma,
    chicago_il,
    los_angeles_ca,
    new_york_ny,
    pd,
    san_francisco_ca,
    springfield_il,
    springfield_ma,
):
    df_san_francisco_ca = pd.read_csv(
        san_francisco_ca,
        usecols=[0, 1, 2]
    )

    df_new_york_ny = pd.read_csv(
        new_york_ny,
        usecols=[0, 1, 2]
    )

    df_springfield_ma = pd.read_csv(
        springfield_ma,
        usecols=[0, 1, 2]
    )

    df_boston_ma = pd.read_csv(
        boston_ma,
        usecols=[0, 1, 2]
    )

    df_springfield_il = pd.read_csv(
        springfield_il,
        usecols=[0, 1, 2]
    )

    df_albany_ny = pd.read_csv(
        albany_ny,
        usecols=[0, 1, 2]
    )

    df_los_angeles_ca = pd.read_csv(
        los_angeles_ca,
        usecols=[0, 1, 2]
    )

    df_chicago_il = pd.read_csv(
        chicago_il,
        usecols=[0, 1, 2]
    )
    return


@app.cell
def _():
    ##############x rethink
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

        df = pd.read_csv(
            f'/home/peti/Documents/Pandas_workout/data/{i}',
            header=0,
            usecols=[0, 1, 2],
            names=['date_time', 'max_temp', 'min_temp']
        )

        df[city] = city
        df[state] = state

        dfs.append(df)
    return (dfs,)


@app.cell
def _(dfs):
    dfs
    return


if __name__ == "__main__":
    app.run()
