immutable_var = 1,2,3, "Dima"
print(immutable_var)
        #immutable_var[0][0] = 2 Кортеж служт инструментом для неизменяемых данных. Его успользуют, при работе с данными когда
        #нужно быть уверенным что данные не потеряют свое значение. В кортеж можно добавить изменяемые структуры
        #При попытке изменить картеж, будет выдавать ошибку "TypeError: 'int' object does not support item assignment"
mutable_list = ([2,3,4], 32)
print(mutable_list)
mutable_list[0][0] = 4
mutable_list[0][2] = 9
print(mutable_list)