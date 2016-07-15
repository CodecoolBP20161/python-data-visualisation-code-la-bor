from connect_db import ConnectDatabase
from tagcloudgen import TagCloudGen
from companytagcloudgen import CompanyTagCloudGen
from company import Company
from project import Project
from projectcloudgen import ProjectTagCloudGen


class Menu:

    @staticmethod
    def choose():
        option = input("Please enter the key of the option, that you want to choose: ")
        if option == "1":
            companies = Company.get_all()
            tagcloud = CompanyTagCloudGen(companies)
            tagcloud.display_company()
        elif option == "2":
            projects = Project.get_all()
            tagcloud = ProjectTagCloudGen(projects)
            tagcloud.display()
            # TagCloudGen.display(projects)
        elif option == "3":
            hqs = Hq.get_all()
            tagcloud = HqTagCloudGen(hqs)
            #tagcloud.display_hq()
        elif option == "q":
            exit()
        else:
            raise KeyError("There is no such option.")

    @staticmethod
    def handle_menu():
        print("\tMain menu\n", "\t\t1: Client tag-cloud\n", "\t\t2: Project tag-cloud\n", "\t\t3: HQ tag-cloud\n""\tPress Q to EXIT")

    @staticmethod
    def main():
        while True:
            Menu.handle_menu()
            try:
                Menu.choose()
            except KeyError as err:
                print("Please choose from these options:")


if __name__ == '__main__':
    Menu.main()
