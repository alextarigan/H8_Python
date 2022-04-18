# n = 5
# while n > 0:
#     n -= 1
#     print(n)

# i = 1
# while i < 6:
#     print(i)
#     i += 1 
# print('abcdef')

#break
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print('Loop ended.')

# Continue
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print('Loop ended.')

#while else
# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Loop done.')

#while break else
#keyword = 'ab'
# keyword = 'aj'
# fruits = ['aa','ab','ac','ad','ae','af']
# n = 0
# while n < len(fruits):
#     if keyword in fruits[n]:
#         print('Found in index', n)
#         break
#     n+=1
# else:
#     print('could not be Found in any index')
#     print('Loop done.')

#infinite loop
# while True:
#     print('foo')

# age = 80
# gender = 'F'
# if age < 18:
#     if gender == 'M':
#         print('son')
#     else:
#         print('daughter')
# elif age >= 18 and age < 65:
#     if gender == 'M':
#         print('father')
#     else:
#         print('mother')
# else:
#     if gender == 'M':
#         print('grandfather')
#     else:
#         print('grandmother')

# a = ['foo', 'bar']

# while len(a): #Selama len(a) > 0
#     print(a.pop(0)) #mengeluarkan list a elemen ke-0 dna mereturn
#     #nilai yang hendak dikeluarkan tersebut
    
#     b = ['baz', 'qux']
    
#     while len(b):
#         print('B >', b.pop(0))

# for item in a:
#     print(item)

# d = {'foo':1,'bar':2,'baz':3}
# for k in d:
#     print(k)

# d = {'foo':1,'bar':2,'baz':3}
# # for k in d:
# #     print(d[k])
# # #atau
# # for k in d.values():
# #     print(k)
# for k,v in d.items():
#     print(k, ":", v)


# for i in ['foo','bar','baz','qux']:
#     if 'b' in i:
#         break
#     print(i)

# for i in ['foo','bar','baz','qux']:
#     if 'b' in i:
#         continue
#     print(i)

# for i in ['foo', 'bar', 'baz', 'qux']:
#     print(i)
# else:
#     print('Done.')  # Will execute

for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 