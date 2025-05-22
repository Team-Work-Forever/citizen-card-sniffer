from dataclasses import dataclass
from store import StoreObject

from models import parse_response

@dataclass
class AddressInfo(StoreObject):
    district: str
    municipality: str
    street_name: str
    civil_parish: str
    floor: str
    door_in: str
    side: str
    place: str
    locality: str
    zip: str
    postal_locality: str

    def get_key(self):
        return "address-info"

    def get_data(self):
        # put in json
        return f"{self.district} {self.civil_parish}"

def parse_address_info(text: str) -> AddressInfo:
    return AddressInfo(**parse_response(text))