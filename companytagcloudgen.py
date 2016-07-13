from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tagcloudgen import TagCloudGen
from company import Company
from tagcloudgen import TagCloudItem


class CompanyTagCloudGen(TagCloudGen):
    def __init__(self, companies):
        # companies = Company.get_all()
        super().__init__()
        for company in companies:

            self.tag_cloud_items.append(TagCloudItem(company.name, 1, [0, 0, 0]))
