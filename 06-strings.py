# String is immutable means it cannot change
sample_s1 = "My name is Phani"
print(sample_s1[0])

# sample_s1[0] = "I"
# print(sample_s1[0])   # It will throw error because string is immutable

print(dir(sample_s1))

"""
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__',
   '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
     '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
       '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold',
         'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
           'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
             'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
               'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
                 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
                   'upper', 'zfill']
"""

sample_s2 = "PhaniKUMAR"
print(sample_s2.capitalize())
print(sample_s2.lower())
print(sample_s2.upper())
print(sample_s2.center(20,"#"))

# reverse a string
sample_s3 = "Phani"
print(sample_s3[::-1])

# Type casting
print(list(sample_s3) , tuple(sample_s3))

sample_s4 = "Good morning, how are you"
print(sample_s4.split(" "))
print(sample_s4)
print("#".join(sample_s4.split(" ")))