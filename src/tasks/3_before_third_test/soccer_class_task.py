class Soccer_club:
    def __init__(self, player_list: list[Player] | None = None) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param player_list: Description
        :type player_list: list[Player] | None
        """
        
        self._player_list = player_list if player_list is not None else []
    
    
    def add_soccer_players(self, new_players: list[Player] | None = None) -> None:
        
        """
        Docstring for add_soccer_players
        
        :param self: Description
        :param new_players: Description
        :type new_players: list[Player] | None
        """
        
        if new_players is not None:
            self._player_list.extend(new_players)
    
    def compute_average_age(self) -> float:
        
        """
        Docstring for compute_average_age
        
        :param self: Description
        :return: Description
        :rtype: float
        """
        
        if not self._player_list:
            return 0.0
        
        age_list: list[int] = []
        
        for player in self._player_list:
            age_list.append(player.age)
        
        return round(sum(age_list) / len(age_list), 2)
    
    def show_club_info(self) -> None:
        
        """
        Docstring for show_club_info
        
        :param self: Description
        """
        
        print(f"Soccer Players within the Club:")
        for player in self._player_list:
            player.show_info()
        print()
        
        print(f"Average Age: {self.compute_average_age()}")

class Player:
    def __init__(self, name: str, age: int, positions: list[str] | None = None) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :type name: str
        :param age: Description
        :type age: int
        :param positions: Description
        :type positions: list[str] | None
        """
        
        self.name = name
        self.age = age
        self.positions = positions if positions is not None else []
    
    def show_info(self) -> None:
        print(f"Name: {self.name} | Age: {self.age} | Possible Positions: {self.positions}")

class Forward(Player):
    def __init__(self, name: str, age: int, positions: list[str] | None = None, goals: int = 0) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :type name: str
        :param age: Description
        :type age: int
        :param positions: Description
        :type positions: list[str] | None
        :param goals: Description
        :type goals: int
        """
        
        super().__init__(name, age, positions)
        self._goals = goals
    
    def show_info(self) -> None:
        super().show_info()
        print(f"| Goals: {self._goals}")
        
        
class Midfielder(Player):
    def __init__(self, name: str, age: int, positions: list[str] | None = None, passes: int = 0) -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :type name: str
        :param age: Description
        :type age: int
        :param positions: Description
        :type positions: list[str] | None
        :param passes: Description
        :type passes: int
        """
        
        super().__init__(name, age, positions)
        self._passes = passes
    
    def show_info(self) -> None:
        super().show_info()
        print(f"| Passes: {self._passes}")

class Defender(Player):
    def __init__(self, name: str, age: int, positions: list[str] | None = None, blocks: int = 0):
        
        """
        Docstring for __init__
        
        :param self: Description
        :param name: Description
        :type name: str
        :param age: Description
        :type age: int
        :param positions: Description
        :type positions: list[str] | None
        :param blocks: Description
        :type blocks: int
        """
        
        super().__init__(name, age, positions)
        self._blocks = blocks
    
    def show_info(self) -> None:
        super().show_info()
        print(f"| Blocks: {self._blocks}")