

import asyncio
import asyncpg

from config import DB_USERNAME, DB_NAME, DB_PORT, DB_PASSWORD, APP_HOST


# TODO: Добавить логирование
class PostgresConn(object):
    connection_string = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@' \
                        f'{APP_HOST}:{DB_PORT}/{DB_NAME}'
    """
    def __aenter__(self):
        self.conn = await asyncpg.connect(
            user=DB_USERNAME, password=DB_PASSWORD, database=DB_NAME,
            host=APP_HOST, port=DB_PORT
        )
        return self.conn


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()
    """
