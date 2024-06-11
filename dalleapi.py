import openai
import requests
import os

def gen(prompt):

    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    image_url = response['data'][0]['url']

    image_response = requests.get(image_url)

    if image_response.status_code == 200:
        return image_response.content
    else:
        raise Exception("Failed to download image")