import os
import io
import base64
import requests
from PIL import Image
from speechbubble import generate_speechbubble, add_speechbubble
from discord_upload import upload_to_discord
import pyperclip

WEBHOOK_URL = "https://discord.com/api/webhooks/1085957523766526042/mKcInGVV5qVtlRdwX-ju9vy21w7mZ2-8JMyp2L9CmxMWzPxD3JRvh_lykZRXXuKwajjs"

def is_url_image(url):
    try:
        response = requests.head(url)
        content_type = response.headers.get('content-type')
        return content_type and content_type.startswith('image')
    except:
        return False

def print_help():
    print("Prefix 1: Adds a transparent speech bubble on the image (recommended for Images)")
    print("Prefix 2: Adds a speech bubble above the image (recommended for discord convs)")

def main():
    while True:
        image = None

        if pyperclip.is_available() and pyperclip.paste().startswith("data:image"):
            image = Image.open(io.BytesIO(base64.b64decode(pyperclip.paste().split(',')[1])))
        else:
            file = ''
            if not file:
                print('Choose prefix (1 or 2), drop/drag image or enter image URL (type "help" for more info):')
                file = input().strip('\"')

            if file.lower() == "help":
                print_help()
                continue
            elif file.lower() == "exit" or file.lower() == "quit":
                break

            prefix, file = file[0], file[1:]
            if is_url_image(file):
                image = Image.open(io.BytesIO(requests.get(file).content))
            elif os.path.exists(file):
                image = Image.open(file)
            else:
                print('Error: The provided input is neither a valid file path nor a valid image URL')
                continue

        if prefix == '1':
            new_image = generate_speechbubble(image)
        elif prefix == '2':
            new_image = add_speechbubble(image)

        gif_file = 'edited.gif'
        new_image.save(gif_file)

        try:
            upload_to_discord(WEBHOOK_URL, gif_file)
            print(f"Your gif has been successfully uploaded to discord !")
        except requests.exceptions.HTTPError as e:
            print(f"Error uploading GIF to Discord: {e}")

if __name__ == '__main__':
    main()
