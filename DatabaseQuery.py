from typing import Callable
from uuid import uuid4


class DatabaseQuery:
    query: str
    values: tuple
    transactional: bool
    # If is set, this query will be considered transactional
    next_query: 'DatabaseQuery'
    id: str
    fetch: bool
    database: str
    def __init__(self, query, values=None, next_query=None, fetch=False, database = None) -> None:
        self.database = database
        self.query = query
        self.values = values
        self.transactional = bool(next_query)
        self.next_query = next_query
        self.fetch = fetch
        self.id = str(uuid4())

    def put_next_query(self, query):
        self.next_query = query
        self.transactional = True

    def cache_to_file():
        raise NotImplementedError("Must implement")
