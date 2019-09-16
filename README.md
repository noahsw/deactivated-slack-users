# deactivated-slack-users
Get an email when slack users in your workspace are deactivated.

## Installation
`pip3 install sendgrid`

## Command line parameters
`SLACK_API_TOKEN`: Login at https://app.slack.com and inspect the API calls to get this value.

`SLACK_D_COOKIE`: Login at https://app.slack.com and copy the value of your the `d` cookie.

`SENDGRID_API_KEY`: Register at https://www.sendgrid.com

`FROM_EMAIL`: name@domain.com

`TO_EMAIL`: name@domain.com

## Run
`SLACK_API_TOKEN=x SLACK_D_COOKIE=y SENDGRID_API_KEY=z FROM_EMAIL=name@domain.com TO_EMAIL=name@domain.com python3 deactivated-slack-users.py`
