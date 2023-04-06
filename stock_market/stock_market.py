import asyncio

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application(
        [("/", MainHandler)], autoreload=True
    )


async def main():
    app = make_app()
    app.listen(8523)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
