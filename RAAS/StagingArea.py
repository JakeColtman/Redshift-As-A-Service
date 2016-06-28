import random
import string
from Redshift import Redshift

class StagingArea:

    def __init__(self, conn = Redshift()):

        self.conn = conn
        self.tables = []

    def create_table(self, columns):
        def generate_column_query():
            return ",".join(["{0} {1}".format(col[0], col[1]) for col in columns])

        def random_table_name():
            return "".join([random.choice(string.ascii_letters) for i in range(9)])

        base_query = "CREATE TABLE {0}.{1} ({2});"
        table_name = random_table_name()
        self.conn.run_query(base_query.format(self.schema, table_name, generate_column_query()))
        return table_name