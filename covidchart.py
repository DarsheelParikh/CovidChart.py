import pandas as pd 
import plotly.express as px
df = pd.read_csv("covidchart.csv")
fig= px.line(df,x="country",y="cases", title="Country Covid Cases")
fig.show()