import bleach
from validate_email_address import validate_email
from microservice1 import redis_service

# Creates the response that gets send to the user upon receiving a valid complaint
def create_response_to_user(email):
    return_message = f"Hello, {email}.We have recieved your complaint, and will get in touch with you within 24 hours. This is an auto generated message.".format(
        email
    )
    return return_message


# Checks if the users email exsists
def validate_user_email(email):
    isvalid = validate_email(email, verify=True)
    if isvalid is not True:
        raise Exception(f"The E-mail '{email}' is invalid.")


def sanitize_user_subject(subject):
    sanitized_subject = bleach.clean(subject)
    return sanitized_subject


def sanitize_user_complaint(complaint):
    sanitized_complaint = bleach.clean(complaint)
    return sanitized_complaint


# Wrapper for all the methods that deal with the users complaint
def handle_user_complaint(data):
    try:
        validate_user_email(data["email"])
        sanitize_user_subject(data["subject"])
        sanitize_user_complaint(data["complaint"])
        redis_service.send_messages_to_redis(data)
    except Exception as _e:
        return "Following error occured: " + str(_e)

    return create_response_to_user(data["email"])
