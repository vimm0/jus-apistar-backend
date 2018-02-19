from apistar.handlers import docs_urls, static_urls
from apistar import Include, Route

from app.jus.views import create_video, list_video, create_user, list_user, create_payment, list_payment

routes = [
    Route('/v1/create/video', 'POST', create_video),
    Route('/v1/list/video', 'GET', list_video),

    Route('/v1/create/user', 'POST', create_user),
    Route('/v1/list/user', 'GET', list_user),

    Route('/v1/payment', 'POST', create_payment),
    Route('/v1/list/payment', 'POST', list_payment),

    Include('/docs', docs_urls),
    Include('/static', static_urls)
]
