import json
import requests
from fastapi import FastAPI, HTTPException
from schema.input import UpdaterInput
from version import get_version

app = FastAPI()


@app.get("/version")
async def info():
    result = get_version()
    return {"version": result}


@app.post("/publication-date-updater")
async def update_publication_date(updater_input: UpdaterInput):
    headers = {
        "X-Dataverse-key": updater_input.dataverse_information.api_token,
        'Content-Type': 'application/ld+json'}
    url = f'{updater_input.dataverse_information.base_url}/api/datasets/:persistentId/actions/:releasemigrated?persistentId={updater_input.pid}'
    publication_date = {
        "schema:datePublished": f'{updater_input.publication_date}',
        "@context": {"schema": "http://schema.org/"}}
    r = requests.post(url, data=json.dumps(publication_date), headers=headers)
    if not r.ok:
        raise HTTPException(status_code=r.status_code, detail=r.reason)
    return r.text
