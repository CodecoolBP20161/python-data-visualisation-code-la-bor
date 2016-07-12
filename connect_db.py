import psycopg2


class Connect_database:
    # setup connection string
    connect_str = "dbname='eszter' user='eszter' host='localhost' password='postgres'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()

    # def __init__(self, connect_str, conn, cursor):

    @staticmethod
    def run_query(query):
        Connect_database.cursor.execute(query)
        rows = Connect_database.cursor.fetchall()
        print(rows)


    #     # removing the test table if it already exists
    #     cursor.execute("""DROP TABLE IF EXISTS project;""")
    #     # create a new table with a single column called "name"
    #     cursor.execute("CREATE TABLE project (name varchar(50));")
    #     # Insert a row to see something in the output
    #     cursor.execute("""INSERT INTO project VALUES (1, 'Y-find', '2004-12-05 00:29:49', 'Camimbo', 'Adirejo', '#2bb', 'Carolyn Carpenter', '3141.51', 'EUR', 2, FALSE);;""")
    #     # run a SELECT statement
    #     cursor.execute("""SELECT company_name FROM project;""")
    #     # Fetch and print the result of the last execution
    #
    # except Exception as e:
    #     print("Uh oh, can't connect. Invalid dbname, user or password?")
    #     print(e)
query = "SELECT company_name, COUNT(company_name), string_agg (main_color, ' ') FROM project GROUP BY company_name;"
Connect_database.run_query(query)