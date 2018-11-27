from flask import Flask
from twilio.rest import Client
from os import environ as env

app = Flask(__name__)


@app.route("/callback")
def notify():
    account_sid = env['TWILIO_ACCOUNT_SID']
    auth_token  = env['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to=env['CALL_TO'],
                            from_=env['CALL_FROM']
                        )

    return call.sid

if __name__ == "__main__":
    app.run()