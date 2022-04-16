"""
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
