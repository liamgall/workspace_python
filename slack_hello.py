from slacker import Slacker

slack = Slacker('https://hooks.slack.com/services/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')

# Send a message to #general channel
slack.chat.post_message('#webhook_test', 'Hello fellow slackers!')

# Get users list
#response = slack.users.list()
#users = response.body['members']

# Upload a file
#slack.files.upload('hello.txt')
