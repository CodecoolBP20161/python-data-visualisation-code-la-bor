from connect_db import ConnectDatabase
from tagcloudgen import TagCloudGen
from companytagcloudgen import CompanyTagCloudGen
from company import Company
from project import Project


class Menu:

    @staticmethod
    def choose():
        option = input("Please enter a number: ")
        if option == "1":
            companies = Company.get_all()
            tagcloud = CompanyTagCloudGen(companies)
            tagcloud.display()
        elif option == "2":
            projects = Project.get_all()
            TagCloudGen.display(projects)
        elif option == "q":
            exit()
        # else:
        #     raise KeyError("There is no such option.")

    @staticmethod
    def handle_menu():
        print("Main menu\n", "1: Client tag-cloud\n", "2: Project tag-cloud\n", "Press Q to EXIT")

    @staticmethod
    def main():
        while True:
            Menu.handle_menu()
            try:
                Menu.choose()
            except KeyError as err:
                print("error message")


if __name__ == '__main__':
    Menu.main()
