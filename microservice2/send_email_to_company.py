from microservice2 import message_retriver, email_service
from decouple import config

COOPERATE_EMAIL = config('RECEIVER_COOPERATE_EMAIL')



def get_messages():
    return message_retriver.get_messages_from_redis()


def get_relevant_data_from_messages(data):
    my_list = []
    for element in data:
        item_value = get_values_from_dict(element)
        email = item_value["email"]
        subject = item_value["subject"]
        complaint = item_value["complaint"]
        my_object = {"email": email, "subject": subject, "complaint": complaint}
        my_list.append(my_object)
    return my_list


def get_values_from_dict(item):
    keyList = list(item.values())
    value = keyList[0]
    return value


# THIS IS A MESS, THAT WILL BE FIXED LATER
def send():
    some_list = get_relevant_data_from_messages(get_messages())
    for element in some_list:
        email = element["email"]
        subject = element["subject"]
        complaint = element["complaint"]
        email_message = f"There is a new complaint from {email}, please address this as fast as possible. The complaint goes as follows: {complaint}".format(
            email, complaint
        )
        email_service.send_message(COOPERATE_EMAIL, subject, email_message)
