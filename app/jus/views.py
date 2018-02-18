from app.jus.models import Video, User

from apistar.backends.sqlalchemy_backend import Session


def create_video(session: Session, title: str, length: str, description: str, release_date: str, quality: str):
    """
Cast given locale to string. Supports also callbacks that return locales.
        title:
            Object or class to use as a possible parameter to locale calla   ble
        length:
            Locale object or string or callable that returns a locale.
    """
    video = Video(title=title, length=length, description=description, release_date=release_date, quality=quality)
    session.add(video)
    session.flush()
    return {'id': video.id, 'title': video.title}


def list_video(session: Session):
    """
    List videos.
    """
    queryset = session.query(Video).all()
    return [
        {'id': video.id, 'title': video.title, 'length': video.length, 'description': video.description,
         'release_date': video.release_date}
        for video in queryset
    ]


def create_user(session: Session, fullname: str, email: str, payment: str, subscription_type: str,
                subscription_plan: str):
    """
    Create User.
    """
    user = User(fullname=fullname, email=email, payment=payment, subscription_type=subscription_type,
                subscription_plan=subscription_plan)
    session.add(user)
    session.flush()
    return {'id': user.id, 'title': user.fullname}


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
