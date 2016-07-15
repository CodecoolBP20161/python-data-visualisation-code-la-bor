from tagcloudgen import TagCloudGen
from tagcloudgen import TagCloudItem


class HqTagCloudGen(TagCloudGen):

    def __init__(self, hqs):
        super().__init__()
        min_value = 100
        max_value = 0
        for hq in hqs:
            if hq.value > max_value:
                max_value = hq.value
            if hq.value < min_value:
                min_value = hq.value

        for hq in hqs:
            if hq.color:
                self.tag_cloud_items.append(TagCloudItem(hq.name, self.scaling(
                    hq, min_value, max_value), self.color_avg(
                    hq.color.split(" "))))

    @staticmethod
    def color_avg(colors):
        color_first_digit = 0
        color_second_digit = 0
        color_third_digit = 0
        for color in colors:
            color = color.lstrip('#')
            color_first_digit += int(color[0], 16)*17
            color_second_digit += int(color[1], 16)*17
            color_third_digit += int(color[2], 16)*17
            color_first_digit = round(color_first_digit/len(colors))
            color_second_digit = round(color_second_digit/len(colors))
            color_third_digit = round(color_third_digit/len(colors))
            rgbcolor = (color_first_digit, color_second_digit, color_third_digit)
        return rgbcolor

    @staticmethod
    def scaling(hq, min_value, max_value):
        scale = max_value - min_value
        def_font_size = 8
        if hq.value > 0.9 * scale:
            return def_font_size * 10
        elif 0.9 * scale >= hq.value > 0.8 * scale:
            return def_font_size * 9
        elif 0.8 * scale >= hq.value > 0.7 * scale:
            return def_font_size * 8
        elif 0.7 * scale >= hq.value > 0.6 * scale:
            return def_font_size * 7
        elif 0.6 * scale >= hq.value > 0.5 * scale:
            return def_font_size * 6
        elif 0.5 * scale >= hq.value > 0.4 * scale:
            return def_font_size * 5
        elif 0.4 * scale >= hq.value > 0.3 * scale:
            return def_font_size * 4
        elif 0.3 * scale >= hq.value > 0.2 * scale:
            return def_font_size * 3
        elif 0.2 * scale >= hq.value > 0.1 * scale:
            return def_font_size * 2
        elif 0.1 * scale >= hq.value >= 0:
            return def_font_size
        else:
            raise ValueError("It's kind of magic!")
