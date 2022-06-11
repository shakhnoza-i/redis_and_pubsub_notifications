"""
    18. Getting Started with Strings

set new key if is not exist
> set <keyname> <keyvalue> nx

appends the value at the end of the string
> APPEND mykey "Hello"
command line return integer <length of keyvalue>

Increments the number stored at key by one
> INCR mykey

Increments the number stored at key by some value
> INCRBY mykey <some_value>

Decrements the number stored at key by one
> DECR mykey

Decrements the number stored at key
> DECRBY mykey 3

Increment the string representing a floating point number
> INCRBYFLOAT mykey 0.1
"""


"""
    19. Different Ways to work with String

Atomically sets key to value and returns the old value stored at key
> GETSET mycounter "0" 

Sets the given keys to their respective values
> MSET key1 "Hello" key2 "World"

Returns the values of all specified keys
> MGET key1 key2

Set key to hold string value if key does not exist
> SETNX mykey "Hello"

Sets the given keys to their respective values if all keys don't exist
> MSETNX key1 "Hello" key2 "there"
"""


"""
    20. Wrapping up String Section

Returns the substring of the string value stored at key
> GETRANGE mykey 0 3

set name samsung
get range name 0 3  - > return "sams" in output
> GETRANGE mykey -3 -1. (-1 means the last character and so on)

set key to hold the string value and set key to timeout number of seconds
> SETEX mykey 10 "Hello"

expire time is specified in milliseconds instead of seconds
> PSETEX mykey 1000 "Hello"

overwrites part of the string stored at key
> SETRANGE key1 6 "Redis"

returns the length of the string
> STRLEN mykey
"""