"""   
Redis sets are an unordered collection of strings

It is possible to add, remove and test for existence of members 
so it's just basic commands that we can operate on sets
O(1) - dependancy

They support a number of server-side commands to compute sets starting
from existing sets - union, intersection, difference of sets
"""

"""     
Sets basic commands

add set with key party
> sadd party Bob Rob Robert Sam
return integer 4 - as output

get the value of key
> smembers key
return unordered collection of strings

check that particular member exists in set or not 
> sismember key member
return 0 - if not exists, 1 - if exists
this command is case sensitive

check total number of elements in set
> scard key

move one member of set into another set
> smove source destination member

remove one or more(quantity) random elements from set 
> spop key quantity 
return removed elements

remove a member(s) from set
> srem key member
"""


"""
    Sets Operations

A = {1,2,3}   B = {3,4,5}

Difference of two sets written as A - B is the set of all elements of A
that doesn't exist in B.
difference A-B = {1,2}
diffenence B-A = {4,5}
> sdiff A B
Save the difference in another key
> sdiffstore C A B


Intersection of two sets A and B is the set of all elements that both in A 
and B.
intersection A&B = {3}
> sinter A B
> sinterstore C A B - save in C


Union - is combine all of the elements of two sets into one new set without
repetition
union AuB = {1,2,3,4,5}
> sunion A B
> sunionstore C A B

Random - get random element from a set
> srandmember A

We can also apply basic commands than we learned previously like - del key
"""
