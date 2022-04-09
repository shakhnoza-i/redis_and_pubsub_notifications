import redis
import sys

ctx = {'data': {'task': 'name_of_task', 'user': 'test1'}}


def publisher(ctx):

	channel = ctx['data']['user']
	event = ctx['data']['task']
	action = f"{channel} closed task {event}"

	client = redis.Redis(host='127.0.0.1', port=6378)
	print(channel, action)

	return client.publish(channel, action)

publisher(ctx)
