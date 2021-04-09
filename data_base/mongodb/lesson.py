import datetime

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip': ['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}
stack2 = {
    'name': 'customer2',
    'pip': ['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
print(stack_id, type(stack_id))
print('#'*10)
print(db_stacks.find_one({'_id': stack_id}))




