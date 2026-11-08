class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_info(self):
        return f"Make: {self.make}, Model:  {self.model}, Year:  {self.year}"

    @classmethod
    def from_vin(cls, vin):
        return Car("Ford", "Bronko", 2022)

    @staticmethod
    def is_valid_year(year):
        return year >= 1980


