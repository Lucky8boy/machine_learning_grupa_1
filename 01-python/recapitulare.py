# my_list = [8, 2, -3, 4, 2]
# print(len(my_list))

my_tuple = (1, 7)
print(type(my_tuple))

dictionar = {"key": "value", "key2": "value2", "key": "value3"}
print(dictionar["key2"])
print(dictionar.get('key3', "nu are valoare"))
print(dictionar)

dictionar.update({"key5": "value5", "key6": "value6"})
print(dictionar)

for i in dictionar:  # iteration thru keys
    print(i)

for i in dictionar.keys():  # same
    print(i)

for i in dictionar.values():  # iteration thru value
    print(i)

for k, v in dictionar.items():  # iteration thru both
    print(k, v)

my_set = {1, 2, 3, 2}

# print(my_set[2])

my_var = 5
if my_var < 6:
    print('6')