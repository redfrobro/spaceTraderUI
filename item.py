class Item:
    def __init__(self, symbol: str, name: str, description: str, units: int = None):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.units = units

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"

    @staticmethod
    def item_from_data(item_data):
        """Create an Item object from an item data dict"""
        return Item(symbol=item_data['symbol'], name=item_data['name'],
                    description=item_data['description'], units=item_data['units'])

