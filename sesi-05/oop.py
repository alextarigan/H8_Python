def nama_fungsi (parameter):
    pass

class Dog:
    #pass
    def __init__(self, name, age):
        #kiri -> attribute yang ada di class, 
        # ((pada instance tertentu yang ditandai dengan self)
        #kanan -> nilai yang di assign untuk
        self.name = name
        self.age = age

#instantiating
dog1 = Dog('Miles',2)
dog2 = Dog('Abby',2)
print('aman')