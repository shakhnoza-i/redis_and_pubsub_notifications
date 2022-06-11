"""
    64. Introduction to Publish/Subscribe

    It allows for simple message buses to be created
This allows Redis to act as a broker for multiple clients providing a simple way 
to post and consume messages and events.

In this section we will finish up some typical use cases for publish and subscribe.
Senders are also called as publishers and receivers are also called subscribers.

    Senders are not programmed to send their messages to specific receivers. 
It means that when you send any information onto a channel sender doesn't know 
who will be the receiver.

    Subscriber expressed interest in one or more channels and only receive messages 
that are of interest without knowledge of what if publishers there are.

    Only those subscribers will get the message who are subscribed at the time of 
sending the message.

Redis doesn't guarantee delivery of your message sent on the channel
"""


"""
    65. Publish/Subscribe Commands

> publish ch1 "Hello"
> subscribe ch
"""


"""
    66. Working with Patterned Subscription
Pattern subscription

create a pattern to subscribe all channels where name is started with ch
> psubscribe ch*

it will be matching like this ch1 or ch2 or che - only for one of this characters
> psubscribe ch[12e] 

for some administration tasks
> pubsub
pubsub command have sub commands and using sub commands you can check out number 
of subscribers etc

check number of subscribers, but it doesn't check for number of subscribers 
for a patterned subscription
> pubsub Numsub ch1

check number of subscribers for a patterned subscription
> pubsub numpat
"""
