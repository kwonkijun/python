message = "문자봇 테스트 중입니다."

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACc7797bdbfea59b3b37fadf1e6e151ec9'
auth_token = os.environ['4f7f7f81be5515ed668c819cedb5f18f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body=message,
                     from_='+17652685452',
                     to='+821043521929'
                 )

print(message.sid)
