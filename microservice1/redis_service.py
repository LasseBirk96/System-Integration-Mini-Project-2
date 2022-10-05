import json
import os
import redis


def connect():
    connection = redis.Redis(
        host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT")
    )
    return connection


def get_keys_from_dict(item):
    key_list = list(item.keys())
    key = key_list[0]
    return key


def get_values_from_dict(item):
    key_list = list(item.values())
    value = key_list[0]
    return value


def send_messages_to_redis(message):
    r = connect()
    pipe = r.pipeline()
    pipe.set(message["email"], json.dumps({message["email"]: message}))
    pipe.execute()
    return "Sent message"
