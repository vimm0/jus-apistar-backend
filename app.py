from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App
from apistar import environment, typesystem

from app.jus.models import Base
import routes


class Env(environment.Environment):
    properties = {
        'DEBUG': typesystem.boolean(default=False),
        'DATABASE_URL': typesystem.string(default='sqlite:///db.sqlite3')
    }


env = Env()

settings = {
    # "DATABASE": {
    #     "URL": "postgresql://:@localhost/apistar",
    #     "METADATA": Base.metadata
    # },
    "DATABASE": {
        "URL": env['DATABASE_URL'],
        "METADATA": Base.metadata

    }
}

app = App(routes=routes.routes,
          settings=settings,
          commands=sqlalchemy_backend.commands,
          components=sqlalchemy_backend.components
          )

if __name__ == '__main__':
    app.main()
