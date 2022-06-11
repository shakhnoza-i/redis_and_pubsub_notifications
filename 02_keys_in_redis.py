# Basically inside keys we store our data in Redis

"""
    10. Working with Keys in Redis

> Set Key value
> Get Key
> DEL key1 key2 key3 (To delete a key)
> EXISTS key1 key2 (To check a key exist or not)
> TTL key  (To check time to live)
> EXPIRE key 10(set EXPIRATION to key in seconds)
> PTTL mykey (to check time in millisecond)
> PEXPIRE mykey 1500 (Time in Milliseconds)
> PERSIST mykey (Remove EXPIRATION from the key)
> KEYS a?? (Returns all keys matching pattern)
(integer) -2 - mean key is expired
(integer) -1 - mean key doesn't have expiration time
expire a key - this key isn't available after this time    
"""


"""
    11. Pattern Matching with Keys

Return all keys matching pattern

return list of keys like hallo, hillo and etc
> keys h?llo

return all keys
> keys *
"""


"""
    12. Understanding Shutdown Command
shutdown save(nosave)    
"""


"""
    13. Some more commands
Return a random key from the currently selected database
> randomkey

Renames key to newkey - in any case
> rename mykey newkey

Renames key to newkey if newkey does not yet exist
> renamenx mykey newkey

Alters the last access time of a key(s)
> touch key1 key2

The actual removal will happen later asynchronously
> unlink key1 key2 key3 

Return Type of Value
> type key1
"""


"""
    14. Dump & Restore in Redis

Serialize the value stored at the key in a Redis-specific format
> dump mykey
Also dump command is used to take backup of your data

    With dump command simply we serialize the value in Redis specific format 
which user can't read but using that serialized value you can backup your data

Serialized value created by a specific Redis version can't be decoded by another 
version
> restore mykey 0 
"\n\x17\x17\x00\x00\x00\x12\x00\x00\x00\x03\x00\”
We can make restore only for deleted key
"""
