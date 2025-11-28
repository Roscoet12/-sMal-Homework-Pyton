class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def addToAddress(self,to_address):
        self.to_address = to_address


    def addFromAddress(self,from_address):
        self.from_address = from_address

    def __str__(self):
        return f'Отправление {self.track} {self.to_address} в {self.from_address}. Стоимость {self.cost} рублей.'
