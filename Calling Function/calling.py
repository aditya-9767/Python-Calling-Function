# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>hello this code runs successfully</Say></Response>',
                        to='',
                        from_=''
                    )

print(call.sid)