import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline.offline import _plot_html
import plotly
import pandas as pd

# User API
plotly.tools.set_credentials_file(username='ArdyBeheshti', api_key='wbdYVRcns2Jt1SpATA8R')

df3 = pd.read_csv('D:/Personal/EDF/rawdata_example3.csv', low_memory=False)

data3 = [go.Scatter(
        x=df3.Date,
        y=df3.Mean_15)]

plotly.offline.plot(data3, filename='data_set3.html')
py.iplot(data3)