from fastapi import FastAPI
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

app = FastAPI()

@app.post("/")
async def recieve_job(job: dict):
    print(job["description"])
    print(job["location"])
    print(job["organization"])
    print(job["title"])

    SCOPES = ["https://www.googleapis.com/auth/documents"]
    DOCUMENT_ID = "13b1HFZRQ-eNUwLWv3Ei3qYiep1MEpcEm9q0nKOKTFIM"

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("docs", "v1", credentials=creds)

        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        print(f"The title of the document is: {document.get('title')}")
    except HttpError as err:
        print(err)






















    # SCOPES = ["https://www.googleapis.com/auth/documents"]

    # creds = None

    # if os.path.exists("token.json"):
    #     creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # if not creds or not creds.valid:
    #     if creds and creds.expired and creds.refresh_token:
    #         creds.refresh(Request())
    #     else:
    #         flow = InstalledAppFlow.from_client_secrets_file(
    #             "credentials.json", SCOPES
    #         )
    #         creds = flow.run_local_server(port=0)

    #     with open("token.json", "w") as token:
    #         token.write(creds.to_json())

    # service = build("docs", "v1", credentials=creds)

    # document = service.documents().create(
    #     body={"title": "Cover Letter Creator Test"}
    # ).execute()

    # document_id = document["documentId"]

    # service.documents().batchUpdate(
    #     documentId=document_id,
    #     body={
    #         "requests": [
    #             {
    #                 "insertText": {
    #                     "location": {"index": 1},
    #                     "text": job["description"]
    #                 }
    #             }
    #         ]
    #     }
    # ).execute()

    # print("Document created!")
    # print("https://docs.google.com/document/d/" + document_id + "/edit")
