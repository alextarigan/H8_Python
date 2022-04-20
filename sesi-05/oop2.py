# def dog_speak(self, sound):
#     pass
# def cat_speak(self, sound):
#     pass
# def dog_description(self):
#     pass
# def cat_description(self):
#     pass
# class Dog:
#     #class attribute
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#         #kiri -> attribute yang ada di class, 
#         # ((pada instance tertentu yang ditandai dengan self)
#         #kanan -> nilai yang di assign untuk
#         self.name = name
#         self.age = age
class Dog:
    species = "Canis familiaris"
 
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"    
        #return self.name + ' is ' + str(self.age) + ' years old'
    
    def speak(self,sound):
        return f"{self.name} says {sound}"
        #return self.name + ' says ' + sound

#instantiating
# dog1 = Dog('Miles',2)
# dog2 = Dog('Abby',2)
# print(dog1.name, dog1.age, dog1.species)
# print(dog2.name, dog2.age, dog2.species)

# dog3 = Dog()
# print(dog3.species)

# buddy = Dog('Buddy', 9)

# miles = Dog('Miles',4)
# print(buddy.name)
# print(miles.name)

# print(buddy.age)
# print(miles.age)

# print(buddy.species)
# print(miles.species)
 
dog1 = Dog('miles', 2)
dog2 = Dog('abby', 1)
dog3 = Dog('', '')
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)
description_of_buddy = buddy.description()
print(description_of_buddy)
#or
print(buddy.description())
 
print(dog1.description())
print(dog2.description())

sound_of_buddy = buddy.speak('woof woof')
print(sound_of_buddy)

print(miles.speak("boow boow"))