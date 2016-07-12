class Menu:
    def choose():
        inputs = input("Please enter a number: ")
        if option == "1":
            Connect_database.run_query(file_name)
        elif option == "2":
            Connect_database.run_query(file_name)

        elif option == "0":
            sys.exit(0)
        else:
            raise KeyError("There is no such option.")

    def handle_menu():
        print("Main menu \n", "1: Client tag-cloud", "\n 2: Project tag-cloud")

    def main():
        while True:
            Menu.handle_menu()
            try:
                Menu.choose()
            except KeyError as err:
                print("error message")


if __name__ == '__main__':
    Menu.main()
