# from text_size import Size
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Text:

    def __init__(self, size, color, content, position, font):
        self.name = name
        self.size = size
        self.color = color
        self.content = content
        self.position = position
        self.font = font

    def position(self):


    def font(self):


    @staticmethod
    def create_image(cls, file_name):
        img = Image.new("RGB", (700, 700), (255, 255, 255))
        img.save('sample-out.png')
