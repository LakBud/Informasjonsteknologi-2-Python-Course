class Player:
    
    _allowed_races: list[str] = ["Human", "Orc", "Elf", "Dwarf"]
    
    
    def __init__(self, player_ID: str, race: str, attack_power: int, profession: str, location: str = "Starter Village") -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param player_ID: Description
        :type player_ID: str
        :param race: Description
        :type race: str
        :param attack_power: Description
        :type attack_power: int
        :param profession: Description
        :type profession: str
        """
        
        
        if race not in self._allowed_races:
            raise ValueError("Invalid Race")
        else:
            self.race = race

        
        self.player_ID = player_ID
        self.attack_power = attack_power
        self.profession = profession 
        self.location = location
        self.alive = True
        self.side = None
        

    def attack(self, target: Player) -> None:
        
        """
        Docstring for attack
        
        :param self: Description
        :param target: Description
        :type target: Player
        """
        
        print()
        if not self.alive:
            print(f"{self.player_ID} is dead and cannot attack.")
            return
        if not target.alive:
            print(f"{target.player_ID} is already dead.")
            return

        print(f"{self.player_ID} attacks {target.player_ID}!")
        
        if self.attack_power > target.attack_power:
            target.alive = False
            print(f"{target.player_ID} has died!")
            
        elif self.attack_power == target.attack_power:
            self.alive = False
            target.alive = False
            print(f"Both {self.player_ID} and {target.player_ID} have died!")
            
        else:
            self.alive = False
            print(f"{self.player_ID} has died!")
        
    def __str__(self) -> str:
        player_status = "alive" if self.alive else "dead"
        return (
        f"Player ID: {self.player_ID:^10} | "
        f"Race: {self.race:^10} | "
        f"Profession: {self.profession:^10} | "
        f"Side: {self.side:^10} | "
        f"Attack Power: {self.attack_power:^4} | "
        f"Status: {player_status:^5} | "
        f"Location: {self.location:^15}"
        )

        

class EvilPlayer(Player):
    
    _allowed_professions: list[str] = ["Knight", "Wizard", "Archer", "Barbarian"]
    
    def __init__(self, player_ID: str, race: str, attack_power: int, profession: str, location: str = "Starter Village") -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param player_ID: Description
        :type player_ID: str
        :param race: Description
        :type race: str
        :param attack_power: Description
        :type attack_power: int
        :param profession: Description
        :type profession: str
        """
        
        super().__init__(player_ID, race, attack_power, profession, location)
        
        if profession not in self._allowed_professions:
            raise ValueError("Invalid Profession")
        
        self.side = "Evil"

class GoodPlayer(Player):
    
    _allowed_professions: list[str] = ["Knight", "Wizard", "Archer", "Palladin"]
    
    def __init__(self, player_ID: str, race: str, attack_power: int, profession: str, location: str = "Starter Village") -> None:
        
        """
        Docstring for __init__
        
        :param self: Description
        :param player_ID: Description
        :type player_ID: str
        :param race: Description
        :type race: str
        :param attack_power: Description
        :type attack_power: int
        :param profession: Description
        :type profession: str
        """
        
        super().__init__(player_ID, race, attack_power, profession, location)
        
        if profession not in self._allowed_professions:
            raise ValueError("Invalid Profession")
        
        self.side = "Good"


class Game:
    def __init__(self) -> None:
        self._player_server: list = []
    
    
    def add_players(self, new_players: list[Player]) -> None:
        
        """
        Docstring for add_players
        
        :param self: Description
        :param new_players: Description
        :type new_players: list[Player]
        """
        
        self._player_server.extend(new_players)
    
    def find_player(self, selected_id: str) -> None:
        
        """
        Docstring for find_player
        
        :param self: Description
        :param selected_id: Description
        :type selected_id: str
        """
        
        print()
        for person in self._player_server:
            if selected_id in person.player_ID:
                print(person)
    
    def show_evil_players(self) -> None:
        print()
        print("All evil players:")
        total_evil: int = 0
        for person in self._player_server:
            if person.side == "Evil":
                total_evil += 1
                print(person)
        print()
        print(f"Total Amount of Evil Players: {total_evil}")
    
    def show_good_players(self) -> None:
        print()
        print("All good players:")
        total_good: int = 0
        for person in self._player_server:
            if person.side == "Good":
                total_good += 1
                print(person)
        print()
        print(f"Total Amount of Good Players: {total_good}")
                
    def show_server(self) -> None:
        print()
        print("Server:")
        for person in self._player_server:
            print(person)

# Test-Case

game = Game()

# robot = Player("Robot", "Human", 20, "Archer")
alice = GoodPlayer("Alice", "Human", 50, "Palladin")
bob = EvilPlayer("Bob", "Orc", 45, "Barbarian")

game.add_players([alice, bob])


game.show_good_players()
game.show_evil_players()
game.show_server()

alice.attack(bob)
bob.attack(alice)
