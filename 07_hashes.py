"""
    36. What are Hashes

    Hashes are maps between string fields and string values
They are perfect datatype to represent object - object type data like a user 
with number of fields like name surname and age and many more.

    Hashes are mainly used to represent objects but they are capable of storing 
many elements too so it's your choice to use hashes in other tasks as well

    Capacity of hash is really great - every hash can store up to 2^32 - 
1 field-value pairs
"""


"""
    37. Hash Creation Commands

Sets field in the hash stored at key to value. If field already exists in the hash, 
it is overwritten
> HSET myhash field1 "Hello"

Returns the value associated with field in the hash stored at key
> HGET myhash field1

Set Multiple values
> HMSET myhash field1 "Hello" field2 "World"

Returns all fields and values of the hash stored at key
> HGETALL myhash

Returns the values associated with the specified fields in the hash stored at key
> HMGET myhash field1 field2

Returns if field is an existing field in the hash stored at key
> HEXISTS myhash field1

Returns all field names in the hash stored at key
> HKEYS myhash

Returns the number of fields contained in the hash stored at key
> HLEN myhash
"""


"""
    38. More on Hashes Commands

Sets field in the hash stored at key to value, only if field does not yet exist
> HSETNX myhash field "Hello"

Removes the specified fields from the hash stored at key
> HDEL myhash field1

Increments the number stored at field in the hash stored at key by increment
> HINCRBY myhash field 1

Increment the specified field of a hash stored at key, and representing a floating 
point number, by the specified increment
> HINCRBYFLOAT mykey field 0.1

Returns the string length of the value associated with field in hash stored at key
> HSTRLEN myhash f1

Returns all values in the hash stored at key
> HVALS myhash
"""
