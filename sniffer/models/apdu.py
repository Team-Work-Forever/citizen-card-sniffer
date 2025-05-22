class APDU():
    def __init__(self, cla, ins, p1, p2, payload):
        self.cla = cla
        self.ins = ins
        self.p1 = p1
        self.p2 = p2
        self.payload: bytes = payload

    def extract_pin(self) -> str:
        return ''.join(chr(b) for b in self.payload if 0x30 <= b <= 0x39)
