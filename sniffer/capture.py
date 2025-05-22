import pyshark

from models.apdu import APDU
from event import EventHandler, Events
from store import StoreHandler 
from validator import get_events

class Consumer():
    file = 'data/otta_boy.pcapng'
    has_connected: bool = False

    def __init__(self):
        self.capture = pyshark.FileCapture(
            self.file, 
            display_filter='usb',
            use_json=True,         
            include_raw=True,
        )

        self.store_handler = StoreHandler()
        self.event_handler = EventHandler(self.store_handler)
    
    def __parse_apdu(self, apdu):
        if len(apdu) < 4:
            return "Invalid APDU"

        cla, ins, p1, p2 = apdu[:4]
        rest = apdu[4:]

        return APDU(cla=cla, ins=ins, p1=p1, p2=p2, payload=rest)

    def add_apdu(self, data: bytes):
        parsed_data = self.__parse_apdu(data)
        self.event_handler.on_event(get_events(parsed_data), parsed_data)

    def notify_connected(self, data: bytes):
        parsed_data = self.__parse_apdu(data)
        self.event_handler.on_event(Events.CONNECTED, parsed_data)
        self.has_connected = True

    def start(self):
        for pkt in self.capture:
            if not 'USB' in pkt:
                continue

            usb_layer = pkt['USB']

            if not hasattr(usb_layer, 'transfer_type'):
                continue

            transfer_type = int(usb_layer.transfer_type, 16)

            if hasattr(usb_layer, 'capdata'):
                pass

            if  'DATA' in pkt and hasattr(pkt['DATA'], 'data'):
                hex_data = pkt['DATA'].data.replace(':', '')
                apdu_bytes = bytes.fromhex(hex_data)

                if transfer_type == 3 and not self.has_connected:
                    self.notify_connected(apdu_bytes)
                else:
                    self.add_apdu(apdu_bytes)