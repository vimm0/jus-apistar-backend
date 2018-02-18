from apistar import typesystem


class Quality(typesystem.Enum):
    enum = ['low', 'medium', 'high']


class Video(typesystem.Object):
    properties = {
        'title': typesystem.string(max_length=100),
        # 'length': typesystem.string(max_length=100),
        'description': typesystem.string(max_length=100),
        # 'release_date': typesystem.string(max_length=100),
        'quality': Quality
    }
