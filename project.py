from connect_db import ConnectDatabase


class Project:
    def __init__(self, project_name, value, color):
        self.project_name = project_name
        self.value = value
        self.color = color

    @classmethod
    def get_all(cls):
        query ="SELECT name, ROUND(CAST((budget_value) AS FLOAT)/0.9) AS value, main_color FROM project +" \
               "WHERE budget_currency IN ('USD') UNION +" \
               "SELECT name, ROUND(CAST((budget_value) AS FLOAT)*1.2) AS value, main_color FROM project +" \
               "WHERE budget_currency IN ('GBP') UNION +" \
               "SELECT name, ROUND(CAST((budget_value) AS FLOAT)) AS value, main_color FROM project +" \
               "WHERE budget_currency IN ('EUR') ORDER BY value;"
        rows = ConnectDatabase.run_query(query)
        projects = []
        for row in rows:
            projects.append(Project(row[0], row[1], row[2]))

        return projects
