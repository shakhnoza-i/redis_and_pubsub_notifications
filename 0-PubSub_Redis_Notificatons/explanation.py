""" 
Publish and subscribe allows for simple message buses to be created
This allows Redis to act as a broker for multiple clients providing a 
simple way to post and consume messages and events.
Senders are also called as publishers and receivers - is subscribers.

How pub/sub work?
- Senders are not programmed to send their messages to specific receivers. 
It means that when you send any information onto a channel sender doesn't 
know who will be the receiver.
- Subscriber expressed interest in one or more channels and only receive 
messages from subscrubed channels without knowledge of what if publishers 
there are. Possible - try to subscribe a channel that doesn't exist
Only those subscribers will get the message who are subscribed at the time 
of sending the message.
Redis doesn't guarantee delivery of your message sent on the channel
"""
