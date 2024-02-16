# text1 = 'karich'
# text2 = 'Shirak'
# list1 = list(text1)
# list2 = list(text2)
# list1.sort()
# list2.sort()
# print(list1 == list2)
# -------------------------------------------------
# mylist = []
# while True:
#     text = input('Enter text: ')
#     if text == '':
#         break
#     else:
#         mylist.append(text)
# print(mylist)
# -------------------------------------------------

# chars = ('!', '@', '#', '$', '%', '&', '*')
# while True:
#     number_count = 0
#     char_count = 0
#     password = input('Enter password: ')
#     if len(password) < 8:
#         print('Is not strong!!')
#     else:
#         for i in password:
#             if i.isdigit():
#                 number_count += 1
#             elif i in chars:
#                 char_count += 1
#         if number_count >= 2 and char_count >= 2:
#             print(password)
#             break
#         else:
#             print('Is not strong!!')
# -------------------------------------------------

# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# for i in range(0, len(link)):
#     if link[i] == '=':
#         print(link[i + 1:])
# -------------------------------------------------

# link = link.split('=')
# print(link[1])
# -------------------------------------------------

# link = link.partition('=')
# print(link[-1])
# -------------------------------------------------

# print(link[link.index('=') + 1:])
# -------------------------------------------------


# text = input('Enter text: ')
# print(text == text[::-1])
# -------------------------------------------------


# text = 'barev'
# print([i for i in text])
# print(list(text))
# mylist = []
# for i in text:
#     mylist.append(i)
# print(mylist)
# -------------------------------------------------

# number = input('Enter 5 numbers: ')
# mylist = number.split(' ')
# for i in mylist:
#     i = int(i)
#     if i % 2 == 0:
#         print(i)
# -------------------------------------------------

# mylist = [4, 4, 4, 5, 8, 7, 9, 4, 4, 1, 2]
# for i in mylist.copy():
#     if i % 2 == 0:
#         mylist.remove(i)
# print(mylist)
# -------------------------------------------------
# import random

# mylist = ['Vazgen', 'Harut', 'Hayk Komitas', 'Abo Avan', 'Karen']
# newlist = []
# while mylist != []:
#     random_user = random.choice(mylist)
#     newlist.append(random_user)
#     mylist.remove(random_user)
# for i in range(0, len(newlist) - 1):
#     print(f'{newlist[i]} --> {newlist[i + 1]}')
# print(f'{newlist[-1]} --> {newlist[0]}')
# -------------------------------------------------
# mylist = [4, 4, 5, 8, 7, 8, 5, 6, 5, 4, 1, 2, 1, 4, 5, 8, 7, 4]
# newlist = []
# for i in mylist:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)
# -------------------------------------------------
# mylist = [4, 4, 5, 8, 7, 8, 5, 6, 5, 4, 1, 2, 1, 4, 5, 8, 7, 4]
# for i in mylist.copy():
#     if mylist.count(i) > 1:
#         mylist.remove(i)
# print(mylist)
# -------------------------------------------------
# 112, 113, 114, 115, 116, 117
# -------------------------------------------------

# n = int(input('Enter number'))
# mylist = []

# for i in range(2,n+1):
#     for j in range(2,i//2+1):
#         if i % j == 0:
#             break
#     else:
#         mylist.append(i)
# print(mylist)
# -------------------------------------------------
# mylist = [1, 2, 3, 4]
# sub_list = []
# for i in range(len(mylist) + 1):
#     for j in range(i + 1, len(mylist) + 1):
#         sub = mylist[i:j]
#         sub_list.append(sub)
# sub_list.sort(key = len)
# print(sub_list)
# -------------------------------------------------

# info = {
#     'elbakyanPython@gmail.com': 'I Love Python (ONLY)',
#     'vardan@gamil.com': 'No UXUI'
# }



# data = {
#     'a':10,
#     'b':5,
#     'c':70
# }

# print(data.keys())
# print(data.values())
# print(data.items())
# print(data)
# print(data['a'])
# print(data[0])
# print(data.get('b', 'Chka'))
# data['d'] = 30
# data['a'] = 30
# print(data)
# data.setdefault('v', 10)
# print(data)
# data.clear()
# print(data)

# data = ['Shirak', 'Lyova', 'Anzhela', 'Narine', 'Abo']
# age = [26, 21, 'End Process', 18, 16]
# mydict = {}
# for i, j in zip(data, age):
#     mydict[i] = j
# print(mydict)


# data = ['Shirak', 'Lyova', 'Anzhela', 'Narine', 'Abo']
# age = 35
# mydict = dict.fromkeys(data, age)
# print(mydict)


# data = ['Shirak', 'Lyova', 'Anzhela', 'Narine', 'Abo']
# age = 35
# mydict = {}
# for i in data:
#     mydict[i] = age
#     age += 1
# print(mydict)

# data = {
#     'a':10,
#     'b':5,
#     'c':70
# }
# my_values = sorted(data.values(), reverse=True)
# print(my_values)
# my_keys = sorted(data, key=data.get)
# print(my_keys)