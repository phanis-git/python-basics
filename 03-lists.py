tools = ["linux","shell scripting","ansible","terraform","docker","kubernetes","argocd","jenkins"]
# length of list
print("length :", len(tools))
# slicing  ["start","end","step"]
print(tools[0:2])
print(tools[0:7:2])

newTools = ["linux","shell scripting","ansible","terraform","docker","kubernetes","argocd","jenkins"]
# we can do negative indexing , reverse
print(newTools[-1:-3:-1])


# List is a mutable datatype
# Mutable: Once defined, can change at any time E.g. List, dictonaries
# Immutable: Once defined, can't be changed E.g. Tuple, sets

# dir() :- used to check what are operations we can perform on specific variable or datatype
print("List of operations" , dir(newTools))
#  ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
#  '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__',
#  '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend',
#  'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# append: used to append at end of list
num1 = [1,2,3]
num1.append(4)
print(num1)

# Difference between append and extend
num1.append([5,6])
print(num1)
num1.extend([7,8])
print(num1)

# index
print(num1.index(8))

# insert : - insert the value before the given index   insert(index,value)
num1.insert(0,10)
print(num1)

# remove:- removes the first occurance of value
num1.remove(10)
print(num1)

# reverse:

arr1=["a","b","c"]
arr1.reverse()
print(arr1)
arr1=arr1[::-1]
print(arr1)

# sort: 
servers = [1,8,9,2,3]
servers.sort()
print("sort servers" , servers)

servers_1 = sorted(servers)
print("sorted" , servers, servers_1)


# remove
servers_1.remove(9)
print("remove", servers_1)
# If the value not present in list and if we want to remove it , it will throw error
# servers_1.remove(10)
# print("remove", servers_1)