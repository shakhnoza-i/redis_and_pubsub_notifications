"""
Sorted sets are mix between set and hash.

In some sense a sorted set is a set as well so in sets what we could do we 
can store some elements and those elements are non repeating and they were 
unique.

Sorted sets elements are ordered.

Every element in sorted set is associated with a floating point value called 
the score (this is why the type is also similar to a hash, since every element 
is mapped to a value
"""

"""
Create set with values or add values to existing set
> zadd key index value 
> zadd students 1 Rob 2 John 3 Smith
index can only be froat type

Get set values
> zrange key[0 -1]
> zrange students 0 -1
> zrange students 0 -1 withscores

ZADD options
> zadd key [NX|XX] [CH] [INCR] score member
NX - don't update any existing elements instead add new elements
In redis you can map multiple values to one particular score(index), so one
index can consist multiple values and in one index values sorted in 
alphabetical order
XX - can only update already existing element but you can't never add new 
elements
CH - will return an integer that tell us that how many elements have been 
changed using this zadd
INCR - increment value of score 
> zadd key student incr 2 Bob
add 2 to existing score of Bob
"""
