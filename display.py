from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class Display:

    @staticmethod
    def draw(tagcloud):
        from tagcloudgen import TagCloudGen
        img = Image.new("RGB", (700, 700), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        # font_size = int(tagcloud[0].font_size)
        # font = ImageFont.truetype("sans-serif.ttf", 20)
        text_content = tagcloud[0].label
        text_size = draw.textsize(text_content)
        text_options = {
            'fill': tagcloud[0].color
        }
        #     # draw.text((x, y),text_content,(r,g,b))
        draw.text((10, 200), text_content, **text_options)
        draw.text((0, text_size[1]), text_content, **text_options)
        draw.text((text_size[0], 0), text_content, **text_options)
        draw.text(text_size, text_content, **text_options)
        img.save('image.png')
