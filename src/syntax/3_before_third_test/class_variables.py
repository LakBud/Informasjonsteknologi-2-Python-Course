print()
# ? A classvariable is a variable which is common for all objects of the class.
# * Every object of the class can change the variable

class Member:
    
    """
    Docstring for Member
    
    ? Class_Variables:
    - club_name (str)
    - member_number (int)
    """
    
    club_name: str = "Avengers"
    member_number: int = 0
    
    def __init__(self, member_name: str):
        self.name = member_name
        
        """
        * Updates the class_variable member_number and sets the objects member_number to this
        """
        Member.member_number += 1
        self.m_nr = Member.member_number
        
    def show_info(self):
        print(f"Member Number: {self.m_nr} | Name: {self.name} - Member of {Member.club_name}")
    

Johnny = Member("Johnny")
Peter = Member("Peter")

Johnny.show_info()
Peter.show_info()
