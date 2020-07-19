from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
import base64
import email



# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])


def log_in():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    return service


# Basically subscribes to watch the gmail account from the pickle
def watch_request():

    gmail = log_in()

    request = {
        'labelIds': ['INBOX'],
        'topicName': 'projects/email2voice/topics/emailreceived'
    }

    watchResponse = gmail.users().watch(userId='me', body=request).execute()

    print(watchResponse)

def get_all_mail():
    gmail = log_in()

    emails = gmail.users().messages().list(userId='me').execute()
    print(emails)


def check_email():

    gmail = log_in()

    emails = gmail.users().messages().list(userId='me').execute()

    targetId = emails['messages'][1]['id']

    message = gmail.users().messages().get(userId='me', id=targetId, format='full').execute()


    okText = base64.urlsafe_b64decode(message['payload']['parts'][0]['body']['data'])

    print(message['payload']['parts'][2]['mimeType'])


    # try:
    #     message = service.users().messages().get(userId='me', id=msg_id).execute()
    # except e:
    #     print("error")


if __name__ == '__main__':
    check_email()
