import redis

r = redis.Redis('192.168.99.100')

product = [
    { # dictionary - cause redis map key with value
        "color": "black", # like hashes inside redis
        "price": 49.99,
        "style": "fitted",
        "quantity": 5,
        "nPurchased": 0,
    },

    {
        "color": "maroon",
        "price": 60,
        "style": "Office Shirt",
        "quantity": "6",
        "nPurchased": 0,
    },

    {
        "color": "Pink",
        "price": 79.99,
        "style": "Over Shirt",
        "quantity": "3",
        "nPurchased": 0,
    }

]

shirts = dict()
id = 1
for i in product:
    key = f"shirt:{id}"
    shirts[key] = i
    id += 1

print(shirts) # {'shirt:1':{'color': 'black',...}, 'shirt:2':{},..}

r.flushdb()  # For Development Environment only, not Production
            # delete all of your keys inside redis

pipe = r.pipeline() # without it we hit db as many times as for loop runs

for s_id, shirt in shirts.items():
    for field, value in shirt.items():
        pipe.hset(s_id, field, value) # s_id - key name,
                                    # field, value - separate them to store in db

pipe.execute() # execute all commands at once only

r.close()

# inside redis-cli
# hgetall shirt:1
# 1) "color"
# 2) "black"
