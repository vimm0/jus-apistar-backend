from apistar import typesystem


class SubscriptionType(typesystem.Enum):
    enum = ['Monthly', 'Yearly']


class SubscriptionPlan(typesystem.Enum):
    enum = ['Trial', 'Basic']


class User(typesystem.Object):
    properties = {
        'fullname': typesystem.string(max_length=100),
        'email': typesystem.string(max_length=100),
        'subscription_type': SubscriptionType,
        'subscription_plan': SubscriptionPlan
    }


class Method(typesystem.Enum):
    enum = ['Paypal']


class Status(typesystem.Enum):
    enum = ['Succeed', 'Pending', 'Failed']


class Payment(typesystem.Object):
    properties = {
        # 'user_id': User,
        'amount': typesystem.number(maximum=1000000),
        # 'length': typesystem.string(max_length=100),  # time
        # 'method': Method,
        # 'data': typesystem.string(max_length=100),
        # 'status': Status,
        # 'date': Quality  # time
    }


class Quality(typesystem.Enum):
    enum = ['Low', 'Medium', 'High']


class Video(typesystem.Object):
    properties = {
        'title': typesystem.string(max_length=100),
        # 'length': typesystem.string(max_length=100),# time
        'description': typesystem.string(max_length=100),
        # 'release_date': typesystem.string(max_length=100),# time
        'quality': Quality
    }
