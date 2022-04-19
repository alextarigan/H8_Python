# file = open('Hack8_Sample_Text.txt')
# file.close()

# print('File selesai dibuka')

# try:
#    f = open("Hack8_Sample_Text_zzz.txt", encoding = 'utf-8')
#    # perform file operations
# except FileNotFoundError:
#     print('File tidak ada')
# finally:
# #    f.close()
#     print('Already tried')

#membuat dan menulis file
# with open("sample.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")
#    f.write("AlexTarigan")

# f = open("sample.txt",'r',encoding = 'utf-8')
# print(f.read(4)) # read the first 4 data
# print(f.read(4)) # read the first 4 data
# print(f.tell()) # get the current file position
# print(f.read())   # read in the rest till end of file
# print("\nSetelah direset\n")
# f.seek(0)   # bring file cursor to initial position 
# print(f.tell()) # get the current file position
# print(f.read())  # read the entire file
# print(f.readline()) #membaca setiap 1 baris

# read the entire file using .read():
# with open('sample.txt', 'r') as reader:
#      # Read & print the entire file
#      print(reader.read())



