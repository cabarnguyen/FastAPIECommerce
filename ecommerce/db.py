from . import config
from pymongo import mongo_client

client = mongo_client.MongoClient(f'mongodb://{config.DATABASE_USERNAME}:{config.DATABASE_PASSWORD}@{config.DATABASE_HOST}/{config.DATABASE_NAME}')
print('Connected to MongoDB...')
db = client.commerce

users = db.get_collection('users')

