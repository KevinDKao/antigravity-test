import dash
from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Initialize App
app = dash.Dash(__name__)
app.title = "NEO-DASH"

# Dummy Data
np.random.seed(42)
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': np.random.randint(10, 100, 5),
    'Growth': np.random.randn(5)
})

# Neo-Brutalist Plot Styling
def style_fig(fig):
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Courier New', 'color': 'black', 'size': 14},
        title_font={'size': 24, 'family': 'Courier New', 'color': 'black'},
        margin=dict(l=40, r=40, t=60, b=40),
        xaxis=dict(
            showgrid=True, gridwidth=2, gridcolor='black',
            zeroline=True, zerolinewidth=3, zerolinecolor='black',
            linecolor='black', linewidth=3, mirror=True
        ),
        yaxis=dict(
            showgrid=True, gridwidth=2, gridcolor='black',
            zeroline=True, zerolinewidth=3, zerolinecolor='black',
            linecolor='black', linewidth=3, mirror=True
        )
    )
    fig.update_traces(
        marker_line_color='black', 
        marker_line_width=3
    )
    return fig

# Bar Chart
fig_bar = go.Figure(data=[
    go.Bar(x=df['Category'], y=df['Value'], marker_color='#4ecdc4')
])
fig_bar.update_layout(title="CATEGORY PERFORMANCE")
style_fig(fig_bar)

# Scatter Plot
fig_scatter = go.Figure(data=[
    go.Scatter(
        x=np.random.randn(20), 
        y=np.random.randn(20), 
        mode='markers',
        marker=dict(size=15, color='#ff6b6b', line=dict(width=3, color='black'))
    )
])
fig_scatter.update_layout(title="SCATTER CHAOS")
style_fig(fig_scatter)


app.layout = html.Div(className='container', children=[
    html.H1("NEO-BRUTALISM DASHBOARD", style={'textAlign': 'center'}),
    
    html.Div(className='grid-2', children=[
        html.Div(className='nb-card', children=[
            html.H3("METRIC 01"),
            html.P("VALUE: 420.69", style={'fontSize': '2em', 'fontWeight': 'bold'}),
            html.P("STATUS: OPTIMAL", style={'backgroundColor': '#00ff00', 'display': 'inline-block', 'padding': '5px', 'border': '2px solid black'})
        ]),
        html.Div(className='nb-card', children=[
            html.H3("METRIC 02"),
            html.P("VALUE: 1337", style={'fontSize': '2em', 'fontWeight': 'bold'}),
            html.P("STATUS: CRITICAL", style={'backgroundColor': '#ff0000', 'color': 'white', 'display': 'inline-block', 'padding': '5px', 'border': '2px solid black'})
        ])
    ]),

    html.Div(className='nb-card', children=[
        dcc.Graph(figure=fig_bar)
    ]),

    html.Div(className='nb-card', children=[
        dcc.Graph(figure=fig_scatter)
    ])
])

if __name__ == '__main__':
    app.run(debug=True)
