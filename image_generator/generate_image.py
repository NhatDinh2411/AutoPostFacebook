from openai import OpenAI
from base64 import b64decode
import json
import os
from typing import List

def generate_image(prompt: str, OPENAI_KEY:str, save_path:str):

    client = OpenAI(token=OPENAI_KEY)
    response_img = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="512x512",
        n=1,
        response_format="b64_json"
    )

    imgdata = b64decode(response_img.data[0].b64_json)
    with open(save_path, "wb") as f:
        f.write(imgdata)

    return imgdata