import uuid
from dataclasses import dataclass, field
from datetime import datetime

from common import Database


@dataclass(init=True, repr=True, eq=True)
class Post:
    """Class for managing writing posts"""
    collection: str = field(init=False, default="posts")
    author: str
    title: str
    subtitle: str
    content: str
    featured: bool = False
    date_created: datetime = None
    date_last_edited: datetime = None
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

    def save_to_db(self):
        if self.date_created is None:
            # This case occurs when a new post is submitted
            self.date_created = datetime.now()
            self.date_last_edited = self.date_created
        elif self.date_last_edited is None:
            # This case happens when a post is edited
            self.date_last_edited = datetime.now()
        Database.update(self.collection, {'_id': self._id}, self.json())
