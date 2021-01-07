from PIL import Image,ImageFont,ImageDraw
import random
import textwrap
import json
from wallpaper import set_wallpaper, get_wallpaper
with open("quotes.json") as file:
	quotes = json.load(file)
quote = random.choices(quotes)
text = quote[0]['text']
author = "by  "+quote[0]['author']
x=0
y=0
img_list = [{"image":"img3.jpg","font_size":64},{"image":"img4.jpg","font_size":64}]
random_wallpaper = random.choices(img_list)
random_wallpaper[0]
wallpaper = Image.open(random_wallpaper[0]["image"])
width, height = wallpaper.size
if len(text)>30:
    x = width/6 + 100
    y = height/2
    wrapper = textwrap.TextWrapper(width=30)

    text = wrapper.wrap(text=text)
    text ="\n".join(text)
else:
    x = width / 6 + 300
    y = height / 2
author_y = y+300
author_x = x+500

wallpaper_draw = ImageDraw.Draw(wallpaper)
wallpaper_font = ImageFont.truetype('LEVIBRUSH.TTF',random_wallpaper[0]["font_size"])
wallpaper_edited = wallpaper_draw.text((x,y), text, (237, 230, 211), font=wallpaper_font)
wallpaper_edited = wallpaper_draw.text((author_x,author_y), author, (237, 230, 211), font=wallpaper_font)
wallpaper.save("wallpaper.jpg")
set_wallpaper("wallpaper.jpg")
