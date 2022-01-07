class Cashiers:
    def __init__(self, cashier_name, cashier_id, password):
        self.cashier_name = cashier_name
        self.cashier_id = cashier_id
        self.password = password
        self.cafeteria = ''

    def set_cafeteria(self, cafeteria):
        self.cafeteria = cafeteria
