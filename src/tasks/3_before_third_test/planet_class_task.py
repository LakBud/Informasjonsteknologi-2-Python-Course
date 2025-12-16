print()
import math as m

class Planet:
    
    def __init__(self, name: str, diameter: float, distance_from_sun: float, moon_list: list = []) -> None:

        self.name = name
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.total_moons = len(moon_list)
        self.moon_list = moon_list
        
    def calculate_planet_volume(self) -> float:
        
        radius = self.diameter / 2
        return round(4/3 * m.pi * radius**3, 2)
    
    def calculate_surface_area(self) -> float:
        
        radius = self.diameter / 2
        return round(4 * m.pi * radius**2, 2)
    
    def __str__(self) -> None:
        
        print()
        print(f"Planet Name:         | {self.name:^25}")
        print(f"Planet Diameter:     | {self.diameter:^25} km")
        print(f"Distance from Sun:   | {self.distance_from_sun:^25} million km")
        print(f"Total Moons:         | {self.total_moons:^25} Moons")
        print(f"Planet Volume:       | {self.calculate_planet_volume():^25} km^3")
        print(f"Planet Surface Area: | {self.calculate_surface_area():^25} km^2")
        
        print()
        print(f"{self.name} Moons:")
        print("-" * 80)
        
        if self.moon_list:
            
            for moon in self.moon_list:
                print(f"Moon Name: {moon.name}")
                print(f"Moon Volume: {moon.calculate_moon_volume()} km^3")
                print(f"Earth-Volume Ratio: {round(moon.calculate_moon_volume() / self.calculate_planet_volume(), 2)} km^3")
                print()
                
        else:
            print("This Planet has no Moons")


class Moon:
    
    def __init__(self, name: str, moon_diameter: float) -> None:
        self.name = name
        self.moon_diameter = moon_diameter
        
    def calculate_moon_volume(self) -> float:
        radius = self.moon_diameter / 2
        return round(4/3 * m.pi * radius**3, 2)

planets: dict = {
    "Mercury": Planet("Mercury", 4879, 579.9),
    "Venus": Planet("Venus", 12104, 108.21),
    "Earth": Planet("Earth", 12742, 149.60, [Moon("Luna", 3476)]),
    "Mars": Planet("Mars", 6779, 227.923, [Moon("Phobos", 24), Moon("Deimos", 8)]),
    "Jupiter": Planet("Jupiter", 139822, 778.570),
    "Saturn": Planet("Saturn", 120536, 1433.530),
    "Uranus": Planet("Uranus", 50724, 2872.460),
    "Neptune": Planet("Neptune", 49244, 4495.06)
}


try:
    choose_planet = str(input("Enter a planet in the solar system for details: ")).capitalize()
    
    if choose_planet in planets:
        print(planets[choose_planet])
    else:
        print("\nINVALID NAME!")

except Exception as e:
    print("\nERROR OCCURRED!")
    print(f"System message: {e}")
