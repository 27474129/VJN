import asyncpg
import logging

from ..config import CONNECTION_STRING


logger = logging.getLogger(__name__)


class PostgresConn(object):
    async def __aenter__(self):
        self.conn = await asyncpg.connect(CONNECTION_STRING)
        logger.info('Коннект с БД установлен')
        return self.conn

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        logger.info('Коннект с БД разорван')
