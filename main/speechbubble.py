from PIL import Image

def add_alpha_channel(image):
    if image.mode == 'RGBA':
        return image
    else:
        return image.convert("RGBA")

def generate_speechbubble(image):
    image = add_alpha_channel(image)
    
    bubble_width = int(image.width)
    bubble_height = int(image.height * 0.2)

    bubble_image = Image.open('speechbubble.png').convert("RGBA")
    bubble_image = bubble_image.resize((bubble_width, bubble_height))

    new_image = Image.new('RGBA', (image.width, image.height))
    new_image.paste(image, (0, 0), mask=image)

    for x in range(bubble_image.width):
        for y in range(bubble_image.height):
            pixel = bubble_image.getpixel((x, y))
            if pixel[3] != 0:
                new_image.putpixel((x, y), (0, 0, 0, 0))

    return new_image

def add_speechbubble(image):
    image = add_alpha_channel(image)
    
    bubble_image = Image.open('speechbubble.png').convert('RGBA')
    original_bubble_width, original_bubble_height = bubble_image.size
    bubble_width = image.width
    bubble_height = int(original_bubble_height * (bubble_width / original_bubble_width))
    bubble_image = bubble_image.resize((bubble_width, bubble_height))

    new_image = Image.new('RGBA', (image.width, image.height + bubble_height), (0, 0, 0, 0))
    new_image.paste(image, (0, bubble_height))
    new_image.paste(bubble_image, (0, 0), mask=bubble_image)

    return new_image