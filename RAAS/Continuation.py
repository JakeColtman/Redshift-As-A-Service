from Redshift import Redshift
from psycopg2 import ProgrammingError

class Continuation:

    def __init__(self, conn = Redshift()):
        self.conn = conn
        self.continuation_queries = {}

    def register(self, table, continuation):

        try:
            self.continuation_queries[table].append(continuation)
        except:
            self.continuation_queries[table] = [continuation]

    def trigger(self, table):
        try:
            for continuation in self.continuation_queries:
                self.conn.run_query(continuation)
            return True
        except ProgrammingError:
            return False