from event import Events
from models.apdu import APDU

SIGNATURE_PIN_HEADER = b'\x00\x82\x08'
ADDRESS_PIN_HEADER = b'\x00\x83\x08'

def get_events(apdu: APDU) -> Events:
    if SIGNATURE_PIN_HEADER in apdu.payload:
        return Events.RECIVED_SIGNATURE_PIN

    if ADDRESS_PIN_HEADER in apdu.payload:
        return Events.RECIVED_ADDRESS_PIN
    
    return Events.UNKNOWN
