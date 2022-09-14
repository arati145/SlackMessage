#importing required libraries

import requests
import sys
import getopt
import json

#enter your webhook url in the response section
#to send a message to slack channel

def send_slack_message(message):
    payload ='{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
        data = payload)
    print(response.text)
    create_issue(message)

def create_issue(message):
    headers={
    "Accept": "application/json",
    "Content-Type": "application/json"
    }
    value = {
        "fields": {
        "project":{
        "key":"DEMOSAMPLE" #enter your valid jira project id here.
        },
        "summary":message,
        "description" : "Issue created using slack",
        "issuetype":{
        "name":"Task"
        }
        }
        }
    payload = json.dumps(value)

    #enter your valid jira project url and email below
    response = requests.post('https://bootcamp-training.atlassian.net/rest/api/2/issue',
        headers = headers,
        data = payload,
        auth=("aaruwable16@gmail.com", "QiZgFsY1QIZjEJAuC3m98F06"))
    data = response.json()
    print(data)

def main(argv):
    message =" "

    try: opts, args = getopt.getopt(argv, "hm:",["message="])

    except getopt.GetoptError:
        print('SlackMessage.py -m <message>')
        sys.exit(2)

    if len(opts)==0:
        print('provide a valid message')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('SlackMessage.py -m <message>')
            sys.exit()
        elif opt in ("-m","--message"):
            message= arg

    send_slack_message(message)

if __name__ == "__main__":
    main(sys.argv[1:])