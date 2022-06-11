"""
   1. Introduction to Redis

   Redis is an open source in memory data structures store used as a database, 
cache and message broker.
   Caching is a process of storing data into a cache and cache is a temporary 
storage component area where the data is stored so that in future data can be 
served faster.

   In caching we don't store our data on our secondary devices like hard disk, but 
we store our data into temporary storage
   Redis is a NoSQL database which follows the principle of key value store.
Redis holds its database entirely in the memory, using that disk only for 
persistence. So when you run your redis, then all of your data is stored entirely 
in the memory. And when you shutdown your redis, then you have option to store 
your data onto the disk or not.
   Redis supports data structures such as string, hashes, lists, sets, sorted sets 
with range of queries, bitmap, hyperloglogs. Other key-value db doesn't support 
these much of varieties.
   Redis is written in ANSI C.

   redis-py -most popular redis client
"""


"""
   5. Configuring Redis Inside Docker
   
Redis client is the program that interacts with your redis server.
~$ docker run --name redis_db -p 6379:6379 redis

to start existing container
~$ docker start -ai <name>

to run redis client
~$ docker exec -it redis_db redis-cli
"""