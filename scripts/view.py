from car import Car

vehicle_1 = Car("Toyota", "Corolla", 1999)
vehicle_2 = Car.from_vin("Po9091823")

print(vehicle_1.get_info(), vehicle_2.get_info())
print(vehicle_1.is_valid_year(vehicle_1.year), vehicle_2.is_valid_year(vehicle_2.year))


