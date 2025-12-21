print()
import math as m

# 1a
class Polygon:
    
    def __init__(self, total_sides: int, length_list: list = []) -> None:
        self.total_sides = total_sides
        self.length_list = length_list
    
    def calculate_circumference(self) -> float:
        
        total_circumference: float = 0
        
        for sides in self.length_list:
            if self.total_sides >= 3 and len(self.length_list) == self.total_sides:
                total_circumference += sides
                
        return round(total_circumference, 2)
    
    def __str__(self) -> str:
        return f"Total sides: {self.total_sides} | Lengths: {self.length_list} | Circumference: {self.calculate_circumference()}"
    

# input_length_list: list = []
# input_total_sides: int = int(input("Enter total sides: "))

# for _ in range(0, input_total_sides):
#     input_length = float(input("Enter value for side: "))
#     input_length_list.append(input_length)
#     input_length = 0
    

# input_polygon = Polygon(input_total_sides, input_length_list)
# print(input_polygon)

#1b

# polygon_list: list = [Polygon(3, [1,2,3]), Polygon(4, [1,4,3,2]), Polygon(6, [1,5,3,9,3,2]), Polygon(5, [2,53,2,1,7])]

# for polygon in polygon_list:
#     print(polygon)


# 2abcd)

class Rectangle(Polygon):
    def __init__(self, width: float, height: float) -> None:
        super().__init__(4, [width, height, width, height])
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return round(self.width * self.height, 2)

    def __str__(self) -> str:
        return (f"Rectangle | Width: {self.width}, Height: {self.height} | " f"Area: {self.calculate_area()} | " f"Circumference: {self.calculate_circumference()}"
        )



# 2ef)

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def __str__(self) -> str:
        return (f"Square | Side: {self.width} | " f"Area: {self.calculate_area()} | " f"Circumference: {self.calculate_circumference()}")



# 2g)

# rectangle_list: list = [Rectangle(2, 4), Rectangle(3, 5), Rectangle(6, 1)]

# square_list: list = [Square(2), Square(4), Square(6), Square(8)]

# for rectangle in rectangle_list:
#     print(rectangle)

# print()

# for square in square_list:
#     print(square)


# 3acd)

class Triangle(Polygon):
    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__(3, [a, b, c])
        self.a = a
        self.b = b
        self.c = c
    
    
    def calculate_area(self) -> float:
        s = (self.calculate_circumference() / 2)
        area = m.sqrt(s*(s - self.a)*(s - self.b)*(s - self.c))
        return round(area, 2)
    
    def __str__(self) -> str:
        return (f"Total sides: {self.total_sides:^3}\n"
                f"Lengths: {self.length_list}\n"
                f"Circumference: {self.calculate_circumference():^3}\n"
                f"Area: {self.calculate_area():^3}\n")

# 3b)

triangle_list: list = [Triangle(4, 4.2, 5), Triangle(5, 5.6, 5.6), Triangle(4, 4, 4), Triangle(4, 6, 7), Triangle(3, 6.2, 6.2)]

for triangle in triangle_list:
    print(triangle)