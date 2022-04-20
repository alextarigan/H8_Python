#Contoh penggunaan Class Child

class Dog:
    # class attribute
    species = "Canis familiaris"
    fav_meal = "Brand meal 2022"
 
    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed
    def __init__(self, name, age):
        # instance attribute
        self.name = name
        self.age = age
 
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"    
        #return self.name + ' is ' + str(self.age) + ' years old'

    # instance method
    def speak(self,sound):
        return f"{self.name} says {sound}"
        #return self.name + ' says ' + sound
    

class JackRussellTerrier(Dog):
    #child class dari dog class
    # pass
    def speak(self,sound="Arf"):
        return f"{self.name} says {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

# Instatiating new instance of Dog class
# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# instatiating new instance of [breed] class
# instatiating new instance pf JackRusselTerrier class
miles = JackRussellTerrier('Miles',4)

buddy = Dachshund('Buddy',9)

# instatiating new instance
jack = Bulldog("Jack",3)
jim = Bulldog("Jim", 5)

# print(miles.name, miles.age, miles.breed)
# print(buddy.name, buddy.age, buddy.breed)
# print(jack.name, jack.age, jack.breed)
# print(jim.name, jim.age, jim.breed)
# print(buddy.speak("Yap"))
# print(jim.speak("Woof"))

# print(miles.name, miles.age)
# print(buddy.name, buddy.age)
# print(jack.name, jack.age)
# print(jim.name, jim.age)

# print(buddy.description())
# print(miles.description())
# print(jack.description())
# print(jim.description())

# print(buddy.species)
# print(miles.species)
# print(jack.species)
# print(jim.species)

# print(buddy.fav_meal)
# print(miles.fav_meal)
# print(jack.fav_meal)
# print(jim.fav_meal)

print(buddy.speak("Yap"))
print(jim.speak("woof"))
print(jack.speak("woof"))

print(miles.speak("before arf"))
print(miles.speak())
print(miles.speak("arf arf arf"))
print(miles.speak("Grrr"))