import os
from twilio.rest import Client

# Tus credenciales de Twilio
account_sid = 'ACd3646fe88e68c40a3f92fee83044954c'
auth_token = 'd01dacadae40a9ea62df2c567241c0e6'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
  content_variables='{"1":"12/1","2":"3pm"}',
  to='whatsapp:+5492664745297'
)

print(message.sid)
