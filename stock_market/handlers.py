import tornado.web

from postgres_conn import PostgresConn


class StocksHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write('Hello, World')
