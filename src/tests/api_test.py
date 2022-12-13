from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_incorrect_publication_date():
    response = client.post(
        "/publication-date-updater",
        json={
            "pid": "doi:10.5072/FK2/DWYPWW",
            "publication_date": "bad date",
            "dataverse_information": {
                "base_url": "https://portal.staging.odissei.nl",
                "api_token": "95ece972-6e98-4239-806e-f225bb6585aa"
            }
        }
    )
    assert response.status_code == 400
    assert response.json() == {'detail': {
        'code': 400,
        'message': 'Bad Request. The API request cannot be completed with '
                   'the parameters supplied. Please check your code for '
                   'typos, or consult our API guide at '
                   'http://guides.dataverse.org.',
        'requestMethod': 'POST',
        'requestUrl': 'http://portal.staging.odissei.nl/api/v1/datasets/'
                      ':persistentId/actions/:releasemigrated?persistentId='
                      'doi:10.5072/FK2/DWYPWW',
        'status': 'ERROR'}}


def test_bad_token():
    response = client.post(
        "/publication-date-updater",
        json={
            "pid": "doi:10.5072/FK2/1YCZOL",
            "publication_date": "2020-10-26",
            "dataverse_information": {
                "base_url": "https://portal.staging.odissei.nl",
                "api_token": "bad token"
            }
        }
    )
    assert response.status_code == 401
    assert response.json() == {
        'detail': {'message': 'Bad api key ', 'status': 'ERROR'}}


def test_nonexistent_dataset():
    response = client.post(
        "/publication-date-updater",
        json={
            "pid": "bad pid",
            "publication_date": "2020-10-26",
            "dataverse_information": {
                "base_url": "https://portal.staging.odissei.nl",
                "api_token": "95ece972-6e98-4239-806e-f225bb6585aa"
            }
        }
    )
    assert response.status_code == 404
    assert response.json() == {
        'detail': {'message': 'Dataset with Persistent ID bad pid not found.',
                   'status': 'ERROR'}}
