import threading

from ama_api import get_info, get_address_info, sign_document
from enum import Enum
from models.apdu import APDU
from models.person_info import parse_person_info
from models.address_info import parse_address_info
from store import StoreHandler, StoreObject

DOCUMENTS_SIGN = [
    "data/pdfs/sign.pdf"
]

class Events(Enum):
    UNKNOWN = 0
    RECIVED_ADDRESS_PIN = 1
    RECIVED_SIGNATURE_PIN = 2
    CONNECTED = 3

class EventHandler():
    store_handler: StoreHandler

    def __init__(self, store_handler: StoreHandler):
        self.store_handler = store_handler

    def on_event(self, event: Events, data: APDU):
        thread = threading.Thread(target=self.__process_event, args=(event, data))
        thread.start()

    def __process_event(self, event: Events, data: APDU):
        store_obj = None

        try:
            match event:
                case Events.RECIVED_ADDRESS_PIN:
                    store_obj = self.__handle_address_call(data)
                case Events.RECIVED_SIGNATURE_PIN:
                    self.__handle_signature_call(data)
                case Events.CONNECTED:
                    store_obj = self.__handle_connected()

            if not store_obj:
                return

            self.store_handler.set_data(store_obj)
        except Exception as e:
            print(e)

    def __handle_address_call(self, data: APDU) -> StoreObject:
        addr_code = data.extract_pin()
        print(f"Recived: ADDRESS PIN! {addr_code}")
        print("Fetching CC. Address Details...")
        
        try:
            ama_data = get_address_info(addr_code)
            
            if not ama_data:
                raise Exception("there is no data")

            address_info = parse_address_info(ama_data)
        except Exception:
            raise Exception("failed to fetch address info")

        return address_info
        
    def __handle_signature_call(self, data: APDU):
        sign_code = data.extract_pin()
        print(f"Recived: SIGNATURE PIN! {sign_code}")
        print("Signing document batch...")

        try:
            for doc in DOCUMENTS_SIGN:
                sign_document(sign_code, doc, "data/pdfs/out/verify.pdf")

            print("Yes!")
        except Exception as e:
            print(e)

    def __handle_connected(self) -> StoreObject:
        print("Fetching CC. User Details...")
        ama_data = get_info()
        person_info = parse_person_info(ama_data)

        return person_info