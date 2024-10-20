immutable_var = 1, 2, 3, 4 ,5, 'bingo', 'salo'
print(immutable_var)
#immutable_var[4] = 20
# Выдает ошибку что не может поменять символ
# TypeError: 'tuple' object does not support item assignment
mutable_list = ['Big', 'car', 'Banana', 'list' ]
#mutable_list[0][2] = 2
mutable_list[2] = '!!!zamena!!!'
mutable_list.append('finish')
print(mutable_list)