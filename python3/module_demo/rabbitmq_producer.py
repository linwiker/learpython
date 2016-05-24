#!/usr/bin/env python
# -*- coding: utf-8 -*-
#producer mode
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello', durable=True)
for i in range(10000000):
    channel.basic_publish(exchange='',routing_key='hello',body='Hello World! {0}'.format(i), properties=pika.BasicProperties(delivery_mode=2,))
    print("{0} Sent 'Hello World!'".format(i))
connection.close()

