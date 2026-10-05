
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, html, dcc, dash_table
from dash.dependencies import Input, Output


external_stylesheets = [
   {
       'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
       'rel': 'stylesheet',
       'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
       'crossorigin': 'anonymous'
   }
]

patients = pd.read_csv('IndividualDetails.csv')

app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server




# Simplified setup (since original GitHub paths may change):
# trimc = pd.read_csv('path_to_confirmed_global.csv')
# trimd = pd.read_csv('path_to_deaths_global.csv')
# trimr = pd.read_csv('path_to_recovered_global.csv')

# Example country-level data:
df_latest = trimc.groupby('Country').max().reset_index()


total_cases = df_latest['Confirmed'].sum()
total_deaths = df_latest['Deaths'].sum()
total_recovered = df_latest['Recovered'].sum() if 'Recovered' in df_latest.columns else 0
active_cases = total_cases - total_deaths - total_recovered


options = [{'label': 'World', 'value': 'All'}]
for c in sorted(df_latest['Country'].unique()):
    options.append({'label': c, 'value': c})


app.layout = html.Div([
    html.H1("🌍 COVID-19 Dashboard", className="text-center my-4 text-primary"),

    # Cards
    html.Div([
        html.Div([
            html.Div([
                html.H4("Total Cases", className="card-title text-light"),
                html.H2(f"{total_cases:,}", className="text-light")
            ], className="card bg-info p-3 rounded shadow")
        ], className="col-md-3"),

        html.Div([
            html.Div([
                html.H4("Active Cases", className="card-title text-light"),
                html.H2(f"{active_cases:,}", className="text-light")
            ], className="card bg-warning p-3 rounded shadow")
        ], className="col-md-3"),

        html.Div([
            html.Div([
                html.H4("Deaths", className="card-title text-light"),
                html.H2(f"{total_deaths:,}", className="text-light")
            ], className="card bg-danger p-3 rounded shadow")
        ], className="col-md-3"),

        html.Div([
            html.Div([
                html.H4("Recovered", className="card-title text-light"),
                html.H2(f"{total_recovered:,}", className="text-light")
            ], className="card bg-success p-3 rounded shadow")
        ], className="col-md-3"),
    ], className="row text-center mb-4"),

    html.Hr(),

    # Dropdown and Graph
    html.Div([
        html.Div([
            html.Label("Select Country:", className="font-weight-bold"),
            dcc.Dropdown(id='country_dropdown', options=options, value='All')
        ], className="col-md-4"),

        html.Div([
            dcc.Graph(id='country_graph')
        ], className="col-md-8")
    ], className="row mt-4"),

    html.Hr(),

    # Data Table
    html.Div([
        html.H3("Country-wise Summary", className="text-center mb-3 text-secondary"),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df_latest.columns],
            data=df_latest.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'center'},
            page_size=10
        )
    ])
], className="container-fluid")


@app.callback(
    Output('country_graph', 'figure'),
    [Input('country_dropdown', 'value')]
)
def update_country_graph(country):
    if country == 'All':
        df_plot = trimc.groupby('Date').sum().reset_index()
        title = "Global COVID-19 Cases Over Time"
    else:
        df_plot = trimc[trimc['Country'] == country]
        title = f"COVID-19 Cases in {country}"

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_plot['Date'], y=df_plot['Confirmed'], mode='lines+markers', name='Confirmed'))
    fig.add_trace(go.Scatter(x=df_plot['Date'], y=df_plot['Deaths'], mode='lines+markers', name='Deaths'))
    if 'Recovered' in df_plot.columns:
        fig.add_trace(go.Scatter(x=df_plot['Date'], y=df_plot['Recovered'], mode='lines+markers', name='Recovered'))

    fig.update_layout(title=title, xaxis_title="Date", yaxis_title="Number of Cases", template="plotly_dark")
    return fig


if __name__ == "__main__":
    app.run(debug=True)
