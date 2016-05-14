#!/usr/bin/env python
# -*- coding: utf-8 -*-
#producer mode
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("Received %r" % body)
    #time.sleep(10)
    print('OK')
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(callback,
                        queue='hello',
                        no_ack=False)
print('[*] Waiting for messages, To exit press CTRL+C')
channel.start_consuming()
