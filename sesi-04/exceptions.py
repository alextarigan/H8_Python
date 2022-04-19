# Raise Exceptio
# x = 10
# if x > 5:
#     # raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
#     raise Exception('x tidak boleh melebihi 5. Nilai x yang di input adalah : {}'.format(x))
#     # raise Exception('x tidak boleh melebihi 5. Nilai x yang di input adalah : {}{}'.format(x,y))


# AssertionError Exception
#import sys
#assert ('win' in sys.platform), "This code runs on Windows only."

#The try and except Block: Handling Exceptions
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Tidak bisa membuka file.log')

# import sys
# assert ('linux' in sys.platform), "Function can only run on Linux systems."
# assert ('win' in sys.platform), "This code runs on Windows only."
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except:
#     print('Skip')
#     print('Linux Function was not executed')
#     pass


#menampilkan error menggunakan AssertionError
# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')

# Here’s another example where you open a file and use a built-in exception:

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')
# print(189,334, 'Asal ngeprint')

# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

# try except except
# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('os_interaction() function was not executed')


#try except else
# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause.')


# import sys
# def os_interaction():
#     # assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('sample.txt') as file:
#             read_data = file.read()
#             print(read_data)
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)


# try except else finally
import sys
def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('win' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# Have a look at the following example:

try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')