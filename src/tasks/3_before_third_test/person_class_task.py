print()
from datetime import datetime, date

class Person:

    
    def __init__(self, first_name: str, last_name: str, birth_date: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
        
    def calculate_age(self) -> int:
        today = date.today()
        age = today.year - self.birth_date.year
        
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        
        return age
    
    
    def show_info(self) -> None:
        
        birth_date_str = self.birth_date.strftime("%A %d %B %Y")
        
        print(f"First Name: {self.first_name:^10} | Last Name: {self.last_name:^10} | Age: {self.calculate_age():^10} | Birth Date: {birth_date_str:^10}", end=" | ")
        
class Student(Person):
    
    
    def __init__(self, first_name: str, last_name: str, birth_date: str) -> None:
        super().__init__(first_name, last_name, birth_date)
        

    def find_class_year(self) -> str:
        age = self.calculate_age()
        
        if age == 16:
            return "VG1"
        
        elif age == 17:
            return "VG2"
        
        elif age == 18:
            return "VG3"
        
        else:
            return "Unknown"


    def show_info(self) -> None:
        super().show_info()
        print(f"Class Year: {self.find_class_year()}")


class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, birth_date: str, primary_class: str = "", subjects: list | None = None) -> None:
        super().__init__(first_name, last_name, birth_date)
        
        self.primary_class = primary_class
        self.subjects = subjects if subjects is not None else []
    
    def find_specific_subject(self, subject: str) -> bool:
        return subject in self.subjects
    
    def show_info(self) -> None:
        super().show_info()
        print(f"Teachers Subject: {self.subjects} | Primary Class: {self.primary_class}")



# Test-Cases


# p1 = Person("Jimmy", "Devold", "07-01-2008") 
# p2 = Person("Max", "Timmy", "03-12-2030")
# p3 = Person("Jimmy", "Newtron", "11-04-1955")

# person_list = [p1, p2, p3]

# for person in person_list:
#     person.show_info()


# s1 = Student("Ola", "Nordmann", "10-08-2008")
# s2 = Student("Kari", "Hansen", "10-08-2008")
# s3 = Student("Per", "Olsen", "10-08-2008")

# student_list = [s1, s2, s3]

# for student in student_list:
#     student.show_info()


# t1 = Teacher("Ola", "Nordmann", "10-08-2008", "2STB", ["Math", "English"])
# t2 = Teacher("Kari", "Hansen", "10-08-2008", "2STE", ["Math", "English"])
# t3 = Teacher("Per", "Olsen", "10-08-2008", "2STA", ["Math", "English"])

# teacher_list = [t1, t2, t3]

# for teacher in teacher_list:
#     teacher.show_info()


