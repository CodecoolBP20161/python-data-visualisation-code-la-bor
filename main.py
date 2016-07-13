from connect_db import ConnectDatabase
from tagcloudgen import TagCloudGen
from companytagcloudgen import CompanyTagCloudGen
from company import Company


class Menu:

    @staticmethod
    def choose(cls):
        option = input("Please enter a number: ")
        if option == "1":
            # tagcloud = CompanyTagCloudGen
            companies = Company.get_all()
            TagCloudGen.display(companies[0].name)
        elif option == "2":
            ConnectDatabase.run_query(file_name)
        elif option == "q":
            exit()
        # else:
        #     raise KeyError("There is no such option.")

    @staticmethod
    def handle_menu(cls):
        print("Main menu\n", "1: Client tag-cloud\n", "2: Project tag-cloud\n", "Press Q to EXIT")

    @staticmethod
    def main(cls):
        while True:
            Menu.handle_menu()
            try:
                Menu.choose()
            except KeyError as err:
                print("error message")


if __name__ == '__main__':
    Menu.main()
