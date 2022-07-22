import jinja2
import aiohttp_jinja2

from aiohttp import web

from app.settings import config, BASE_DIR
from app.store.database.accessor import PostgresAccessor
from app.forum.routers import setup_routes as setup_forum_routes


def setup_config(application):
    application["config"] = config


def setup_routers(application):
    setup_forum_routes(application)


def setup_external_libraries(application: web.Application):
    aiohttp_jinja2.setup(application,
                         loader=jinja2.FileSystemLoader("templates")
                         )


def setup_accessor(application):
    application['db'] = PostgresAccessor()
    application['db'].setup(application)


def setup_app(application):
    setup_external_libraries(application)
    setup_routers(application)
    setup_config(application)
    setup_accessor(application)


app = web.Application()

if __name__ == "__main__":
    setup_app(app)
    web.run_app(app, port=config['common']['port'])