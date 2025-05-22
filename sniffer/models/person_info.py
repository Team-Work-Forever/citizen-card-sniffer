from dataclasses import dataclass
from store import StoreObject

from models import parse_response

@dataclass
class PersonInfo(StoreObject):
    surname: str
    given_name: str
    sex: str
    height: str
    nationality: str
    birthdate: str
    n_document: str
    valid_date: str
    mother_surname: str
    mother_given_name: str
    father_surname: str
    father_given_name: str
    nif: str
    social_security: str
    health: str

    def get_key(self):
        return "person-info"

    def get_data(self):
        # put in json
        return f"{self.health} {self.father_given_name}"

def parse_person_info(text: str) -> PersonInfo:
    return PersonInfo(**parse_response(text))