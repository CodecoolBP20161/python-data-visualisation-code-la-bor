from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random


class Display:

    @staticmethod
    def draw(tagcloud):
        from tagcloudgen import TagCloudGen
        img = Image.new("RGB", (700, 700), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        #     # draw.text((x, y),text_content,(r,g,b))
        z = len(tagcloud) - 100

        for i in range(10, z, 30):
            x += random.randint(-10, 10)
            y += random.randint(-10, 10)

            text_content = tagcloud[i].label
            font_size = int(tagcloud[i].font_size)
            text_size = draw.textsize(text_content)
            font = ImageFont.truetype("Roboto-Condensed.ttf", font_size)
            text_options = {
            'fill': tagcloud[i].color
            }
            draw.text((x, y), text_content, **text_options, font=font)

        img.save('image.png')

    def _check_overlap(self, x, y, font_size, h, w, tagcloud):
        h = tagcloud[i].font_size
        if not tagcloud[i].label:
            tagcloud[i].label = []
            return False

            for word in tagcloud[i].label:
                if not ((x + w < word['x']) or (word['x'] + word['w'] < x) or (y + h < word['y']) or (word['y'] + word['h'] < y)):
                    return True

                    return False
