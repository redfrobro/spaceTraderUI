class Item:
    def __init__(self, symbol: str, name: str, description: str, units: int = None):
        self.symbol = symbol
        self.name = name
        self.description = description
        self.units = units

    @staticmethod
    def item_from_data(item_data):
        """Create an Item object from an item data dict"""
        return Item(symbol=item_data['symbol'], name=item_data['name'],
                    description=item_data['description'], units=item_data['units'])

    @staticmethod
    def item_from_symbol(symbol):
        """Create an Item object from an item symbol"""
        item_data = get_item(symbol)
        return Item.item_from_data(item_data)