from pymongo import MongoClient


class MongoORM(object):
    def __init__(self, db_name, host='localhost', port=27017):
        client = MongoClient(host, port)
        self.db = client[db_name]

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.db.close()

    def select(self, name_collection, search_dict):
        collection = self.db[name_collection]
        return collection.find(search_dict, {'_id': False})

    def distinct(self, name_collection, field):
        collection = self.db[name_collection]
        return collection.distinct(field)

    def insert(self, json, name_collection):
        collection = self.db[name_collection]
        collection.insert(json)
        return 0

    def count(self, name_collection):
        collection = self.db[name_collection]
        return collection.count()

    def drop_collection(self, name_collection):
        self.db.drop_collection(name_collection)
        return 0

    def drop_database(self, database):
        db = self.db
        db.drop_database(database)
        return 0
