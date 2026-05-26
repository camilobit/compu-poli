import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key="AIzaSyAXLwXnexNiWIsJwoIoM0wKGfMy1P_d_Mw",
    )

    model = "gemini-3.5-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    tools = [
        types.Tool(googleSearch=types.GoogleSearch(
        )),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        media_resolution="MEDIA_RESOLUTION_HIGH",
        tools=tools,
        response_mime_type="application/json",
        response_schema=genai.types.Schema(
            type = genai.types.Type.OBJECT,
            properties = {
                "response": genai.types.Schema(
                    type = genai.types.Type.STRING,
                ),
            },
        ),
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")

if __name__ == "__ai_studio__":
    generate()


