#calling function
from unittest import result


def printme(str):
    "This prints a passed string into this function"
    print(str)
    return;

# #Memanggil function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")



#Function Arguments
#memanggil function menggunakan tipe:
# ●Required arguments
# ●Keyword arguments
# ●Default arguments
# ●Variable-length arguments


#Required arguments
#maka akan mereturn error, karena tidak ada argument
# printme()

#Keyword Argument
# printme(str = "Hacktiv8")

#Default arguments
# def printInfo(name,age = 26):
#     "This prints a passed info into this function"
#     print("Name : ",name)
#     print("Age : ",age)
#     return;
# printInfo(age = 50, name="Hacktiv8")
# printInfo(name="Hacktiv8")

# def function_name( parameters ):
#    '''docstring'''
#    statement(s)

# Example of Function Creation

# def my_function(p, l):
#     '''Function to calculate area of a square'''
#     print(p * l)


# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# Function definition is here
# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")

# Function definition is here
# def changeme( mylist ):
#    '''This changes a passed list into this function'''
#    mylist = mylist+[1,2,3,4]
#    print("\nValues inside the function : ", mylist)
#    return mylist

# # Now you can call changeme function
# mylist = [10,20,30]
# print("\nValues outside the function - before : ", mylist)
# mylist = changeme( mylist )
# print("\nValues outside the function - after  : ", mylist)

# Function definition is here
# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)
 
# # Now you can call printme function
# printme("Hello")

# # # This syntax will give you an error
# # printme()

# Function definition is here
# def calculate_rect(length, width):
#   '''This function is used to calculate area of rectangle'''
#   print('Area : ', length*width)

# # Define parameters
# length = 100
# width = 20

# # Call calculate_rect
# calculate_rect(length, width)

# # # This syntax will give you an error
# # calculate_rect(length)

#Default arguments
# def printInfo(name,age = 26):
#     "This prints a passed info into this function"
#     print("Name : ",name)
#     print("Age : ",age)
#     return;
# printInfo(age = 50, name="Hacktiv8")
# printInfo(name="Hacktiv8")

# def printInfo(name, *pets):
#     pass

# def print_pets(name, *pets):
#     pass

# print_pets('andy','cats')
# print_pets('andy','cats','dogs','rabbits')

# Function definition is here
# def print_pets( name, *pets ):
# # def printinfo(name, arg2, arg3, arg4):
# # '''This prints a variable passed arguments'''
#     print('name     : ', name)
#     print('pets : ', pets)

#     for pet in pets:
#       print('isi pets : ', pet) 
    
#     print('')

# # Now you can call printinfo function
# print_pets('andy','cats')
# print_pets('andy','cats','dogs','rabbits')
# print_pets('andy')

#Variable-length Argument 
# def print_bought_items( name, **bought_items ):
# # def printinfo(name, arg2, arg3, arg4):
# # '''This prints a variable passed arguments'''
#     print('name     : ', name)

#     for key,value in bought_items.items():
#       print('key : ', key) 
#       print('value : ', value) 
    
#     print('')
# print_bought_items('Ani', first="egg",second="sugar",third="salt",fourth="baking powder")
# print_bought_items('Ali', first="thread",second="hoop",third="neddle")
# print_bought_items('Cici',fruit='Apple',milk="oatmilk")


#Anonymous Function
# Function definition is here
# sum = lambda arg1, arg2: arg1 + arg2

# # That lambda function will be equal to :
# # def sum(arg1, arg2):
# #     return arg1+arg2

# # Now you can call sum as a function
# print("Value of total : ", sum( 10, 20 ))
# print("Value of total : ", sum( 20, 20 ))

# multiply = lambda x, y: x * y
# print(multiply(3,4))

# def sum(arg1,arg2):
#     total = arg1+arg2
#     total2 = total + arg1
#     return total,total2

# # result = sum(10,20)
# # print("Result function : ", result)
# # print(type(result))

# x,y = sum(10,20)
# print("result ",x,y)

# Declare a global variable
# total = 0

# # Create sum function
# def sum( arg1, arg2 ):
#    total = arg1 + arg2; 
#    print("Inside the function local total   : ", total)

# # Call a function
# total = sum( 10, 20 )
# print("Outside the function global total : ", total)

# Example of docstring in a function

def sum_number(num1, num2):
  '''
  This function is used to sum of 2 variables.
  :param num1: Input number 1 | int or float
  :param num2: Input number 2 | int or float
  
  :return: num3: Sum of number | int or float
  '''

  num3 = num1 + num2
  return num3

print(sum_number(1,23))
#Return isi docstring
print(sum_number.__doc__)
#return attribut 
print(dir(sum_number))