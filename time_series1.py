import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline.offline import _plot_html
import plotly
import pandas as pd

# User API
plotly.tools.set_credentials_file(username='ArdyBeheshti', api_key='wbdYVRcns2Jt1SpATA8R')

# File path
df = pd.read_csv('D:/Personal/EDF/rawdata_example1.csv', low_memory=False)

# Plotting 
data1 = go.Scatter(x=df.Date, y=df.kW,
        name='kW Energy Output Site')

layout = go.Layout(title='kW at Site / 15 Minutes',
                   xaxis = dict(title = 'Date-time'),
                   yaxis = dict(title = 'kW'),
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)
fig = go.Figure(data=[data1], layout=layout)

# Stand alone HTML
plotly.offline.plot(fig, filename='data_set1.html')
py.iplot(fig)