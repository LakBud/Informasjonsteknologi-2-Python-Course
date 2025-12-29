from typing import List

# 1
class Car:
    def __init__(self, brand: str, model: str, year: int, km_state: float = 0.0) -> None:
        self._brand = brand
        self._model = model
        self._year = year
        self._km_state = km_state
    
    def drive(self, km_driven: float) -> None:
        if km_driven >= 0:
            self._km_state += km_driven 
        else:
            print("Total driven kilometers has to be higher then 0")
    
    
    def __str__(self) -> str:
        return f"Brand: {self._brand} | Model: {self._model} | Year: {self._year} | Kilometer State: {self._km_state}"

# 3
class Electric_car(Car):
    def __init__(self, brand: str, model: str, year: int, battery_capacity: float, battery_level: float, consumption: float, km_state: float = 0.0) -> None:
        super().__init__(brand, model, year, km_state)
        self._battery_capacity = battery_capacity
        self._battery_level = battery_level
        self._consumption = consumption
    
    
    def charge(self) -> None:
        self._battery_level = self._battery_capacity
    
    def drive(self, km_driven: float) -> None:
        super().drive(km_driven)
        self._battery_level -= km_driven * self._consumption
    
    
    def __str__(self) -> str:
        return f"Brand: {self._brand} | Model: {self._model} | Year: {self._year} | Kilometer State: {self._km_state} | Battery Level: {self._battery_level}"



class Fossil_car(Car):
    def __init__(self, brand: str, model: str, year: int, km_state: float, tank_volume: float, fuel_level: float, consumption: float) -> None:
        super().__init__(brand, model, year, km_state)
        self._tank_volume = tank_volume
        self._fuel_level = fuel_level
        self._consumption = consumption
        
        
    def drive(self, km_driven: float) -> None:
        super().drive(km_driven)
        self._fuel_level -= km_driven * self._consumption
    
    def fuel_tank(self) -> None:
        self._fuel_level = self._tank_volume
    
    def __str__(self) -> str:
        return f"Brand: {self._brand} | Model: {self._model} | Year: {self._year} | Kilometer State: {self._km_state} | Fuel Level: {self._fuel_level}"


# 5
class Customer:
    def __init__(self, name: str, cars: list[Car] | None = None) -> None:
        self._name = name
        self._cars = cars if cars is not None else []
    
    
    def buy_car(self, new_cars: list[Car] | None = None) -> None:
        if new_cars is not None:
            self._cars.extend(new_cars)
    
    def __str__(self) -> str:
        cars_list = ", ".join(str(car) for car in self._cars)
        return f"Name: {self._name} | Cars: {cars_list}"





class Car_Retailer:
    def __init__(self, name: str, car_storage: list[Car] | None = None) -> None:
        self._name = name
        self._car_storage = car_storage if car_storage is not None else []
    
    def add_car(self, new_car: Car | None = None) -> None:
        if new_car is not None:
            self._cars.append(new_car)
    
    def sell_car(self, selected_car: Car, customer: Customer) -> None:
        if selected_car in self._car_storage:
            self._cars.remove(selected_car)
            customer.buy_car([selected_car])
    
    def __str__(self) -> str:
        cars_list = ", ".join(str(car) for car in self._car_storage)
        return f"Name: {self._name} | Car Storage: {cars_list}"
