keys = ["name", "age", "city"]
my_dict = dict.fromkeys(keys)

print("新字典:", my_dict)

#新字典: {'name': None, 'age': None, 'city': None}

#______________________________________________________-

keys = ["name", "age", "city"]
value = "Unknown"
my_dict = dict.fromkeys(keys, value)

print("新字典:", my_dict)

#新字典: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}


