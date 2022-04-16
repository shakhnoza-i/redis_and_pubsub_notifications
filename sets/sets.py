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
