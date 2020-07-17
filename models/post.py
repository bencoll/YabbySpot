import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from common import Database


@dataclass(init=True, repr=True, eq=True)
class Post:
    """Class for managing writing posts"""
    collection: str = field(init=False, default="posts")
    author: str
    title: str
    subtitle: str
    post_type: str
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
            'post_type': self.post_type,
            'content': self.content,
            'featured': self.featured,
            'date_created': self.date_created,
            'date_last_edited': self.date_last_edited,
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

    @classmethod
    def load_all_by_type(cls, post_type: str = None) -> List:
        db_elements = Database.find(cls.collection, {"type": post_type})
        return [cls(**elem) for elem in db_elements]
