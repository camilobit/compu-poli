import os
from google import genai


client = genai.Client( api_key= "AIzaSyAXLwXnexNiWIsJwoIoM0wKGfMy1P_d_Mw" )

prompt = input("Ingrese su pregunta: ")


response = client.models.generate_content_stream(
    model="gemini-3.5-flash",
    contents= prompt
)

for chunk in response:
    print(chunk.text, end="", flush=True)