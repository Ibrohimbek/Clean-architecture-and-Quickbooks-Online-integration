class InvoiceLine:

    def __init__(self, description: str, net_value: int):
        self.description = description
        self.net_value = net_value

    def validate(self):
        pass