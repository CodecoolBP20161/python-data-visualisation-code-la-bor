from connect_db import Connect_database


class Menu:
    def choose():
        option = input("Please enter a number: ")
        if option == "1":
            Connect_database.run_sql_file('clients_query.sql')
        elif option == "2":
            Connect_database.run_query(file_name)
        elif option == "q":
            exit()
        # else:
        #     raise KeyError("There is no such option.")

    def handle_menu():
        print("Main menu\n", "1: Client tag-cloud\n", "2: Project tag-cloud\n", "Press Q to EXIT")

    def main():
        while True:
            Menu.handle_menu()
            try:
                Menu.choose()
            except KeyError as err:
                print("error message")



if __name__ == '__main__':
    Menu.main()

# file_name = "SELECT company_name, COUNT(company_name), string_agg (main_color, ' ') FROM project GROUP BY company_name;"
