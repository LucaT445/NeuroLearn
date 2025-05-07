import dash
from dash import dcc, html, Input, Output
from test_brain import build_brain_figure

# Get the figure and dictionary from your other file
fig, description_dict = build_brain_figure()

# Set up Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("NeuroLearn: Interactive Brain"),
    dcc.Graph(id='brain-graph', figure=fig),
    html.Div(id='description-box', style={
        'padding': '20px',
        'border': '1px solid #ccc',
        'margin-top': '20px',
        'backgroundColor': '#f9f9f9'
    })
])

@app.callback(
    Output('description-box', 'children'),
    Input('brain-graph', 'clickData')
)
def update_description(clickData):
    if clickData and clickData.get('points'):
        region_name = clickData['points'][0].get('hovertext')
        return description_dict.get(region_name, "No description available.")
    return "Click a brain region to learn more."

if __name__ == '__main__':
    app.run(debug=True)
