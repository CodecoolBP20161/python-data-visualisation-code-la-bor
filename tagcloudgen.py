from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from display import Display


class TagCloudItem:
    def __init__(self, label, font_size, color):
        self.label = label
        self.font_size = font_size
        self.color = color


class TagCloudGen:
    def __init__(self):
        self.tag_cloud_items = []


    def display(self):
        Display.draw(self.tag_cloud_items)
