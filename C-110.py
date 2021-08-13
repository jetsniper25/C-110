import plotly.figure_factory as ff
import statistics
import csv
import random
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()

populationMean=statistics.mean(data)
std=statistics.stdev(data)
print(std)
print(populationMean)

fig=ff.create_distplot([data],["average"],show_hist=False)
fig.add_trace(go.Scatter(x=[populationMean,populationMean],y=[0,1], mode="lines", name="mean"))
fig.show()