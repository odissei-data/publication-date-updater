from pydantic import BaseModel


class DataverseInformation(BaseModel):
    base_url: str
    api_token: str


class UpdaterInput(BaseModel):
    pid: str
    publication_date: str
    dataverse_information: DataverseInformation
