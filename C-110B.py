import plotly.figure_factory as ff
import statistics
import csv
import random
import pandas as pd
import plotly.graph_objects as go

df=pd.read_csv("newdata.csv")
data=df["average"].tolist()

def randomSetOfMean(counter):
    dataset=[]
    
    for i in range(0,counter):
        randomIndex=random.randint(0,len(data)-1)
        value=data[randomIndex]
        dataset.append(value)
    
    mean=statistics.mean(dataset)
    print(mean)
    return mean

def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1], mode="lines", name="mean"))
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,1000):
        setOfMeans=randomSetOfMean(100)
        meanlist.append(setOfMeans)
    
    showfig(meanlist)
    mean=statistics.mean(meanlist)

    std=statistics.stdev(meanlist)
    print("mean",mean)
    print(std)
    
setup()
