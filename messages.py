from slackclient import SlackClient
import time
import os


SLACK_TOKEN = 'xoxp-55611760100-55622254247-229227602258-fe1e1daf5fc4aa5b1f58eeb6d0e964ba'

slack_client = SlackClient(SLACK_TOKEN)


if slack_client.rtm_connect():
    while True:
        events = slack_client.rtm_read()
        for event in events:
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']

                if len(text) == 10:
                    phoneNumber = True
                    for digit in text:
                        if not int(digit):
                            phoneNumber = False
                    if phoneNumber == True:
                        message = "Morty, idiot.. Phone numbers get formatted:"
                        phone_format = "(" + text[:3] + ") " + text[3:6] + "-" + text[6:10]
                        final_output =  message +  "\n" + phone_format

                    slack_client.api_call(
                        'chat.postMessage',
                        channel=channel,
                        text=final_output,
                        as_user='true:'
                    )
        time.sleep(1)
else:
    print('Connection failed, invalid token?')
