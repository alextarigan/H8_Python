
numbers = [
  951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 
  725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 
  219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 
  907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
  399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
  626, 949
  ]

print('Menggunakan For Loop')
for angka in numbers:
    if angka == 918:
        print(angka if angka % 2 == 0 else '')
        # if angka % 2 == 0:
        #     print(angka)
        break
    elif angka %  2 == 0:
        print(angka)
    else:
      continue
print('Done')

print('\nMenggunakan While Loop')
items = 0
while items < len(numbers):
  items += 1
  if numbers[items] == 918:
    if numbers[items] % 2 == 0:
      print(numbers[items])
    break
  if numbers[items] % 2 == 0:
    print(numbers[items])
  else:
    continue
print('Done')


