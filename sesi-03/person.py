name = 'zack kambaew'
devices = ['laptop', 'smartphone', 'tablet']

def display(arg):
    #f -> untuk menyisipkan langsung variabel
    print(f'arg = {arg}')
    #atau
    #print('arg'+arg)

#agar saat di import tidak cetak
if (__name__ == '__main__'): #selection name
  print('Executing as standalone script')
  print(name)
  print(devices)
  print(display('Good Morning'))
