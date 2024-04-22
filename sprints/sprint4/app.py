# %%
import pandas as pd
import numpy as np
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from datetime import datetime, timedelta
import math

# Load the dataset
data = pd.read_csv("dataset1.csv")

# Drop unnecessary columns
columns_to_drop = ['ObjectId', 'ISO2', 'ISO3', 'Indicator', 'Unit', 'Source', 'CTS_Code', 'CTS_Name', 'CTS_Full_Descriptor']
data_cleaned = data.drop(columns=columns_to_drop)

# Rename columns
data_cleaned.rename(columns={'Country': 'country'}, inplace=True)

# Convert the dataset from wide format to long format
data_tidy = pd.melt(data_cleaned, id_vars=['country'], var_name='year', value_name='temperature_change')

# Remove 'F' from year
data_tidy['year'] = data_tidy['year'].str.replace('F', '')

# Set a fixed end date for the countdown, 5 years from now
end_date = datetime.now() + timedelta(days=5*365+108,hours=12,minutes=3)

# Create the Dash app
app = Dash(__name__)

server = app.server

app.layout = html.Div([
    # Main content area with graph, text boxes, and controls
    html.Div([
        # Graph, its associated text box, and controls
        html.Div([
            # Controls (Dropdown and Slider) placed side by side
            html.Div([
                html.Div([
                    html.Label('Dropdown'),
                    dcc.Dropdown(
                        id='country-dropdown',
                        options=[{'label': i, 'value': i} for i in np.sort(data_tidy['country'].unique())],
                        value='United States',
                        multi=True
                    ),
                ], className='control-group control-group-right'),

                html.Div([
                    html.Label('Slider'),
                    dcc.RangeSlider(
                        id='year-range-slider',
                        min=int(data_tidy['year'].min()),
                        max=int(data_tidy['year'].max()),
                        step=1,
                        value=[int(data_tidy['year'].min()), int(data_tidy['year'].max())],
                        marks=None,
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                ], className='control-group control-group-left'),
            ], style={'width': '100%', 'margin-bottom': '20px'}),

            dcc.Graph(id='line-chart', style={'height': '400px'}),
        ], className='graph-area', style= {'background-color': '#9ab5d4ff','padding': '20px', 'border-radius': '15px'}),

        # Polar bear image, title, and its associated text box
        html.Div([
            html.Div([], style={'height': '20px'}),  # This empty div acts as a spacer
            html.H1('Temperature Change', style={'textAlign': 'left','font-family':'Arial'}),
            html.Div("Temperature changes are a natural part of Earth's climate system, influenced by various factors including solar radiation, atmospheric composition, and ocean currents. Over geological timescales, temperatures have fluctuated, leading to ice ages and warmer interglacial periods. In recent decades, however, human activities, particularly the burning of fossil fuels and deforestation, have accelerated temperature changes, leading to global warming. This warming is causing shifts in weather patterns, melting glaciers, rising sea levels, and impacting ecosystems. Understanding and mitigating the causes of these temperature changes is crucial for maintaining a stable climate and ensuring the well-being of all life on Earth.", style={'textAlign': 'left', 'padding-right': '10px' }),
        ], className='polar-bear-area'),
    ], className='content-area'),

    # Countdown timer
    html.Div([
        html.H1("Countdown Timer"),
        html.Div(id='countdown'),
        dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
    ], style={'padding': '20px', 'textAlign': 'center'}),

], style={'height': '100vh', 'padding': '10px'})


@app.callback(
    Output('line-chart', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('year-range-slider', 'value')]
)
def update_graph(selectedCountry, selectedYears):
    if not isinstance(selectedCountry, list) or not selectedCountry:
        # If selectedCountry is not a list (e.g., it's 'Select' or None) or it's empty, initialize it with 'United States'.
        selectedCountry = ['United States']

    # Convert years to strings because the DataFrame has years as strings.
    selectedYears = [str(y) for y in selectedYears]

    # Filter the data based on selected years.
    filtered_data = data_tidy[(data_tidy['year'] >= selectedYears[0]) & (data_tidy['year'] <= selectedYears[1])]

    # If there are countries selected, further filter the data.
    if selectedCountry:
        filtered_data = filtered_data[filtered_data['country'].isin(selectedCountry)]

    # Now, create the figure with the filtered data.
    fig = px.line(filtered_data, x='year', y='temperature_change', color='country',
                  title='Climate Change per Country and Year')

    fig.update_layout(
        xaxis_title='Years',
        yaxis_title='Temperature Change °C',
        legend_title='Countries',
        xaxis=dict(tickmode='linear', tick0=0, dtick=10, tickangle=-45),
        yaxis=dict(tickmode='auto', nticks=10),
    )
    return fig

@app.callback(
    Output('countdown', 'children'),
    Input('interval-component', 'n_intervals'))
def update_countdown(n):
    # Calculate the time difference between now and the end date
    time_left = end_date - datetime.now()

    # Extract days, hours, minutes, and seconds from the time difference
    days = time_left.days
    seconds = time_left.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    years = math.floor(days / 365)
    days = days - years * 365  # Subtract the number of days in the full year   


    # Format the countdown display
    return html.Div(
        f"{years} years, {days} days, {hours:02}:{minutes:02}:{seconds:02}",
        className='countdown'  
    )

if __name__ == '__main__':
    app.run(jupyter_mode='tab', debug=True) 


    
