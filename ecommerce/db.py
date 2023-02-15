import motor.motor_asyncio

from . import config
from pymongo import mongo_client

from .config import CONNECTION_STRING

connection_string = f'mongodb://{config.DATABASE_USERNAME}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}/{config.DATABASE_NAME}'

# Connection by pymongo
client_py_mongo = mongo_client.MongoClient(connection_string)

# connection by motor
client_motor = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STRING)

print('Connected to MongoDB...')
db = client_py_mongo.commerce
db_motor = client_motor["commerce"]

users = db.get_collection('users')
inventories = db_motor["inventories"]
customers = db_motor["customers"]

