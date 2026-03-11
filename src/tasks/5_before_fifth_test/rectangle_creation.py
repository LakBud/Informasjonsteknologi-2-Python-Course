class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    
    def calculate_area(self) -> float:
        return self._width * self._height


with open("data/5/rectangle_data.csv", encoding="utf-8") as file:
    for line in file:
        l = line.strip("\n").split(",")
        
        rectangle = Rectangle(int(l[0]), int(l[1]))
        print(rectangle.calculate_area())



