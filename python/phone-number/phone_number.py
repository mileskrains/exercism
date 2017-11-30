class Phone(object):
    def __init__(self, phone_number):
        self._raw = phone_number
        ph = ''.join(ch for ch in phone_number if ch.isdigit())
        ph = ph[1:] if len(ph) == 11 and ph[0] == '1' else ph
        if len(ph) != 10 or int(ph[0]) < 2 or int(ph[3]) < 2:
            raise ValueError
        self.number = ph
        self.area_code = ph[:3]

    def pretty(self):
        ph = self.number
        return f'({ph[:3]}) {ph[3:6]}-{ph[6:]}'

