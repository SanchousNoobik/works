dict = {'a': 3, 'b': 4, 'c': 1, 'd': 2, 'e': 6}
a = list(dict.keys())[0]
b = list(dict.keys())[-1]
d = dict[b]
c = dict[a]
dict[b] = c
dict[a] = d
del dict[list(dict.keys())[1]]
dict["new_key"] = "new_value"
print(dict)