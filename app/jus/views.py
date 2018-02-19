from app.jus import schemas
from app.jus.models import Video, User, Payment

from apistar.backends.sqlalchemy_backend import Session


def create_video(session: Session, video: schemas.Video):
    """Cast given locale to string. Supports also callbacks that return locales.
        title:
            Object or "class" to use as a possible parameter to locale calla   ble
        length:
            Locale object or string or callable that returns a locale.
    """
    obj = Video(**video)
    session.add(obj)
    session.flush()
    return {'id': obj.id, 'title': obj.title}


def list_video(session: Session):
    """
    List videos.
    """
    queryset = session.query(Video).all()
    return [
        {'id': video.id, 'title': video.title, 'length': video.length, 'description': video.description,
         'release_date': video.release_date, 'quality': video.quality}
        for video in queryset
    ]


def create_user(session: Session, user: schemas.User):
    """
    Create User.
    """
    obj = User(**user)
    session.add(obj)
    session.flush()
    return {'id': obj.id, 'fullname': obj.fullname}


def list_user(session: Session):
    """
    List Users.
    """
    queryset = session.query(User).all()
    return [
        {'id': user.id, 'fullname': user.fullname, 'email': user.email, 'payment': user.payment,
         'subscription_type': user.subscription_type, 'subscription_plan': user.subscription_plan}
        for user in queryset
    ]


# Involves relations.
def create_payment(session: Session, payment: schemas.Payment):
    """
    Create Payment and relation involve with User.
    """
    obj = Payment(**payment)
    session.add(obj)
    session.flush()
    return {'id': obj.id, 'method': obj.method, 'status': obj.status}


def list_payment(session: Session):
    """
    List Payment.
    """
    queryset = session.query(Payment).all()
    return [
        {'id': obj.id, 'user_id': obj.user_id, 'amount': obj.amount, 'method': obj.method}
        for obj in queryset
    ]
