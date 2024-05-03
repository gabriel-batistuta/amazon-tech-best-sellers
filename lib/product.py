from abc import ABC

class AbstractProduct(ABC):
    def __init__(self, name):
        self.name = name
        self.price = 0
        self.discount = 0
        self.tax = 0
        self.total_price = 0
