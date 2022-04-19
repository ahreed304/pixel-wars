import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

from sqlalchemy import create_engine
import psycopg2

import squarify


from flask import Flask, flash, redirect, render_template, request,   session, abort,send_from_directory,send_file,jsonify
import os


def connect_database():
    conn_string = 'postgresql+psycopg2://postgres:pass@127.0.0.1/reddit'
    db = create_engine(conn_string)

    conn = psycopg2.connect("dbname=reddit user=postgres password=Admin")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor

def execute_query_1(cursor):
    sql1='''select pixel_color, count(*) as color_count from pixel_placement where x < 10 and y < 10 group by pixel_color order by color_count desc;'''
    cursor.execute(sql1)
    colors_result = pd.DataFrame(cursor.fetchall())
    return colors_result

def create_plot(colors_result):
    # plot = plt.barh(colors_result[0], colors_result[1], color=colors_result[0], edgecolor="black")
    # plt.savefig('Colo
    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

app = Flask(__name__)

@app.route('/')
def hello_world():
    # cursor = connect_database()
    # plot_dataset_1 = execute_query_1(cursor)
    # plot1 = create_plot(plot_dataset_1)
    plot1 = create_plot('foo')

    # bar = create_plot()
    return render_template('index.html', plot=plot1)
    # return render_template("index.html")
    # # return('foo') 


app.run()