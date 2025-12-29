print()
import random as rnd

class Dice:
    def __init__(self, total_sides: int = 0) -> None:
        self.total_sides = total_sides
        
    def dice_roll(self) -> int:
        return rnd.randint(1, self.total_sides)
    
    def show_info(self) -> None:
        print(f"Total sides: From 1 to {self.total_sides} | Thrown Number: {self.dice_roll()}")


class Cheating_Dice(Dice):
    def __init__(self, total_sides: int) -> None:
        super().__init__(total_sides)
        self.highest_throw = 0
        
        
    def calculate_highest_throw(self) -> None:
        
        total_throw: int = int(input("How many throws do you want to do: "))
        
        for _ in range(total_throw):
            diced_throw = super().dice_roll()
            if diced_throw > self.highest_throw:
                self.highest_throw: int = diced_throw

    
    def show_info(self) -> None:
        print(f"Highest throw: {self.highest_throw}")
    


# * 5, 3, 4, 3, 4, 5, 6, 1, 1, 1
# dice_6 = Dice(6).dice_roll()
# print(dice_6)

# * 20, 8, 15, 4, 7, 11, 6, 6, 14, 7
# dice_20 = Dice(20).dice_roll()
# print(dice_20)

# for i in range(12):
#     Dice(14).show_info()


user_input = int(input("How many sides of the dice do you want to get the highest throw: "))

dice = Cheating_Dice(user_input)
dice.calculate_highest_throw()
dice.show_info()
