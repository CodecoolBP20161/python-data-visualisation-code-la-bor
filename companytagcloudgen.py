from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tagcloudgen import TagCloudGen
from company import Company

class CompanyTagCloudGen(TagCloudGen):
    def __init__(self):
        companies = Company.get_all()
        print(companies)
        # TagCloudGen.display(companies[0].name)
