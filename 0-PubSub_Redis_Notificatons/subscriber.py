import redis

channel = 'test1'  # show which channel to listen to
def subscriber(channel):

	client = redis.Redis(host='127.0.0.1', port=6378)
	p = client.pubsub()  # pubsub feature
	p.subscribe(channel)  # subscribe to that channel

	while True:
		message = p.get_message()
		if message:
			print(message)
			print(message['data'])

subscriber(channel)
