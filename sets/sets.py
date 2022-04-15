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
integer 4 - as output

get the value of key
> smembers party
return unordered collection of strings

check that particular member exists in your set or not 
> sismember key member
return 0 - if not exists, 1 - if exists
"""
