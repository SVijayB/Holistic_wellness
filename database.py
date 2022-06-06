import pymongo
from dotenv import load_dotenv
import os


class Database(object):
    load_dotenv()
    URI = os.getenv("MONGO_URI")
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["holistic_wellness"]
        print(client.list_database_names())

    @staticmethod
    def insert(collection, data):
        return Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection, query, value):
        return Database.DATABASE[collection].update_one(query, value)
