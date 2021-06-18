import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC2bef2472ed1e925cb1b9e4eaac90e8bc'
auth_token = '40ef138458115c9e414e852b3714bc99'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+18302993598',
                     to='+18183123563'
                 )

print(message.sid)
