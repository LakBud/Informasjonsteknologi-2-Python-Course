print()
# ? A classvariable is a variable which is common for all objects of the class.
# * Every object of the class can change the variable

# ? A private variable is a variable which is only available within a class it belongs and shouldnt be manipulated outside the class.
# * Private variables starts with an underscore in the start: _variable

class Member:
    
    """
    Docstring for Member
    
    ? Class_and_Private_Variables:
    - _club_name (str)
    - _member_number (int)
    """
    
    _club_name: str = "Avengers"
    _member_number: int = 0
    
    def __init__(self, member_name: str):
        self._name = member_name
        
        """
        * Updates the class_variable _member_number and sets the objects _member_number to this
        """
        Member._member_number += 1
        self._m_nr = Member._member_number
        
        
    def show_name(self):
        return self._name
    
    
    
    def __repr__(self): # ? The same as __str__(), however it serves more like a message to devs. It will only run with a __str__() if that method doesnt work.
        return f"ERROR HAPPENED"
    
        
    def __str__(self): # ? __str__() is a method which replaces show_info funcs. Makes it so when someone prints a object, it will find this function and run it.
        return f"Member Number: {self._m_nr} | Name: {self._name} - Member of {Member._club_name}"
    
    

Johnny = Member("Johnny")
Peter = Member("Peter")

print(Johnny)
print(Peter)
