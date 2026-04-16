from datetime import date

class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(age: int) -> bool:
       return age >= 18
    
    @classmethod
    def from_birth_year(cls, name: str, birth_year: int) -> 'Person':
        current_year = date.today().year 
        return cls(name, current_year - birth_year)

# Example usage
alice = Person("Alice", 30)
print(f"{alice.name} is an adult: {Person.is_adult(alice.age)}")

bob = Person.from_birth_year("Bob", 1995)
print(f"{bob.name} is an adult: {Person.is_adult(bob.age)}")

kid = Person("Charlie", 10)
print(f"{kid.name} is an adult: {Person.is_adult(kid.age)}")