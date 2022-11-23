from pydantic import BaseModel, Field


class DataverseInformation(BaseModel):
    base_url: str = Field(example="https://portal.odissei.nl/")
    api_token: str = Field(example="12345678-ab12-12ab-abcd-a1b2c3d4e5g6")


class UpdaterInput(BaseModel):
    pid: str = Field(example="doi:10.5072/FK2/1YCZOL")
    publication_date: str = Field(example="2000-01-30")
    dataverse_information: DataverseInformation
