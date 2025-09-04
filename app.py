from dotenv import load_dotenv
load_dotenv()
import dash
from dash import dcc, html, Input, Output, callback, State, ctx
import json
import os
import openai
from openai import OpenAI
from test_brain import build_brain_figure

# gets figure and descriptions from test_brain.py
fig, description_dict = build_brain_figure()

region_data_json = json.dumps(description_dict) # converts the dictionary to JSON string

# system prompt that defines NeuroLearn's role, scope, and rules for answering questions
base_system_prompt = """\
You are NeuroLearn, an interactive assistant that helps users learn about the human brain using a 3D model.

You can answer:
- Questions about the eight regions from the 3D model (based on the JSON below)
- General questions about brain anatomy, function, disorders, neurotransmitters, brain chemistry, and related neuroscience concepts

If the user asks something clearly unrelated to the brain (e.g. about food, movies, sports, celebrities, or non-biological topics), respond with:

I'm sorry, I can't answer questions not related to NeuroLearn or the brain.

When relevant, you can supplement the JSON content with your own accurate neuroscientific knowledge.

Here is the JSON of all brain regions:
"""

# region colors for labels/UI (darker shade of yellow for better visibility)
region_color_dict = {
    "Frontal Lobe": "red",
    "Parietal Lobe": "#ebc310",
    "Temporal Lobe": "green",
    "Occipital Lobe": "blue",
    "Cerebellum": "purple",
    "Pituitary Gland": "brown",
    "Brainstem": "orange",
    "Corpus Callosum": "black"
}
default_color = "lightgrey"

app = dash.Dash(__name__)

server = app.server

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

app.layout = html.Div([

    html.Video(
        src="/assets/neuron_background.mp4",
        autoPlay=True,
        loop=True,
        muted=True, # required for autoplay to work
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
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap", # ensures fonts used below work
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
            config={ # hides the toolbar
                'displayModeBar': False
            }
        ),

        html.Div([
            html.Label('Ask NeuroLearn...', htmlFor='user-input-box', style={
                'marginRight': '10px',
                'fontFamily': 'Inter, sans-serif'
            }),
            html.Button('Submit', id='submit-button'),
            dcc.Input(
                id='user-input-box',
                type='text',
                placeholder="What is your question?",
                style={
                    'fontFamily': 'Inter, sans-serif',
                    'fontSize': '16px',
                    'padding': '8px',
                    'borderRadius': '8px'
                }
            ),
            html.Div(id='answer-box', style={
                'fontFamily': 'Inter, sans-serif',
                'fontSize': '16px',
                'lineHeight': '1.6',
                'padding': '20px',
                'border': '1px solid rgba(0,0,0,0.1)',
                'borderRadius': '10px',
                'margin': '20px auto',
                'maxWidth': '800px',
                'backgroundColor': 'rgba(255,255,255,0.8)',
                'color': '#333'
            })
        ], style={
            'padding': '20px',
            'maxWidth': '800px',
            'margin': '0 auto'
        }),

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
    Output('answer-box', 'children'),
    Input('brain-graph', 'clickData'),
    Input('submit-button', 'n_clicks'),
    State('user-input-box', 'value'), # prevents unnecessary calls
)
def update_description(clickData, n_clicks, user_question): # actual callback function
    button_trigger = ctx.triggered_id  # finds which input caused the callback

    if button_trigger == 'submit-button' and n_clicks and user_question:
        system_header = base_system_prompt + "\nHere is the JSON of all regions:\n" # rules to send to model
        final_system_prompt = { # builds prompt in dict format since that is what OpenAI requires
            "role": "system",
            "content": system_header + region_data_json
        }

        
        messages = [final_system_prompt, {"role": "user", "content": user_question}] # conversation transcript for how the AI answers questions
        try:
            completion = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = messages,
                max_tokens = 300,
                temperature = 0.7 # controls randomness of AI responses
            )
            answer = completion.choices[0].message.content.strip()
        except Exception as e:
            answer = f"Error: {e}"

        response_to_user = html.Div([
            html.P(f"You asked: {user_question}"),
            html.P(answer)
        ])
        return dash.no_update, response_to_user # leaves description-box unchanged and updates answer-box with AI response

            
            

    elif button_trigger == 'brain-graph' and clickData and clickData.get('points'): # run if a brain region was clicked (ensures clickData exists and contains point details)
        region_name = clickData['points'][0]['hovertext'] # gets the name of the region that was stored in hovertext when the trace was created
        region_data = description_dict.get(region_name) # look up the clicked region's details in the dictionary using region_name as the key

        if isinstance(region_data, dict):
            formatted_disorders = [html.Li([html.Strong(f"{item['name']}: "), item['description']]) 
            for item in region_data.get("disorders", [])]
            color = region_color_dict.get(region_name, default_color)
            title_style = {"marginBottom": "10px", "color": color}


            region_info = html.Div([
                html.H2(region_data["name"], style=title_style),
                html.P(f"Function: {region_data['function']}"),
                html.P(f"Location: {region_data['location']}"),
                html.P(f"Examples: {region_data['examples']}"),
                html.Div([html.P("Disorders:"), html.Ul(formatted_disorders)])])
            return region_info, dash.no_update # leaves answer-box untouched and updates description-box with region info

        return region_data or "No description available.", dash.no_update 

    else:
        return "Click a brain region to learn more.", dash.no_update


if __name__ == '__main__':
    port = int(os.getenv("PORT", 8050)) 
    app.run(host="0.0.0.0", port=port, debug=False)



