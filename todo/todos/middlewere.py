import time
from idlelib import query

from django.db import connection
from sqlparse import sql


class QueryLogsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response= self.get_response(request)
        print(f'Query path: {request.path}, Query time: {time.time() - start_time}')
        print(f"Query count: {len(connection.queries)}, Queries: f{[query['sql']  for query in connection.queries]}")
        return response