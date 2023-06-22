import csv
import plotly.figure_factory as ff
import pandas as pd
import random
import statistics

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=rando(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)

def rando(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    mean=statistics.mean(data_set)
    return mean

setup()