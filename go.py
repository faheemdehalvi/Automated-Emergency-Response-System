import gradio as gr
import pandas as pd
import requests
from tabulate import tabulate

# Function to invoke the API with location coordinates
def invoke_api(lat, lon):
    api_url = "http://127.0.0.1:8000/get_locations"
    if lat != "" and lon != "":
        api_url += f"?lat={lat}&lon={lon}"
    response = requests.get(api_url)
    json_data = response.json()
    df = pd.DataFrame(json_data)  # Convert JSON to DataFrame
    df.replace('\\N', '-----', inplace=True)  # Replace '\N' values with '-----'
    df_formatted = tabulate(df, headers='keys', tablefmt='psql')  # Format DataFrame with indentations
    return df_formatted

# Gradio Interface
input_latitude = gr.inputs.Textbox(lines=1, label='Latitude', placeholder="Enter latitude.")
input_longitude = gr.inputs.Textbox(lines=1, label='Longitude', placeholder="Enter longitude.")
submit_button = gr.inputs.Checkbox(label="Submit")
output_text = gr.outputs.Textbox()

gr.Interface(
    fn=invoke_api,
    inputs=[input_latitude, input_longitude],
    outputs=output_text,
    title="API Location Dashboard",
    description="Enter latitude and longitude separated by a comma to get the API response.",
).launch()