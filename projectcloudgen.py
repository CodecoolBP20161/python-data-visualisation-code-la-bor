from tagcloudgen import TagCloudGen
from tagcloudgen import TagCloudItem


class ProjectTagCloudGen(TagCloudGen):
    def __init__(self, projects):
        super().__init__()
        min_value = 1000000000000000000
        max_value = 0
        for project in projects:
            if project.value > max_value:
                max_value = project.value
            elif project.value < min_value:
                min_value = project.value
        for project in projects:
            if project.value:
                self.tag_cloud_items.append(TagCloudItem(project.name, self.scaling(
                    project, min_value, max_value), self.color_translator(str(project.color))))

    @staticmethod
    def scaling(project, min_value, max_value):
        scale = max_value - min_value
        def_font_size = 4
        if project.value > 0.8*scale:
            return def_font_size * 5
        elif 0.8*scale > project.value > 0.6*scale:
            return def_font_size * 4
        elif 0.6*scale > project.value > 0.4*scale:
            return def_font_size * 3
        elif 0.4*scale > project.value > 0.2*scale:
            return def_font_size * 2
        elif 0.2*scale > project.value > 0:
            return def_font_size
        else:
            raise ValueError("Hülye vagy")

    @staticmethod
    def color_translator(color):
        color_first_digit = 0
        color_second_digit = 0
        color_third_digit = 0
        color = color.lstrip('#')
        color_first_digit += int(color[0], 16)*17
        color_second_digit += int(color[1], 16)*17
        color_third_digit += int(color[2], 16)*17
        return [color_first_digit, color_second_digit, color_third_digit]
