import json
import requests
from fastapi import FastAPI, HTTPException
from schema.input import UpdaterInput
from version import get_version

description = """
This dataverse-importer API can be used to import metadata into a given
 dataverse.

"""

tags_metadata = [
    {
        "name": "Version",
        "description": "Returns the version of this API",
    },
    {
        "name": "Publication date updater",
        "description": "Updates the publication date of a given dataset",
        "externalDocs": {
            "description": "This API uses the migration API",
            "url": "https://guides.dataverse.org/en/latest/developers/dataset"
                   "-migration-api.html#publish-a-migrated-dataset",
        },
    },
]

app = FastAPI(
    title="publication-date-updater",
    description=description,
    version="0.1.0",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata
)


@app.get("/version", tags=["Version"])
async def info():
    result = get_version()
    return {"version": result}


@app.post("/publication-date-updater", tags=["Publication date updater"])
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
