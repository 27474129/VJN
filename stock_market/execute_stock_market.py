import asyncio
import logging

import tornado.web

from apply_migrations import apply_migrations
from urls import urls
from backend.config import APP_PORT


async def main():
    app = tornado.web.Application(urls, autoreload=True)
    app.listen(APP_PORT)
    logger.info('Приложение запущено')
    await asyncio.Event().wait()


if __name__ == "__main__":
    # Настройка логирования
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] -  %(name)s - '
               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'
    )

    apply_migrations()
    logger = logging.getLogger(__name__)
    logger.info('Миграции накатились')
    asyncio.run(main())
