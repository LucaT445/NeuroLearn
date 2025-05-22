import dash
from dash import dcc, html, Input, Output
from test_brain import build_brain_figure

# Gets figure and descriptions from test_brain.py
fig, description_dict = build_brain_figure()

app = dash.Dash(__name__)

app.layout = html.Div([

    html.Video(
        src="/assets/neuron_background.mp4",
        autoPlay=True,
        loop=True,
        muted=True,
        style={
            'position': 'fixed',
            'top': '0',
            'left': '0',
            'width': '100%',
            'height': '100%',
            'objectFit': 'cover',
            'zIndex': '-1',
            'opacity': '0.15'
        }
    ),

    html.Link(
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap",
        rel="stylesheet"
    ),

    html.Div([

        html.H1("NeuroLearn: Interactive Brain", style={
            'fontFamily': 'Inter, sans-serif',
            'fontWeight': '800',
            'fontSize': '36px',
            'textAlign': 'center',
            'marginTop': '20px',
            'color': '#222'
        }),

        html.P("Click a brain region to learn more", style={
            'fontFamily': 'Inter, sans-serif',
            'fontSize': '18px',
            'textAlign': 'center',
            'marginBottom': '40px',
            'color': '#555'
        }),

        dcc.Graph(
            id='brain-graph',
            figure=fig,
            style={
                'height': '600px',
                'backgroundColor': 'rgba(255,255,255,0)'  
            },
            config={
                'displayModeBar': False
            }
        ),

        html.Div(id='description-box', style={
            'fontFamily': 'Inter, sans-serif',
            'fontSize': '16px',
            'lineHeight': '1.6',
            'padding': '20px',
            'border': '1px solid rgba(0,0,0,0.1)',
            'borderRadius': '10px',
            'margin': '40px auto',
            'maxWidth': '800px',
            'backgroundColor': 'rgba(255,255,255,0.8)',  
            'color': '#333'
        })

    ], style={
        'padding': '20px',
        'maxWidth': '1000px',
        'margin': '0 auto',
        'position': 'relative',
        'zIndex': '10',
        'backgroundColor': 'rgba(255,255,255,0.2)',  
        'borderRadius': '12px',
        'boxShadow': '0 4px 12px rgba(0, 0, 0, 0.15)'
    })

])

@app.callback(
    Output('description-box', 'children'),
    Input('brain-graph', 'clickData')
)
def update_description(clickData):
    if clickData and clickData.get('points'):
        region_name = clickData['points'][0]['hovertext']
        return description_dict.get(region_name, "No description available.")
    return "Click a brain region to learn more."

if __name__ == '__main__':
    app.run(debug=True)

