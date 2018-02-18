from apistar import Include, Route
from apistar.backends import sqlalchemy_backend
from apistar.frameworks.wsgi import WSGIApp as App
from apistar.handlers import docs_urls, static_urls
from apistar import environment, typesystem
from json import JSONEncoder

from app.jus.models import Base, Video

from apistar.backends.sqlalchemy_backend import Session


def create_video(session: Session, title: str, length: str, description: str, release_date: str, quality: str):
    video = Video(title=title, length=length, description=description, release_date=release_date, quality=quality)
    session.add(video)
    session.flush()  # Flush the changes to the database. This will populate the customer id.
    return {'id': video.id, 'title': video.title}


def list_video(session: Session):
    queryset = session.query(Video).all()
    return [
        {'id': video.id, 'title': video.title, 'length': video.length, 'description': video.description,
         'release_date': video.release_date, 'quality': video.quality}
        for video in queryset
    ]


routes = [
    Route('/create', 'POST', create_video),
    Route('/list', 'GET', list_video),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]


class Env(environment.Environment):
    properties = {
        'DEBUG': typesystem.boolean(default=False),
        'DATABASE_URL': typesystem.string(default='sqlite:///db.sqlite3')
    }


env = Env()

# Configure database settings.
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

app = App(routes=routes,
          settings=settings,
          commands=sqlalchemy_backend.commands,  # Install custom commands.
          components=sqlalchemy_backend.components  # Install custom components.
          )

if __name__ == '__main__':
    app.main()
