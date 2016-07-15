from connect_db import ConnectDatabase


class Hq():
    def __init__(self, name, value, color):
        self.name = str(name.encode('utf-8'))
        self.value = value
        self.color = color

    @classmethod
    def get_all(cls):
        query = "SELECT company_hq, ROUND(CAST((budget_value) AS FLOAT)/0.9) AS value, main_color FROM project \
            WHERE budget_currency IN ('USD') AND company_hq IS NOT NULL AND main_color IS NOT NULL UNION \
            SELECT company_hq, ROUND(CAST((budget_value) AS FLOAT)*1.2) AS value, main_color FROM project \
            WHERE budget_currency IN ('GBP') AND company_hq IS NOT NULL AND main_color IS NOT NULL UNION \
            SELECT company_hq, ROUND(CAST((budget_value) AS FLOAT)) AS value, main_color FROM project \
            WHERE budget_currency IN ('EUR') AND company_hq IS NOT NULL AND main_color IS NOT NULL ORDER BY value;"
        rows = ConnectDatabase.run_query(query)
        hqs = []
        for row in rows:
            hqs.append(Hq(row[0], row[1], row[2]))

        return hqs
