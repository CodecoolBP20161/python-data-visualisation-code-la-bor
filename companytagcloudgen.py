from tagcloudgen import TagCloudGen
from tagcloudgen import TagCloudItem


class CompanyTagCloudGen(TagCloudGen):

    def __init__(self, companies):
        super().__init__()
        min_count = 100
        max_count = 0
        for company in companies:
            if company.project_count > max_count:
                max_count = company.project_count
            if company.project_count < min_count:
                min_count = company.project_count

        for company in companies:
            if company.project_colors:
                self.tag_cloud_items.append(TagCloudItem(company.name, self.scaling(
                    company, min_count, max_count), self.color_avg(
                    company.project_colors.split(" "))))

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
    def scaling(company, min_count, max_count):
        scale = max_count - min_count
        def_font_size = 3
        if company.project_count > 0.9 * scale:
            return def_font_size * 10
        elif 0.9 * scale >= company.project_count > 0.8 * scale:
            return def_font_size * 9
        elif 0.8 * scale >= company.project_count > 0.7 * scale:
            return def_font_size * 8
        elif 0.7 * scale >= company.project_count > 0.6 * scale:
            return def_font_size * 7
        elif 0.6 * scale >= company.project_count > 0.5 * scale:
            return def_font_size * 6
        elif 0.5 * scale >= company.project_count > 0.4 * scale:
            return def_font_size * 5
        elif 0.4 * scale >= company.project_count > 0.3 * scale:
            return def_font_size * 4
        elif 0.3 * scale >= company.project_count > 0.2 * scale:
            return def_font_size * 3
        elif 0.2 * scale >= company.project_count > 0.1 * scale:
            return def_font_size * 2
        elif 0.1 * scale >= company.project_count >= 0:
            return def_font_size
        else:
            raise ValueError("It's kind of magic!")
