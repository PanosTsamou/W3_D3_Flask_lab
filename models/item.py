class Item:
    
    def __init__(self, input_name, input_brand, input_availability, input_type, input_kinds, input_price):
        self.name =input_name
        self.brand = input_brand
        self.availability = input_availability
        self.type = input_type
        self.kind = input_kinds
        self.price = input_price
        self.description = ""



    def add_description(self, description):
        self.description = description


