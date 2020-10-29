import pymongo
from datetime import datetime


class DB_Manager:
    client = None
    db = None

    def __init__(self, uri, db_name):
        self.uri = uri
        self.db_name = db_name
        self.client = pymongo.MongoClient(self.uri)
        self.db = self.client[self.db_name]

        # Setup Database
        self.db["devices"].create_index("device_id", unique=True)

    # Database Queries
    def __find(self, collection, query={}):
        return self.db[collection].find(query)

    def __find_one(self, collection, query={}):
        return self.db[collection].find_one(query)

    def __insert_one(self, collection, data):
        return self.db[collection].insert_one(data)

    def __insert_many(self, collection, data):
        return self.db[collection].insert_many(data)

    def __update_one(self, collection, query, data):
        return self.db[collection].update_one(query, data)

    def __insert_or_update(self, collection, query, data):
        return self.db[collection].update_one(query, {"$set": data}, upsert=True)

    # Public Methods
    def update_device_status(self, device_id, occupied):
        device = {
            "device_id": device_id,
            "occupied": occupied,
            "last_update": datetime.utcnow()
        }
        return self.__insert_or_update("devices", {"device_id": device_id}, device)

    def add_to_history(self, device_id, occupied, gateway):
        device = {
            "device_id": device_id,
            "timestamp": datetime.utcnow(),
            "occupied": occupied,
            "gateway": gateway
        }
        return self.__insert_one("history", device)
