import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def google_doc_access(job):
    SCOPES = [
        "https://www.googleapis.com/auth/documents",
        "https://www.googleapis.com/auth/drive",
        "https://www.googleapis.com/auth/spreadsheets"
    ]

    DOC_ID = "1Cx6W6RZd4ImSRS8PMCuEu0dEl7-DaI5qCHaFq5zaG7c"

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

    doc_service = build("docs", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    copied_doc = drive_service.files().copy(
        fileId=DOC_ID, 
        body={'name': f"Cover Letter_{job["organization"]}_{job["title"]}"}
    ).execute()
    copied_doc_id = copied_doc['id']

    return doc_service, copied_doc_id