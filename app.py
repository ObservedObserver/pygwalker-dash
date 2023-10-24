import dash
import dash_dangerously_set_inner_html

import dash_html_components as html
import pygwalker as pyg

from datasets import load_dataset
# load dataset
dataset = load_dataset("gradio/NYC-Airbnb-Open-Data", split="train")
df = dataset.to_pandas()

app = dash.Dash()

walker = pyg.walk(df, spec="./viz-code.json", debug=False)
html_code = walker.to_html()

app.layout = html.Div([
    dash_dangerously_set_inner_html.DangerouslySetInnerHTML(html_code),
])

if __name__ == '__main__':
    app.run_server(debug=True)
