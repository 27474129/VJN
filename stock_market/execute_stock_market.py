import asyncio

import tornado.web

from apply_migrations import apply_migrations
from urls import urls
from config import APP_PORT


async def main():
    app = tornado.web.Application(urls, autoreload=True)
    app.listen(APP_PORT)
    await asyncio.Event().wait()


if __name__ == "__main__":
    apply_migrations()
    try:
        asyncio.run(main())
    except Exception as e:
        # TODO: Поменять на логирование
        print(e)
