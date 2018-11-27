# misscall

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Call a phone number when a webhook is received.  
You need a twilio account.

## Usage

### Shell script

notify when execution is completed

```bash
#!/bin/bash

# do long running stuff here, example:
$ emerge www-client/google-chrome

# send webhook
curl https://your-misscall-url.herokuapp.com/callback

```