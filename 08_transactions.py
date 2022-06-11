"""
    40. What is a Transaction

Transaction in redis consist of block of commands. Using transaction you can 
just process batch of commands at once

Commands multi, exec, discard and watch - are the foundation of transaction in 
redis.

All the commands in transaction are serialized and executed sequentially. 
(consistently, one after another - not random)

    Isolated - it can never happen that a request issued by another client is 
served in the middle of execution of redis transaction. This guarantees that 
commands are executed as single isolated operation.

    Redis transaction is also atomic - if you try to execute batch of command in 
redis using transaction  - if any command fails then redis will not process rest 
of the commands.

Like ACID in SQL DB, but without D-durability
"""


"""
    41. Working with multi and exec

Multi - you are now inside a transaction
Queue will be executed when we will be running command Exec

127.0.0.1:6379> multi
OK
127.0.0.1:6379> set bank1 5000
QUEUED
127.0.0.1:6379> set bank2 3000
QUEUED
127.0.0.1:6379> exec
1) OK
2) OK

Redis doesn't support rollback - yes many other databases out there supports 
rollback but Redis doesn't have this
"""


"""
    42. Understanding Unwatch

    Discard - abort a transaction

    Watch - check and set behavior to redis transaction. watch is used to do 
monitoring over your key and provide check and said behavior. And if there 
is any changes in your key then it stops your transaction.

    Watch is used to provide check and set behavior and if there is any change 
in your key outside the transaction then watch restrict exec to execute.

    Unwatched mean just telling redis that you don't want to monitor your key. 
It will flush all the watched keys, we can't specify what key to unwatch
"""


"""
    45. Pipeline in Redis

    Concept of pipelines where we can group related commands together. 
And all of the commands will be going to hit the database only once. 
Without pipeline we hit database as many times as many commands we execute.
    Now by using this pipelining concept, you save a lot of network cost. 
You minimize the latency involved. And lot of other things that speeds up your 
program.
"""
