class Stock:
    def __init__(self):
        self._stock = {}

    def __str__(self):
        return f'{self._stock}'

    def add_to_stock(self, equipment):
        key_dick = f'{equipment.__class__.__name__} {equipment.name} {equipment.model}'
        try:
            self._stock[key_dick] += equipment.quantity
        except KeyError:
            if key_dick not in self._stock:
                self._stock[key_dick] = equipment.quantity

    def extract_stock(self, equipment, quantity):
        quantity = int(quantity)
        key_dict = f'{equipment.__class__.__name__} {equipment.name} {equipment.model}'
        if self._stock[key_dict]:
            self._stock[key_dict] = self._stock[key_dict] - quantity
        if self._stock[key_dict] == 0:
            self._stock.pop(key_dict)


class OfficeEquipment:
    def __init__(self, name, model, price, quantity):
        self.name = name
        self.model = model
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name} {self.model} {self.quantity}'


class Printer(OfficeEquipment):
    def __init__(self, name, model, price, quantity, print_type):
        super().__init__(name, model, price, quantity)
        self.print_type = print_type


class Scanner(OfficeEquipment):
    def __init__(self, name, model, price, quantity, scan_type):
        super().__init__(name, model, price, quantity)
        self.scan_type = scan_type


class Xerox(OfficeEquipment):
    def __init__(self, name, model, price, quantity, print_method):
        super().__init__(name, model, price, quantity)
        self.print_method = print_method


if __name__ == '__main__':
    pr_1 = Printer('HP', 'LJ-1020', 1500, 3, 'laser')
    sc_1 = Scanner('Canon', 'CS-LiDE400', 900, 3, 'flatbed')
    xe_1 = Xerox('Brother', 'DCP-1510R', 1100, 3, 'color-laser')
    stock = Stock()
    stock.add_to_stock(pr_1)
    stock.add_to_stock(sc_1)
    stock.add_to_stock(xe_1)
    print(stock)
    stock.extract_stock(pr_1, 3)
    stock.extract_stock(sc_1, 3)
    stock.extract_stock(xe_1, 3)
    print(stock)
