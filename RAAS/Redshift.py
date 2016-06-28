import psycopg2
import os

class Redshift:

    def __init__(self, connection_string = None, schema = "Tests"):

        if connection_string is None:
            self.connection_string = os.environ.get("REDSHIFT_CONN_STRING")
        else:
            self.connection_string = connection_string

        self.schema = schema
        self.table_lookup = []

    def create_table(self, columns):
        raise NotImplementedError()

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
