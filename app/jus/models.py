from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import sqlalchemy as sa

# from sqlalchemy_imageattach.entity import image_attachment, Image
from sqlalchemy_utils import ChoiceType, EmailType, JSONType

Base = declarative_base()


class User(Base):
    TYPE = [
        (u'monthly', u'Monthly'),
        (u'quaterly', u'Quaterly'),
        (u'yearly', u'Yearly'),
    ]
    PLAN = [
        (u'Trial', u'Trial'),
        (u'basic', u'Basic'),
        (u'premium', u'Premium'),
    ]
    __tablename__ = "user"
    id = sa.Column(sa.Integer, primary_key=True)
    fullname = sa.Column(sa.String(255))
    email = sa.Column(EmailType)
    payment = relationship("Payment")
    subscription_type = sa.Column(ChoiceType(TYPE))
    subscription_plan = sa.Column(ChoiceType(PLAN))


class Payment(Base):
    METHOD = [
        (u'paypal', u'Paypal'),
        (u'paytm', u'Paytm'),
    ]
    STATUS = [
        (u'succeed', u'Succeed'),
        (u'pending', u'Pending'),
        (u'failed', u'Failed'),
    ]
    __tablename__ = "payment"
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('user.id'))
    amount = sa.Column(sa.Float(255))
    method = sa.Column(ChoiceType(METHOD))
    data = sa.Column(JSONType)
    status = sa.Column(ChoiceType(STATUS))
    date = sa.Column(sa.DateTime, default=sa.func.now())


class Video(Base):
    Quality = [
        (u'low', u'Low'),
        (u'medium', u'Medium'),
        (u'high', u'High'),
    ]
    __tablename__ = "video"
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(255))
    length = sa.Column(sa.Time(255))
    description = sa.Column(sa.String(255))
    # thumbnail = image_attachment('VideoThumbnail')
    release_date = sa.Column(sa.DateTime)
    quality = sa.Column(ChoiceType(Quality))

# class VideoThumbnail(Base, Image):
#     video_id = sa.Column(sa.Integer, sa.ForeignKey('video.id'), primary_key=True)
#     video = relationship('Video')
#     __tablename__ = 'video_thumbnail'
