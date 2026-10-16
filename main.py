from fastapi import FastAPI
from google_doc_access import google_doc_access


app = FastAPI()

@app.post("/")
async def recieve_job(job: dict):
    service, doc_id = google_doc_access()

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
                },
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
                },
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
                },
            ]
        }
    ).execute()