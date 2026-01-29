s1 = {};  # This is dictionary and it contains key value pair 
s2 = {1,2,3,4}  # This is set , it doesnot contain key value pair , it just contain values with {}
s3 = set()  # we can define the set like this also
print(type(s1))
print(type(s2))
print(type(s3))

# sets removes the duplicate values and give the unique values
# sets are unordered collection
s4 = set({1,2,3,4,1,2})   
print(type(s4))
print(s4)

print(dir(set()))

"""
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__',
   '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__',
     '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
       '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__',
         '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
           '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
             'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint',
               'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
                 'symmetric_difference_update', 'union', 'update']

"""


