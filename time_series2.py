import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline.offline import _plot_html
import plotly
import pandas as pd

# User API
plotly.tools.set_credentials_file(username='ArdyBeheshti', api_key='wbdYVRcns2Jt1SpATA8R')

df2 = pd.read_csv('D:/Personal/EDF/rawdata_example2.csv', low_memory=False)

data2 = [go.Scatter(x=df2.Date_2017, y=df2.kW_15,
                    name='kW Energy Output Site 2')]

# Stand alone HTML
plotly.offline.plot(data2, filename='data_set2.html')
py.iplot(fig)
