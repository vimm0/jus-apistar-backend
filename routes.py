from apistar.handlers import docs_urls, static_urls
from apistar import Include, Route

from app.jus.views import create_video, list_video, create_user, list_user

routes = [
    Route('/create/video', 'POST', create_video),
    Route('/list/video', 'GET', list_video),

    Route('/create/user', 'POST', create_user),
    Route('/list/user', 'GET', list_user),

    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
