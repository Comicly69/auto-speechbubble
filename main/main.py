import os
import io
import base64
import requests
from PIL import Image
from speechbubble import *
from discord_upload import upload_to_discord
import pyperclip

WEBHOOK_URL = "https://discord.com/api/webhooks/yourwebhookurl"

def is_url_image(url):
    try:
        response = requests.head(url)
        content_type = response.headers.get('content-type')
        return content_type and content_type.startswith('image')
    except:
        return False

def print_help():
    print("Prefix 1: Adds a transparent speech bubble on the image (recommended for Images)")
    print("Prefix 2: Adds a speech bubble above the image (recommended for retards talking)")

def main():
    image = None

    if pyperclip.is_available() and pyperclip.paste().startswith("data:image"):
        image = Image.open(io.BytesIO(base64.b64decode(pyperclip.paste().split(',')[1])))
    else:
        file = ''
        if not file:
            print('Enter a prefix (1 or 2), drag and drop or enter image path/URL ("help" for more info)')
            file = input().strip('\"')
        
        if file.lower() == "help":
            print_help()
            return

        prefix, file = file[0], file[1:]
        if is_url_image(file):
            image = Image.open(io.BytesIO(requests.get(file).content))
        elif os.path.exists(file):
            image = Image.open(file)
        else:
            print('Retard, you provided a wrong input, go kys nigger')
            return

        width, height = image.size
        ratio = width / height
        height = image.height

        if prefix == '1':
            new_image = generate_speechbubble(image)
        elif prefix == '2':
            if ratio >= 500/300 or height >= 500:
                new_image = add_speechbubble(image)
            else:
                new_image = add_speechbubble_big_image(image)

        gif_file = 'edited.gif'
        new_image.save(gif_file)

    try:
        upload_to_discord(WEBHOOK_URL, gif_file)
        print("Your retard has been successfully speech-bubbled and uploaded to discord")
    except requests.exceptions.HTTPError as e:
        print(f"The gif failed to upload : {e}")


if __name__ == '__main__':
    main()
