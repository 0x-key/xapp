""" Api Health Model """
from pydantic import BaseModel


class ApiHealth(BaseModel):
    """ Api Health Model """
    version: str
