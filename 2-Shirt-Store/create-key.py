import redis

r = redis.Redis('192.168.99.100')
r.flushdb()

i = 1
pipe = r.pipeline()
while i <= 14:
    name = f"check:{i}"
    data = f"hello:{i}"
    pipe.set(name, data)
    i += 1

pipe.execute()
i = 0
while True:
    i, val = r.scan(i, match="check*")
    print("cursor=", i, val)
    if i == 0:
        break

r.close()

"""
Keys * command or any pattern that you specify here is a blocking operation.
It means that it will block your DB and it will waste your resources.
In development enviroment we should use cursors that we use to fetch keys.

So to use the concept of cursor, you have to write scan.
Now when you write scan - telling redis I want to scan over my keys.
> scan 0 match check*
output of cursor value is "0", it means that you have got all of your keys.
if outputs differ from "0" - use this output value to get the next bunch of keys
Remember: don't use keys command in production, use scan instead.
"""
