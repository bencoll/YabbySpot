import os
import pymongo
from typing import Dict


class Database:
    URI = os.environ.get("MONGODB_URL")
    DATABASE = pymongo.MongoClient(URI).get_default_database()

    def __init__(self, database: str):
        self.DATABASE = pymongo.MongoClient(self.URI).get_database(database)

    @staticmethod
    def insert(collection: str, data: Dict):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection: str, query: Dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: Dict) -> Dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: Dict, data: Dict):
        Database.DATABASE[collection].replace_one(query, data, upsert=True)

    @staticmethod
    def remove(collection: str, query: Dict):
        Database.DATABASE[collection].delete_one(query)
