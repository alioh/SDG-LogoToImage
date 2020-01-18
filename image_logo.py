# reference: https://haptik.ai/tech/putting-text-on-image-using-python/

from PIL import Image, ImageDraw, ImageFont
import os

#   Load preferable font
font = ImageFont.truetype('Roboto-Bold.ttf', size=150)
#   Choose location of were to write
(x, y) = (1350, 1250)
#   Out put color
color = 'rgb(27, 41, 86)'

#   List of names
attendees = ['attendees 1', 'attendees 2']

#   Loop through names and write/save
for i in attendees:
    img = Image.open('certificate.png')
    draw = ImageDraw.Draw(img)
    draw.text((x, y), i, fill=color, font=font)
    img.save(f'{i}_done.png')