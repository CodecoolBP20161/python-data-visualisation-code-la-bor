from connect_db import ConnectDatabase


class Company:
    def __init__(self, name, project_count, project_colors):
        self.name = name
        self.project_count = project_count
        self.project_colors = project_colors

    @classmethod
    def get_all(cls):
        query = "SELECT company_name, COUNT(company_name), string_agg (main_color, ' ') AS color FROM project GROUP BY company_name;"
        rows = ConnectDatabase.run_query(query)
        companies = []
        for row in rows:
            companies.append(Company(row[0], row[1], row[2]))

        return companies


company_list = Company.get_all()
print(company_list[0].name)
