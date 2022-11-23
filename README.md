# publication-date-updater
## Description
The publication-date-updater API can be used to update the publication date of a dataset in a Dataverse instance.
When migrating data to a Dataverse the publication date will use the current date and cannot be added to the metadata.
This API makes it possible to use the actual publication date for the dataset. 
**BEWARE:** When updating the publication date the dataset will also automatically be published.

## Frameworks
This project uses:
- Python 3.9
- FastAPI
- Poetry

## Setup
The default port in the example .env is 8081, change it to fit your needs.
1. `cp dot_env_example .env`
2. `make build`
3. Go to http://0.0.0.0:8081/docs

## End-points
### Version
Returns the current version of the API

### Publication date updater
Updates the publication date of a dataset and publishes it.
####Parameters
- base_url - e.g. _https://portal.odissei.nl/_ - The URL of the Dataverse instance.
- api_token - e.g. _12345678-ab12-12ab-abcd-a1b2c3d4e5g6_ - API token of the specific Dataverse. (Login to the Dataverse instance as admin and click your username in the top right to find your token.)
- pid - e.g. _doi:10.5072/FK2/1YCZOL_ - DOI or HANDLE permanently identifying the dataset.
- publication date - e.g. _2000-01-30_ - Dataset's original publication date

#### Return value
When successful, the API call will return a confirmation message containing the dataset's PID.
The call will return an exception on a failed attempt further elaborating what went wrong.