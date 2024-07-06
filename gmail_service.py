from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch
from langchain_community.tools.gmail.utils import (
    build_resource_servive,
    get_gmail_credentials,
)


credentials = get_gmail_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)
search = GmailSearch(api_resource=api_resource)
emails = search("in:inbox")

mails = []

def get_mails():
    for email in emails:
        mails.append(
            {
                "id": email["id"],
                "threadId": email["threadId"],
                "snippet": email["snippet"],
                "sender": email["sender"],
            }
        )
    return mails

