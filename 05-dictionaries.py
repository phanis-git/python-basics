d = {}
d1 = dict()
# Dictionaries are mutable , values can be changes but keys are not changed in dictionary
d2 = {"name":"phani", "age":"25", "role":"DevOps Engineer"}
print(type(d2))
print("my name is " , d2["name"])
print("my age is " , d2.get("age") )
print("my roll no is " , d2.get("rollNo") )  # get() method will return None if key not found which is safe
# print("my rollNo is " , d2["rollNo"])     # but if we directly access with [] if key not found it will through error


print(dir(dict))
"""
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__',
   '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
     '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
       '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy',
         'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 
'values']
"""


sample_d1 = {"name":"phani", "age":"25", "role":"DevOps Engineer", "designation":"DevOps Engineer"}
print(sample_d1.keys())
print(sample_d1.values())

print(sample_d1.items())