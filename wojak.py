# wojak.py
# Uses PIL to add text to images

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def addText(text, path):
  source = Image.open(path)
  draw = ImageDraw.Draw(source)

  # Reduce the font size based on the message length
  fontSize = 32
  texts = []
  if(len(text) < 10):
    fontSize = 42
  if(len(text) > 25):
    fontSize = 28
  if(len(text) > 30):
    # Split the text onto two lines
    font = ImageFont.truetype("assets/arial.ttf", fontSize)
    draw.text((25, 50), text[:30], (0, 0, 0), font=font)
    draw.text((25, 85), text[30:], (0, 0, 0), font=font)
    return source

  font = ImageFont.truetype("assets/arial.ttf", fontSize)
  draw.text((25, 50), text, (0,0,0), font=font)
  return source