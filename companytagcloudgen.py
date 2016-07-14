from tagcloudgen import TagCloudGen
from tagcloudgen import TagCloudItem


class CompanyTagCloudGen(TagCloudGen):

    def __init__(self, companies):
        super().__init__()
        for company in companies:
            if company.project_colors:
                self.tag_cloud_items.append(TagCloudItem(company.name, self.scaling(), self.color_avg(
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
        return [color_first_digit, color_second_digit, color_third_digit]

    @staticmethod
    def scaling():
        return 1
