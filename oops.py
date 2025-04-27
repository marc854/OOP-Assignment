
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.__strength_level = strength_level 

    def display_info(self):
        print(f"Superhero: {self.name}")
        print(f"Special Power: {self.power}")
        print(f"Strength Level: {self.__strength_level}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def get_strength_level(self):
        return self.__strength_level

    def boost_strength(self, amount):
        self.__strength_level += amount
        print(f"{self.name}'s strength increased to {self.__strength_level}!")

# Subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flying_speed):
        super().__init__(name, power, strength_level)
        self.flying_speed = flying_speed  # New attribute for flying heroes

    # Polymorphism: override use_power
    def use_power(self):
        print(f"{self.name} soars through the sky with {self.power} at {self.flying_speed} km/h!")

    def fly(self):
        print(f"{self.name} is flying at {self.flying_speed} km/h!")

# Example usage
hero1 = Superhero("ShadowBlade", "Invisibility", 80)
hero2 = FlyingSuperhero("SkyBolt", "Thunder Flight", 90, 300)

hero1.display_info()
hero1.use_power()
hero1.boost_strength(10)

print()

hero2.display_info()
hero2.use_power()
hero2.fly()
