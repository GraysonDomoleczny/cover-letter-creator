from fastapi import FastAPI
from google_doc_access import google_doc_access


app = FastAPI()

@app.post("/")
async def recieve_job(job: dict):
    print(job["description"])
    print(job["location"])
    print(job["organization"])
    print(job["title"])


service, doc_id = google_doc_access()

service.documents().batchUpdate(
    documentId=doc_id,
    body={
        'requests': [
            {
                'insertText': {
                    'location': {
                        'index': 250
                    },
                    'text': 'this is writing to a doc'
                } 
            }
        ]
    }
).execute()
















































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
