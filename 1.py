data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data:
    if i % 2 == 0:
        out.append((i, i**2))
print(out)
# или
def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res) #[2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))

#или
data = '15 156 96 3 5 8 52 5'
data = list(map(int, data.split()))
print(data)

#или
def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res) #[2, 8, 38]
res = list(map(lambda x: (x, x ** 2), res))
print(res)

#filter
data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)

#или
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
print(res) #[2, 8, 38]
res = list(map(lambda x: (x, x ** 2), res))
print(res)

#Функция zip
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)

#или
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
data = list(zip(users, ids, salary))
print(data)

#Функция enumerate тип данных кортеж
users = ['users1', 'users2', 'users3']
data = list(enumerate(users))
print(data)

#Файлы
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()

#или
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
print(56)

#или режим чтения
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

#Модуль OS
import os
os.chdir('C:/Users/79190/PycharmProjects/GB')

#или
import os
print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'

#или
import os
print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #
'main.py'

#или
import os
print(os.path.abspath('main.py'))
 'C:/Users/79190/PycharmProjects/webproject/main.py'

#Модуль shutil
import shutil
