from apistar import typesystem


class SubscriptionType(typesystem.Enum):
    enum = ['Monthly', 'Yearly']
    description = 'User Subscription Type.'


class SubscriptionPlan(typesystem.Enum):
    enum = ['Trial', 'Basic']
    description = 'User Subscription Plan.'


class User(typesystem.Object):
    properties = {
        'fullname': typesystem.string(max_length=100, description='User fullname.'),
        'email': typesystem.string(max_length=100, description='User email address.'),
        'subscription_type': SubscriptionType,
        'subscription_plan': SubscriptionPlan
    }


class Method(typesystem.Enum):
    enum = ['Paypal']
    description = 'Payment Method Type.'


class Status(typesystem.Enum):
    enum = ['Succeed', 'Pending', 'Failed']
    description = 'Payment Status Type'


class Payment(typesystem.Object):
    properties = {
        # 'user_id': User,
        'amount': typesystem.number(maximum=1000000, description='Payment Amount.'),
        # 'length': typesystem.string(max_length=100),  # time
        'method': Method,
        # 'data': typesystem.string(max_length=100),
        'status': Status,
        # 'date': Quality  # time
    }


class Quality(typesystem.Enum):
    enum = ['Low', 'Medium', 'High']
    description = 'Video Quality Type.'


class Video(typesystem.Object):
    properties = {
        'title': typesystem.string(max_length=100, description='Video Title.'),
        # 'length': typesystem.string(max_length=100),# time
        'description': typesystem.string(max_length=100, description='Video Description.'),
        # 'release_date': typesystem.string(max_length=100),# time
        'quality': Quality
    }
