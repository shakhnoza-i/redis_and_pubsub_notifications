"""
    22. Introduction to List in Redis

Redis lists are implemented via Linked Lists. But the properties of a List 
implemented using an Array are very different from the properties of a List 
implemented using Linked List. Accessing an element by index is very fast in 
first one and no so fast using linked lists.
"""


"""
    23. Working with List in Redis

Insert all the specified values at the tail of the list stored at key
> RPUSH mylist "hello"

Returns the specified elements of the list stored at key
> LRANGE mylist 0 -1

Insert all the specified values at the head of the list stored at key
> LPUSH mylist "world"

Inserts value at the tail of the list stored at key, only if key already exists
> RPUSHX mylist "World" 

Inserts value at the head of the list stored at key, only if key already exists
> LPUSHX mylist "World" 

Removes and returns the last element of the list stored at key
> RPOP mylist

Removes and returns the first element of the list stored at key
> LPOP mylist 
"""

"""
    24. Wrapping up List Commands

truncate an existing list so that it will contain only the specified range of elements
> LTRIM mylist 1 -1

Sets the list element at specified index position
> LSET mylist 0 "four"

Returns the element at index in the list stored at key
> LINDEX mylist 0

Inserts value in list stored at key either before or after the reference value pivot
> LINSERT mylist BEFORE "World" "There"

Returns the length of the list stored at key
> LLEN mylist

Removes the 2 occurrences of elements equal to value from the list stored at key - 
from head to tail
> LREM mylist 2 "hello"

Removes the 2 occurrences of elements equal to value from the list stored at key - 
from tail to head
> LREM mylist −2 "hello"

Removes all occurrences of elements equal to value from the list stored at key
> LREM mylist  0 "hello"
"""
