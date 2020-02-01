import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(init=True, repr=True, eq=True)
class Post:
    """Class for managing writing posts"""
    collection: str = field(init=False, default="posts")
    author: str
    title: str
    subtitle: str
    date_created: datetime
    date_last_edited: datetime
    featured: bool = False
    _id: str = field(repr=False, default_factory=lambda: uuid.uuid4().hex)

    def json(self):
        return {
            '_id': self._id,
            'author': self.author,
            'title': self.title,
            'subtitle': self.subtitle,
            'date_created': self.date_created,
            'date_last_edited': self.date_last_edited,
            'featured': self.featured
        }
