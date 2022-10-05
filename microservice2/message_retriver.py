import ast
import json
import os
import redis



def connect():
    connection = redis.Redis(
        host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT")
    )
    return connection


def get_messages_from_redis():
    r = connect()
    my_list = []
    for key in r.scan_iter():
        data = r.get(key)
        my_dict = data.decode("utf-8")
        mydata = ast.literal_eval(my_dict)
        my_list.append(mydata)
    return my_list
