# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC2a7fd23053a652eed46e874124bda301"
auth_token = "37950282565a26a01034b0c2b47c7652"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+15106935609", from_="+15005550006", body="Hello Sophia!")

print(message.sid)
