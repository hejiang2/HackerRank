# a blueprint for data structures that take  pairs and map keys to their associated values # With dictionary, we can insert, find or delete.
# no restrictions on size, no guaranteed ordering

# Dictionary is a built-in Python Data Structure that is mutable. It is similar in spirit to List, Set, and Tuples. 
# However, it is not indexed by a sequence of numbers but indexed based on keys and can be understood as associative arrays.
# In Python, the Dictionary represents the implementation of a hash-table.

# Technically, it is not quite correct to say an object must be immutable to be used as a dictionary key. More precisely, an object must be hashable, which means it can be passed to a hash function. A hash function takes data of arbitrary size and maps it to a relatively simpler fixed-size value called a hash value (or simply hash), which is used for table lookup and comparison.

# Python’s built-in hash() function returns the hash value for an object which is hashable, and raises an exception for an object which isn’t.

# All of the built-in immutable types you have learned about so far are hashable, and the mutable container types (lists and dictionaries) are not. So for present purposes, you can think of hashable and immutable as more or less synonymous.

# Keys are immutable ( which cannot be changed ) data types that can be either strings or numbers. A key can not be a mutable data type, for example, a list.
# A tuple can also be a dictionary key, because tuples are immutable.
# Keys are unique within a dictionary and can not be duplicated inside a dictionary, in case if it is used more than once then subsequent entries will overwrite the previous value.
# Key connects with the value, hence, creating a map-like structure.
# A dictionary is represented by a pair of curly braces {} in which enclosed are the key: value pairs separated by a comma.

# To access the key value pair, you would use the .items() method, which will return a list of dict_items in the form of a key, value tuple pairs.
# To access keys and values separately, you could use a for loop on the dictionary or the .keys() and .values() method.
# You could even access a value by specifying a key as a parameter to the dictionary.

# Dictionary comprehensions can be used to create dictionaries from arbitrary key and value expressions. It is a simple and concise way of creating dictionaries and is often faster than the usual for loop implementations.
# dict_comprehension = {i: i**3 for i in range(200000)}
# A list of tuples works well:
# d = dict([
#     (<key>, <value>),
#     (<key>, <value),
#        .
#        .
#        .
#     (<key>, <value>)
# ])
# str = "key1=value1;key2=value2;key3=value3"
# d = dict(x.split("=") for x in str.split(";"))
# for k, v in d.items():
#     print(k, v)

# There are unkown number of queries: use while True and catch an exception when there's no input left. 
# Try Except
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
# try:
#   print(x)
# except:
#   print("An exception occurred")
# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error.


n = int(input())
phone_book = dict(input().split() for i in range(n))

while True:
    try: 
        name = input() # avoid Runtime Error
	# The in and not in operators return True or False according to whether the specified operand occurs as a key in the dictionary.
        if name in phone_book:
            print('{}={}'.format(name, phone_book[name]))
        else:
            print('Not found')
    except EOFError:
        break

# Without try except: EOFError: EOF when reading a line
# EOFError is raised when one of the built-in functions input() or raw_input() hits an end-of-file condition (EOF) without reading any data. This error is sometimes experienced while using online IDEs. This occurs when we have asked the user for input but have not provided any input in the input box. We can overcome this issue by using try and except keywords in Python. 
# This is called as Exception Handling.

# Built-in Dictionary Methods
# d.clear() empties dictionary d of all key-value pairs
# d.get(<key>[, <default>]) provides a convenient way of getting the value of a key from a dictionary without checking ahead of time whether the key exists, and without raising an error.
# d.get(<key>) searches dictionary d for <key> and returns the associated value if it is found. If <key> is not found, it returns None.
# If <key> is not found and the optional <default> argument is specified, that value is returned instead of None.
# d.items() returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the key’s value.
# d.keys() returns a list of all keys.
# d.values() returns a list of all values.
# d.pop(<key>[, <default>]) removes a key from a dictionary, if it is present, and returns its value. If <key> is present in d, d.pop(<key>) removes <key> and returns its associated value. d.pop(<key>) raises a KeyError exception if <key> is not in d. If <key> is not in d, and the optional <default> argument is specified, then that value is returned, and no exception is raised.
# d.popitem() removes a key-value pair from a dictionary. d.popitem() removes the last key-value pair added from d and returns it as a tuple. f d is empty, d.popitem() raises a KeyError exception.
# d.update(<obj>) merges a dictionary with another dictionary or with an iterable of key-value pairs. If <obj> is a dictionary, d.update(<obj>) merges the entries from <obj> into d. For each key in <obj>:
# If the key is not present in d, the key-value pair from <obj> is added to d.
# If the key is already present in d, the corresponding value in d for that key is updated to the value from <obj>.
