class Item:
    def __init__(self, item: dict):
        self.symbol = item['symbol']
        self.name = item['name']
        self.description = item['description']
        self.units = item['units']