from sched import scheduler
import sys
import os
from flask import Flask
from flask_apscheduler import APScheduler
from flask_restful import Api

sys.path.append("..")
app = Flask(__name__)
api = Api(app)
scheduler = APScheduler()
scheduler.init_app(app)

# THIS HAS BE HERE IN ORDER FOR FLASK TO WORK, DON'T MOVE IT TO THE TOP OF THE MODULE
from microservice1 import api_service
from microservice2 import send_email_to_company

# Cron task that will execute every morning at 5.
@scheduler.task("cron", id="send_messages", hour=5)
def get_data():
    with scheduler.app.app_context():
        return send_email_to_company.send()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    scheduler.start()
    app.run(debug=False, host="0.0.0.0", port=port)
