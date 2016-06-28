import psycopg2
import os
import random
import string

class Redshift:

    def __init__(self, connection_string = None, schema = "Tests"):

        if connection_string is None:
            self.connection_string = os.environ.get("REDSHIFT_CONN_STRING")
        else:
            self.connection_string = connection_string

        self.schema = schema
        self.tables = []

    def create_table(self, columns):
        def generate_column_query():
            return ",".join(["{0} {1}".format(col[0], col[1]) for col in columns])

        def random_table_name():
            return "".join([random.choice(string.ascii_letters) for i in range(9)])

        base_query = "CREATE TABLE {0}.{1} ({2});"
        table_name = random_table_name()
        self.run_query(base_query.format(self.schema, table_name, generate_column_query()))
        return table_name

    def run_query(self, query):
        conn = psycopg2.connect(self.connection_string)
        cur = conn.cursor()
        cur.execute(query)
        try:
            result = cur.fetchall()
        except:
            result = []
        cur.close()
        conn.commit()
        conn.close()
        return result

Redshift().create_table([["id", "int"]])