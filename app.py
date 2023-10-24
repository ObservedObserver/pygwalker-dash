import dash
# import dash_core_components as dcc
import dash_dangerously_set_inner_html

import dash_html_components as html
import pygwalker as pyg

from datasets import load_dataset

# load dataset
dataset = load_dataset("gradio/NYC-Airbnb-Open-Data", split="train")
df = dataset.to_pandas()

app = dash.Dash()

html_code = pyg.walk(df, return_html=True)

app.layout = html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(html_code),
])

if __name__ == '__main__':
    app.run_server(debug=True)
