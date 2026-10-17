from fastapi import FastAPI
from google_doc_access import google_doc_access
from google_sheet_access import google_sheet_access
import webbrowser
from datetime import date


app = FastAPI()

@app.post("/")
async def recieve_job(job: dict):

    job['address'] = 'Not Found'

    if job['action'] == 'generateLetter':
        doc_service, doc_id = google_doc_access(f"{job['organization']} - {job['title']}")

        webbrowser.open(f"https://docs.google.com/document/d/{doc_id}/edit")


        # insert job title
        doc_service.documents().batchUpdate(
            documentId=doc_id,
            body={
                'requests': [
                    {
                        'deleteContentRange': {
                            'range': {
                                'startIndex': 242,
                                'endIndex': 256
                            }
                        }
                    },
                    {
                        'insertText': {
                            'location': {'index': 242},
                            'text': job['title']
                        } 
                    }
                ]
            }
        ).execute()

        # insert job location
        doc_service.documents().batchUpdate(
            documentId=doc_id,
            body={
                'requests': [
                    {
                        'deleteContentRange': {
                            'range': {
                                'startIndex': 222,
                                'endIndex': 236
                            }
                        }
                    },
                    {
                        'insertText': {
                            'location': {'index': 222},
                            'text': job['location']
                        } 
                    }
                ]
            }
        ).execute()

        # insert job address if exists
        if job['address'] != 'Not Found':
            doc_service.documents().batchUpdate(
                documentId=doc_id,
                body={
                    'requests': [
                        {
                            'deleteContentRange': {
                                'range': {
                                    'startIndex': 207,
                                    'endIndex': 221
                                }
                            }
                        },
                        {
                            'insertText': {
                                'location': {'index': 207},
                                'text': job['address']
                            } 
                        }
                    ]
                }
            ).execute()

        # delete job address if not exists
        else:
            doc_service.documents().batchUpdate(
                documentId=doc_id,
                body={
                    'requests': [
                        {
                            'deleteContentRange': {
                                'range': {
                                    'startIndex': 207,
                                    'endIndex': 222
                                }
                            }
                        },
                    ]
                }
            ).execute()

        # insert job organization
        doc_service.documents().batchUpdate(
            documentId=doc_id,
            body={
                'requests': [
                    {
                        'deleteContentRange': {
                            'range': {
                                'startIndex': 194,
                                'endIndex': 206
                            }
                        }
                    },
                    {
                        'insertText': {
                            'location': {'index': 194},
                            'text': job['organization']
                        } 
                    }
                ]
            }
        ).execute()

        # insert todays date
        date_today = date.today().strftime("%B %d, %Y")
        doc_service.documents().batchUpdate(
            documentId=doc_id,
            body={
                'requests': [
                    {
                        'deleteContentRange': {
                            'range': {
                                'startIndex': 177,
                                'endIndex': 193
                            }
                        }
                    },
                    {
                        'insertText': {
                            'location': {'index': 177},
                            'text': date_today
                        } 
                    }
                ]
            }
        ).execute()


    if job['action'] == 'logToSpreadsheet':
        sheet_service, sheet_id = google_sheet_access()

        webbrowser.open(f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit")
        
        
        sheet_service.spreadsheets().values().append(
            spreadsheetId=sheet_id,
            range="Sheet1!A:B",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body={
                'values': [
                    [
                        job["organization"],   
                        job["title"]
                    ]
                ]
            }
        ).execute()

