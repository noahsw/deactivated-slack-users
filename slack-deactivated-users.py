import os
import json
import requests
import time
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sendgrid_api_key = os.environ["SENDGRID_API_KEY"]
slack_token = os.environ["SLACK_API_TOKEN"]
slack_d_cookie = os.environ["SLACK_D_COOKIE"]
from_email = os.environ["FROM_EMAIL"]
to_email = os.environ["TO_EMAIL"]

uri = "https://slack.com/api/users.list?token=" + slack_token

cookies = {'d': slack_d_cookie}

if os.path.exists("config.json"):
  f = open('config.json')
  config = json.load(f)
  f.close()
else:
  config = { 'last-check': 1568133091 }

r = requests.get(uri, cookies=cookies)
r.status_code
data = r.json()

sorted_members = sorted(data['members'], key = lambda x : x['updated'])

email_contents = ''

print('Members: ' + str(len(sorted_members)))

for member in sorted_members:
  if member['deleted'] == True:
    updated = member['updated']
    if updated > config['last-check'] and member['profile']['real_name']:
      when = datetime.fromtimestamp(member['updated']).strftime('%m/%d/%Y')
      email_contents += member['profile']['real_name'] + ' - ' + member['profile']['title'] + ' (' + when + ')\n'

if len(email_contents) == 0:
  print('Nothing to send!')
else:
  print('Sending mail with contents:')
  print(email_contents)

  message = Mail(
      from_email=from_email,
      to_emails=to_email,
      subject='Deactivated users',
      plain_text_content=email_contents)
  try:
      sg = SendGridAPIClient(sendgrid_api_key)
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
  except Exception as e:
      print(str(e))


config = { 'last-check': time.time() }
with open('config.json', 'w') as f:
  json.dump(config, f)
  print('Updated config to ' + str(config))