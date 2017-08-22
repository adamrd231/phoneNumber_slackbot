import os
from slackclient import SlackClient


SLACK_TOKEN = 'xoxp-55611760100-55622254247-229227602258-fe1e1daf5fc4aa5b1f58eeb6d0e964ba'

slack_client = SlackClient(SLACK_TOKEN)


def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return none

def channel_info(channel_id):
    channel_info = slack_client.api_call("channels.info", channel=channel_id)
    if channel_info:
        return channel_info['channel']
    return None


def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='pythonbot',
        icon_emoji=':100:'
    )



if __name__ == '__main__':
    print('-----')
    # Create a list of all the channels currently in slack
    channels = list_channels()
    # If this list exists, print out all of the channels to the terminal
    if channels:
        print("Channels: ")
        for channel in channels:
            #Print the name of the channel, along with the ID
            print(channel['name'] + " (" + channel['id'] + ")")
            detailed_info = channel_info(channel['id'])
            if channel['id'] == "C1MJA7JF9":
                print('All messages from ' + channel['name'] + ":")
                print(channel)


        print('-----')
    else:
        print("Unable to authenticate.")
