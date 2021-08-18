import plotly.graph_objs as go
import plotly.express as px


monthly_sales = \
    {'data': [{'type': '', 'x': ['Jan', 'Feb', 'March'], 'y': [450, 475, 400]}],
     'layout': {'title': {'text': ''}}}

# Update the type
monthly_sales['data'][0]['type'] = 'bar'

# Update the title text
monthly_sales['layout']['title']['text'] = 'Sales for Jan-Mar 2020'

# Create a figure
fig = go.Figure(monthly_sales)

# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)

# Print it out!
fig.show()