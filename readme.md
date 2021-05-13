# Python tips and tricks to save time #
>tricks
>> Use Counter to count occurences
```

>>> from collections import Counter
>>> c = Counter()
>>> c[’a’] += 1  # the key does not exist, so it is created
Counter({’a’: 1})
>>> c = Counter(’cowboy bebop’)
Counter({’o’: 3, ’b’: 3, ’c’: 1, ’w’: 1, ’y’: 1, ’ ’: 1, ’e’: 1, ’p’: 1})

```

>> Use defaultdict to create keys on the fly
```
>>> from collections import defaultdict
>>> g = defaultdict(list)
>>> g[’paris’].append(’marseille’) # ’paris’ key is created on the fly
>>> g[’paris’].append(’lyon’)
>>> g
defaultdict(<class ’list’>, {’paris’: [’marseille’, ’lyon’]})
>>> g[’paris’] # behaves like a dict
[’marseille’, ’lyon’]
```

> Frequent Errors
```
#1
A = [1, 2, 3]
B = A # Beware! Both variables refer to the same object

#2
A = [1, 2, 3]
B = A[:] # B becomes a distinct copy of A

#3
M = [[0] * 10] * 10 # Do not write this!

#4 Square matrix can be initialized correctly using these expressions
M1 = [[0] * 10 for _ in range(10)]
M2 = [[0 for j in range(10)] for i in range(10)]

```

> Input-Output
>> if the input file is called test.in, and your program is prog.py, the contents of the input file can be directed to your program with the following command, launched from a command window
  **python prog.py < test.in**

>> 
