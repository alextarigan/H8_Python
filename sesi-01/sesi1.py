# Integers
print(type(10))
print(12312321312312312312321 + 1)
print(10)


# Floating numbers
print(type(4.2))
print(4.2)
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)


#strings
print(type("Hacktiv8"))
print("Hacktiv8")
print("this string contains a single quote (') character.")
print('this string contains a single quote (") character.')

#Boolean
print(type(True))
print(type(False))
print(100 > 200)
print(100 == 200)
print(100 < 200)

#Variable Assignment
n = 300
print(n)
#chained assignment
a = b = c =300
print(a,b,c)

#variable names
#PascalCase
#camelCase
#snake_case
name = "Hacktiv8"
Age = 54
has_laptops = True
print(name,Age,has_laptops)

#Operators and Expressions
a=10
b=20
print(a+b)
print(a+b-5)

#Aritmetic Operators
a = 4
b = 3
print(a+b)
print(a-b)
print(a * b)
print(a/b)
print(a %b)
print(a ** b)

#Comparison Operators
a = 10
b = 20

print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

#String Manipulation
s = 'foo'
t = 'bar'
# + and * operators
print(s + t)
print(s * 4)
#Case Conversion
print(s.capitalize())
print(s.lower())  
print(s.swapcase())

#Python Lists
#List didefinisikan dalam Python dengan melampirkan urutan objek yang dipisahkan koma 
# dalam tanda kurung siku ([])
#List are Ordered
#List can contain any arbitrary objects
#List elements can be accessed by index
#List can be nested to arbitrary depth
#List are mutable
#List are dynamic
#nilai tunggal dalam list dapat diganti dengan pengindeksan dan assignment sederhana
a= ['foo','bar','baz','qux']
print(a)
a= ['foo','bar','baz','qux','quux','corge']
a[2] = 10
a[-1] = 20
print(a)
a= ['foo','bar','baz','qux','quux','corge']
print(a[1:4])
a[1:4] = [1.1,2.2,3.3,4.4,5.5]
print(a)

#Python Tuples
# Tuple didefinisikan dengan melampirkan elemen dalam tanda kurung (())
# bukan tanda kurung siku ([]). Tuple tidak dapat diubah.
tuples = ('foo','bar','baz','qux','quux','corge')
print(tuples)
print(tuples[0])
print(tuples[-1])
#packing and unpacking
(s1,s2,s3,s4) = ('foo','bar','baz','qux')
print(s1)

#Python Dictionary
#dictionary dan list memiliki karakteristik berikut:
# ●Keduanya dapat berubah.
# ●Keduanya dinamis.
 
# Mereka dapat tumbuh dan menyusut sesuai kebutuhan.
# ●Keduanya dapat disarangkan. 
# Sebuahlist dapat berisi list lain. 
# dictionary dapat berisi dictionary lain. 
# dictionary juga dapat berisi list, dan sebaliknya. 

# dictionary berbeda dari list terutama dalam cara elemen diakses:
# ●Elemen list diakses berdasarkan posisinya dalam list, melalui pengindeksan.
# ●Elemen dictionary diakses melalui kunci
MLB_Team = {
    'Colorado':'Rockies',
    'Boston':'Red Sox',
    'Minnesota':'Twins'
}
print(MLB_Team['Minnesota'])
#Menambahkan data ke dictionary
MLB_Team['Kansas City'] = 'Royals'
MLB_Team

#Dictionary kosong
person = {}
person['name'] = 'AlexTarigan'
person['age'] = 23
person['pets'] = {'dog':'Fido','cat':'Sox'}
print(person)
print(person['pets']['dog'])

#menghapus key di dictionary
#del person['pets']['dog']
#print(person)