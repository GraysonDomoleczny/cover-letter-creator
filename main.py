from fastapi import FastAPI
from google_doc_access import google_doc_access


app = FastAPI()

@app.post("/")
async def recieve_job(job: dict):

    job['address'] = 'Not Found'

    if job['action'] == 'generateLetter':
        service, doc_id = google_doc_access(f"{job['organization']} | {job['title']}")

        # insert job title
        service.documents().batchUpdate(
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
        service.documents().batchUpdate(
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
            service.documents().batchUpdate(
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
            service.documents().batchUpdate(
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
        service.documents().batchUpdate(
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