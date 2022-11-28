from PIL import Image, ImageDraw, ImageFont, ImageColor

from io import BytesIO
from os import remove

import urllib.request

# Open image and translated it in bytes
def open_image(url: str, text: str, color: str = "#23a9dd") -> str:
    urllib.request.urlretrieve(url, "temp-image.png")

    image_byte = BytesIO()
    
    image = Image.open("temp-image.png")
    image_draw = ImageDraw.Draw(image)
    image_font = ImageFont.truetype("cour.ttf", 72)

    fill_color = ImageColor.getcolor(color=color, mode="RGB")

    image_draw.text(xy=(20, 20), text=text, font=image_font, fill=(fill_color))

    image.save(image_byte, format='PNG')

    remove("temp-image.png")
    image.close

    return BytesIO(image_byte.getvalue())