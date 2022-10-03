import redis
import json
import os

def connect():
        connection = redis.Redis(host = os.environ.get('REDIS_HOST'), 
        port = os.environ.get('REDIS_PORT'))
        return connection

def get_keys_from_dict(item):
        keyList = list(item.keys())
        key = keyList[0]
        return key

def get_values_from_dict(item):
        keyList = list(item.values())
        value = keyList[0]
        return value


def send_messages_to_redis(message):
        r = connect()
        pipe = r.pipeline()
        pipe.set(message["email"], json.dumps({message["email"]:message}))
        pipe.execute()
        return "Sent message"