# A Python script (person.py) with a Person class, including age calculation. 
from datetime import datetime
class Person:
    def __init__(self,name: str,year_of_birth: int):
        self.name = name
        self.year_of_birth = year_of_birth
    def calculate_age(self, current_year: int = None) -> int:
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self.year_of_birth
    
if __name__== "__main__":
    p = Person("Minh",2000)
    print(f"{p.name} is {p.calculate_age(2013)} years old.")