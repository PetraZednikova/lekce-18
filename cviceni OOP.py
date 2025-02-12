class Pet:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def make_sound(self):
        return "Some sound"

    def get_name(self):
        return self.name

    def get_type(self):
        return self.typ

    def info(self):
        return f"{self.get_name()} je {self.get_type()}."


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name, "kočka")

    def make_sound(self):
        return "Mňau"


class Dog(Pet):
    _dog_count = 0  # Tato proměnná se sdílí mezi všemi instancemi Dog

    def __init__(self, name):
        super().__init__(name, "pes")
        Dog._dog_count += 1  # Počet psů se zvětší při každém vytvoření psa

    def make_sound(self):
        return "Hafhaf"

    @staticmethod
    def get_dog_count():
        return Dog._dog_count  # Opraveno: Neprovádíme `print()` přímo v metodě


class Parrot(Pet):
    def __init__(self, name):
        super().__init__(name, "papoušek")

    def make_sound(self):
        return "Pipip"


class Hamster(Pet):
    def __init__(self, name):
        super().__init__(name, "křeček")

    def make_sound(self):
        return "Skvík skvík"


# Seznam domácích mazlíčků
Pets = [
    Cat("Micka"),
    Dog("Azor"),
    Parrot("Pepík"),
    Hamster("Pista"),
    Dog("Lajka"),
    Dog("Béda"),
    Dog("Hafík"),
]

# Výpis informací o mazlíčcích
for pet in Pets:
    print(pet.info())
    print("Dělá:", pet.make_sound())
    print("-" * 20)

# Výpis počtu psů
print(f"Počet vytvořených psů: {Dog.get_dog_count()}")
