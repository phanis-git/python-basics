t1 = ()
t2 = tuple()
t3 = tuple(["linux","shell scripting","ansible","terraform","docker","kubernetes","argocd","jenkins"])
sample_t1 = ("linux","shell scripting","ansible","terraform","docker","kubernetes","argocd","jenkins")

print(type(t1) , t1)
print(type(t2) , t2)
print(type(t3) , t3)
print(type(sample_t1) , sample_t1)

# Tuples are same like list , but list is mutable whereas tuples are immutable
# Tuples doesnot change its values

print(dir(sample_t1))  # these are the operations we can perform on tuples
"""['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
   '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
     '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
       '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']"""

sample_t2 = (1,2,5,4,5,7)
print(sample_t2.count(5))   # it will return how many 5's in tuple
print(sample_t2.count(10))   # if not present in tuple it will return 0
print(sample_t2.index(5))    # it will return the first occurance index of the element


# Datatype conversion or Type casting
sample_list = list(sample_t2)   # converting tuple to list
print(type(sample_list))

sample_tuple = tuple(sample_list)   # converting list to tuple
print(type(sample_tuple))