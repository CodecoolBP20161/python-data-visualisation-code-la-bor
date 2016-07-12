SELECT company_name, COUNT(company_name), string_agg (main_color, ' ')
FROM project
GROUP BY company_name;
