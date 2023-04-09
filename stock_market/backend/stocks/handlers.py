import logging

import tornado.web

from ..postgres.postgres_conn import PostgresConn


logger = logging.getLogger(__name__)


class StocksHandler(tornado.web.RequestHandler):
    async def get(self):
        async with PostgresConn() as conn:
            stocks = \
                await conn.fetch("""SELECT name, stock_name FROM companies""")
        print(stocks)
        logger.info(f'GET запрос к {__class__}')
        self.write('asd')
