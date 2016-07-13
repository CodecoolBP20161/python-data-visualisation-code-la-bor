from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


class TagCloudItem:
    def __init__(self, label, font_size, color):
        self.label = label
        self.font_size = font_size
        self.color = color


class TagCloudGen:
    def __init__(self):
        self.tag_cloud_items = []


    # def display(self, content):
    #     self.img = Image.new("RGB", (512, 512), "red")
    #     self.draw = ImageDraw.Draw(img)
    #     self.content = 'text'
    #     self.text_options = {
    #         'fill': (255, 255, 255)
    #         }
    #     text_size = draw.textsize(content[0])
    #     # draw.text((x, y),text_content,(r,g,b))
    #     self.draw.text((40, 60), content, **text_options)
    #     self.img.save('image.png')
    #     print(content)

    def display(self):
        print(self.tag_cloud_items)
        print(self.tag_cloud_items[0].__dict__)
