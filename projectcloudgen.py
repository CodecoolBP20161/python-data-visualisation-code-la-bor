from tagcloudgen import TagCloudGen
from tagcloudgen import TagCloudItem


class ProjectTagCloudGen(TagCloudGen):
    def __init__(self, projects):
        super().__init__()
        for project in projects:
            if project.value:
                self.tag_cloud_items.append(TagCloudItem(project.name, self.scaling(), project.color))

    @staticmethod
    def scaling():
        return 1
